from urllib.request import urlopen, Request
from json import loads, dumps
from typing import Any, Dict, List
from urllib.parse import quote_plus

from wikibase.compiler import Cmd

from .django_model import DjangoModel
from .django_property import DjangoProperty

from time import sleep
from logging import getLogger

charset_map = dict()

# https://github.com/yuvipanda/python-wdqs/blob/master/wdqs/client.py


class Loggable:

    def __init__(self):
        self.logger = getLogger(f'{__name__}.{self.__class__.__name__}')

    def debug(self, *args, **kwargs):
        self.logger.debug(args, kwargs)


class WbDatabase:
    SHRT_MIN = 1
    SHRT_MAX = 1
    INT_MIN = 1
    INT_MAX = 1
    LONG_MIN = 1
    LONG_MAX = 1

    ISOLATION_LEVEL_READ_COMMITED = 1

    _BASE_URL = '_base_url'
    _MEDIAWIKI_VERSION = '_mediawiki_version'
    _INSTANCE_OF = 'instance of'
    _SUBCLASS_OF = 'subclass of'
    _DJANGO_MODEL = 'django model'
    _DJANGO_NAMESPACE = 'django namespace'
    _DJANGO_APPLICATION = 'django application'
    _DJANGO_FIELD = 'django field'
    _SPARQL_ENDPOINT = '_sparql_endpoint'

    class Error:
        ...

    class DatabaseError(BaseException):
        ...

    class IntegrityError(BaseException):
        ...

    class OperationalError(BaseException):
        ...

    class DataError(BaseException):
        ...

    class InternalError(BaseException):
        ...

    class NotSupportedError(BaseException):
        ...

    class InterfaceError(BaseException):
        ...

    class ProgrammingError(BaseException):
        ...

    @staticmethod
    def get_property_type_for_django_field(field: DjangoProperty) -> str:
        django_field_type = field['property_type']
        if django_field_type == 'CharField':
            return 'string'
        if django_field_type == 'AutoField':
            return 'quantity'
        if django_field_type == 'ForeignKey':
            return 'wikibase-item'
        if django_field_type == 'DecimalField':
            return 'quantity'
        if django_field_type == 'IntegerField':
            return 'quantity'
        if django_field_type == 'DateTimeField':
            return 'time'
        raise WbDatabase.InternalError(
            f'Sorry I can\'t recognize type: {django_field_type} for field {field}.')

    @staticmethod
    def connect(charset: str = 'utf8', url: str = '',
                user: str = '', password: str = '',
                instance_of_property_id: int = None,
                subclass_of_property_id: int = None,
                django_model_item_id: int = None,
                wdqs_sparql_endpoint: str = None,
                django_namespace: str = None):
        return WbDatabaseConnection(charset, url,
                                    user, password,
                                    instance_of_property_id,
                                    subclass_of_property_id,
                                    django_model_item_id,
                                    wdqs_sparql_endpoint,
                                    django_namespace)


class WbLink(dict):

    def __init__(self, id: int, entity_type: str, base_url: str):
        super().__init__(id=id, entity_type=entity_type,
                         url=f'{base_url}{self._entity_prefix(entity_type)}{id}')

    @staticmethod
    def _entity_prefix(entity_type: str) -> str:
        if not entity_type:
            return None
        first_letter = str(entity_type).upper()[:1]
        if first_letter == 'I':
            return 'Q'
        if first_letter == 'P':
            return 'P'
        raise WbDatabase.InternalError(
            f'Sorry I can\'t recognize entity type: {entity_type}')

    def get_entity_id(self) -> str:
        return f'{self._entity_prefix(self["entity_type"])}{self["id"]}'


class WbApi():

    def __init__(self, url: str, charset: str = 'utf-8'):
        super().__init__()
        self.url = url
        self.charset = charset

    def _retry(self, countdown: int, request: Request) -> dict:
        search_result = {}
        for i in range(0, countdown):
            response = urlopen(request)
            search_result = loads(response.read().decode(self.charset))
            if 'error' in search_result and 'code' in search_result['error'] and \
                    (search_result['error']['code'] == 'failed-save' or search_result['error']['code'] == 'no-automatic-entity-id'):
                sleep(1.27 ** i)
                continue
            return search_result
        raise WbDatabase.InternalError(
            f'Countdown exceeds limit {countdown}. The last search result is {search_result}.')

    def mediawiki_info(self):
        return loads(urlopen(
            f'{self.url}/api.php?action=query&meta=siteinfo&format=json').read().decode(self.charset))

    def search_items(self, query):
        if 'label' in query:
            label_search_string = query['label']
            search_result = loads(urlopen(
                f'{self.url}/api.php?action=wbsearchentities&search={quote_plus(label_search_string)}&language=en&type=item&format=json').read().decode(self.charset))
            return search_result['search']
        raise WbDatabase.InternalError('Only search by label implemented')

    def search_properties(self, query):
        if 'label' in query:
            label_search_string = query['label']
            search_result = loads(urlopen(
                f'{self.url}/api.php?action=wbsearchentities&search={quote_plus(label_search_string)}&language=en&type=property&format=json').read().decode(self.charset))
            return search_result['search']
        raise WbDatabase.InternalError('Only search by label implemented')

    def new_item(self, data):
        retrieve_csrf_token = loads(urlopen(
            f'{self.url}/api.php?action=query&meta=tokens&format=json').read().decode(self.charset))
        csrf_token = retrieve_csrf_token['query']['tokens']['csrftoken']
        post_request_body = f'token={quote_plus(csrf_token)}'
        search_result = self._retry(20, Request(
            f'{self.url}/api.php?action=wbeditentity&new=item&data={quote_plus(dumps(data))}&format=json', method='POST', data=post_request_body.encode('utf-8')))
        return search_result['entity']

    def new_property(self, data):
        retrieve_csrf_token = loads(urlopen(
            f'{self.url}/api.php?action=query&meta=tokens&format=json').read().decode(self.charset))
        csrf_token = retrieve_csrf_token['query']['tokens']['csrftoken']
        post_request_body = f'token={quote_plus(csrf_token)}'
        search_result = self._retry(20, Request(
            f'{self.url}/api.php?action=wbeditentity&new=property&data={quote_plus(dumps(data))}&format=json', method='POST', data=post_request_body.encode('utf-8')))
        return search_result['entity']

    def get_item_claims(self, entity_id: int, property_id: int = None):
        response = urlopen(Request(
            f'{self.url}/api.php?action=wbgetclaims&entity=Q{entity_id}&format=json' +
            (f'&poperty=P{property_id}' if property_id else ''),
            method='GET'))
        search_result = loads(response.read().decode(self.charset))
        return search_result['claims']

    def get_entities(self, wb_links: List[WbLink]) -> List[dict]:
        if not wb_links:
            return []
        entities_ids = '|'.join([wb_link.get_entity_id()
                                for wb_link in wb_links])
        response = urlopen(Request(
            f'{self.url}/api.php?action=wbgetentities&ids={entities_ids}&format=json',
            method='GET'))
        search_result = loads(response.read().decode(self.charset))
        return search_result['entities'].values()

    def new_claim(self, entity_type: str, entity_id: int, property_id: int, value: Any) -> dict:
        entity_id = f'{WbLink._entity_prefix(entity_type)}{entity_id}'
        snak_type = 'value' if value else 'novalue'

        retrieve_csrf_token = loads(urlopen(
            f'{self.url}/api.php?action=query&meta=tokens&format=json').read().decode(self.charset))
        csrf_token = retrieve_csrf_token['query']['tokens']['csrftoken']
        post_request_body = f'token={quote_plus(csrf_token)}'
        search_result = self._retry(20, Request(
            f'{self.url}/api.php?action=wbcreateclaim&entity={entity_id}&property=P{property_id}&snaktype={snak_type}&format=json' +
            (f'&value={quote_plus(dumps(value))}' if value else ''), method='POST', data=post_request_body.encode('utf-8')))
        return search_result['claim']


class WbCursor(Loggable):

    def __init__(self, django_namespace: str, wikibase_info: dict, api: WbApi):
        super().__init__()
        self.wikibase_info = wikibase_info
        self.django_namespace = django_namespace
        self.api = api

    def close(self):
        print('close')

    def _get_models(self, cmd: Cmd):
        if cmd['cmd'] == 'add_property':
            return (cmd['data']['model'], ) if not cmd['data']['property']['related_models'] else (cmd['data']['model'], cmd['data']['property']['related_models'][0])
        return None

    def get_or_create_item_if_not_found_by_name(self, item_name: str) -> Dict:
        # TODO: add claims if we'll create the new item
        entities = self.api.search_items({'label': item_name})
        if len(entities) == 1:
            return entities[0]
        if len(entities) == 0:
            entity = self.api.new_item(
                {'labels': {'en': {'language': 'en', 'value': item_name}}})
            return entity
        raise WbDatabase.InternalError(
            f'The entity {item_name} has another one (i.e. not unique)')

    def get_or_create_property_if_not_found_by_name(self, property_name: str, data_type_name: str) -> Dict:
        # TODO: add claims if we'll create the new property
        entities = self.api.search_properties({'label': property_name})
        if len(entities) == 1:
            return entities[0]
        if len(entities) == 0:
            entity = self.api.new_property(
                {'labels': {'en': {'language': 'en', 'value': property_name}}, 'datatype': data_type_name})
            return entity
        raise WbDatabase.InternalError(
            f'The property {property_name} has another one (i.e. not unique)')

    def _wb_link(self, snak: dict) -> DjangoProperty:
        return WbLink(
            snak['mainsnak']['datavalue']['value']['numeric-id'],
            snak['mainsnak']['datavalue']['value']['entity-type'],
            self.wikibase_info[WbDatabase._BASE_URL])

    def _general_model_label(self, model: DjangoModel):
        application = model['application']
        return f'{application}{" for " + self.django_namespace if self.django_namespace else ""}'

    def _model_label(self, model: DjangoModel):
        model_name = model['type'].split('.')[-1]
        return f'{model_name} in {self._general_model_label(model)}'

    def _check_or_create_model(self, model: DjangoModel):

        # Check general model
        general_model_label = self._general_model_label(model)
        if not(general_model_label in self.wikibase_info):
            # get application django model it contains general info
            application_model = self.get_or_create_item_if_not_found_by_name(
                general_model_label)
            application_model_id = int(application_model['id'][1:])
            application_model_claims = self.api.get_item_claims(
                application_model_id)
            # property_id = self.wikibase_info[WbDatabase._SUBCLASS_OF]
            # self.api.create_claim(item_id, property_id, value)
            # print(f'{application_model_claims}')
            # TODO: check claims and add if missed
            # subclass of [django model]
            # application name [application]
            # django namespace [self.django_namespace or snak no value]

            application_model['claims'] = application_model_claims
            self.wikibase_info[general_model_label] = application_model

        # Check concrete model
        concrete_model_label = self._model_label(model)
        if not(concrete_model_label in self.wikibase_info):
            concrete_model = self.get_or_create_item_if_not_found_by_name(
                concrete_model_label)
            concrete_model_id = int(concrete_model['id'][1:])

            django_field_property_id = self.wikibase_info[WbDatabase._DJANGO_FIELD]['id']
            # below is the request existed claims or add a placeholder for them
            concrete_model_claims = self.api.get_item_claims(concrete_model_id)
            if not (f'P{django_field_property_id}' in concrete_model_claims):
                concrete_model_claims[f'P{django_field_property_id}'] = []
            concrete_model_properties = [self._wb_link(property_value) for property_value in concrete_model_claims[f'P{django_field_property_id}']] \
                if f'P{django_field_property_id}' in concrete_model_claims else []

            concrete_model_fields = {
                p['labels']['en']['value'] for p in self.api.get_entities(concrete_model_properties)}
            # TODO: check claims and add if missed
            # subclass of [application model]
            # application name [application]
            # django namespace [self.django_namespace or snak no value]
            # id enumerator (primary sequence)

            # Create/Update properties
            for field in model['fields']:
                related_model_label = self._model_label(
                    field['related_models'][0]) if field['related_models'] else None
                related_models = f' to {related_model_label}' if related_model_label else ''
                property_type_name = f'{field["property_type"]}{related_models}'
                property_name = f'{field["property_name"]} type {property_type_name}'

                if property_name in concrete_model_fields:
                    continue

                # Create claim cause missed
                property = self.get_or_create_property_if_not_found_by_name(
                    property_name, WbDatabase.get_property_type_for_django_field(field))

                claim = self.api.new_claim('item', concrete_model_id, django_field_property_id, {
                                           'entity-type': 'property', 'numeric-id': int(property['id'][1:])})
                concrete_model_claims[f'P{django_field_property_id}'].append(
                    claim)

                print(f'{property}')

            concrete_model['claims'] = concrete_model_claims
            self.wikibase_info[concrete_model_label] = concrete_model
            print(f'{concrete_model}')

        print(f'{model}')

    def _add_property(self, cmd: Cmd, params: list):
        print(f'_add_property ${cmd} with ${params}')

    def _field_indexes(self, cmd: Cmd, params: list):
        print(f'_field_indexes ${cmd} with ${params}')

    def _create_foreignkey_constraint(self, cmd: Cmd, params: list):
        print(f'_create_foreignkey_constraint ${cmd} with ${params}')

    def _show_all_models(self, cmd: Cmd, params: list):
        print(f'_show_all_models ${cmd} with ${params}')

    def _remove_property(self, cmd: Cmd, params: list):
        print(f'_remove_property ${cmd} with ${params}')

    def _savepoint_create(self, cmd: Cmd, params: list):
        print(f'_savepoint_create ${cmd} with ${params}')

    def _savepoint_rollback(self, cmd: Cmd, params: list):
        print(f'_savepoint_rollback ${cmd} with ${params}')

    def _add_items(self, cmd: Cmd, params: list):
        print(f'_add_items ${cmd} with ${params}')

    def _last_insert_id(self, cmd: Cmd, params: list):
        print(f'_last_insert_id ${cmd} with ${params}')

    def _create_model(self, cmd: Cmd, params: list):
        self.debug('_create_model {} with {}', cmd, params)
        self._check_or_create_model(cmd['data']['model'])

    def _table_exists(self, cmd: Cmd, params: list):
        self.debug('_table_exists {} with {}', cmd, params)

    def _enable_constraints(self, cmd: Cmd, params: list):
        self.debug('_enable_constraints {} with {}', cmd, params)

    def _disable_constraints(self, cmd: Cmd, params: list):
        self.debug('_disable_constraints {} with {}', cmd, params)

    def _create_index(self, cmd: Cmd, params: list):
        self.debug('_create_index {} with {}', cmd, params)

    def _get_constraints(self, cmd: Cmd, params: list):
        self.debug('_get_constraints {} with {}', cmd, params)

    def execute(self, cmd, params) -> Any:
        if not isinstance(cmd, Cmd):
            # TODO: transform SQL-92 into commands
            raise WbDatabase.InternalError(f'Wrong command: {cmd}')
        models = self._get_models(cmd)
        if models:
            for model in models:
                self._check_or_create_model(model)
        if cmd['cmd'] == 'add_property':
            return self._add_property(cmd, params)
        if cmd['cmd'] == 'field_indexes':
            return self._field_indexes(cmd, params)
        if cmd['cmd'] == 'create_foreignkey_constraint':
            return self._create_foreignkey_constraint(cmd, params)
        if cmd['cmd'] == 'show_all_models':
            return self._show_all_models(cmd, params)
        if cmd['cmd'] == 'remove_property':
            return self._remove_property(cmd, params)
        if cmd['cmd'] == 'savepoint_create':
            return self._savepoint_create(cmd, params)
        if cmd['cmd'] == 'savepoint_rollback':
            return self._savepoint_rollback(cmd, params)
        if cmd['cmd'] == 'add_items':
            return self._add_items(cmd, params)
        if cmd['cmd'] == 'last_insert_id':
            return self._last_insert_id(cmd, params)
        if cmd['cmd'] == 'create_model':
            return self._create_model(cmd, params)
        if cmd['cmd'] == 'create_model':
            return self._create_model(cmd, params)
        if cmd['cmd'] == 'table_exists':
            return self._table_exists(cmd, params)
        if cmd['cmd'] == 'enable_constraints':
            return self._enable_constraints(cmd, params)
        if cmd['cmd'] == 'disable_constraints':
            return self._disable_constraints(cmd, params)
        if cmd['cmd'] == 'create_index':
            return self._create_index(cmd, params)
        if cmd['cmd'] == 'get_constraints':
            return self._get_constraints(cmd, params)

        raise WbDatabase.InternalError(
            f'Sorry, but that command {cmd} can\'t execute')

    def fetchall(self):
        """Fetch rows from the wikibase

        Returns:
            List[Tuple]: List of rows from the wikibase
        """
        return iter(())

    def fetchone(self):
        """Fetch single row from the wikibase

        Returns:
            Tuple: the row from the wikibase
        """
        return ()


class WbDatabaseConnection(Loggable):

    def __init__(self, charset: str, url: str,
                 user: str, password: str,
                 instance_of_property_id: int,
                 subclass_of_property_id: int,
                 django_model_item_id: int,
                 wdqs_sparql_endpoint: str,
                 django_namespace: str):
        super().__init__()
        self.charset = charset
        self.api = WbApi(url, charset)
        self.user = user
        self.password = password  # TODO: hash instead plain
        self.django_namespace = django_namespace

        if not django_model_item_id:
            # algo: 1. select django model by name 'django model'
            #       2. if not found create the item
            #       3. if found just get the identity
            django_model_item_id = self.create_item_if_not_found_by_name_and_get_id_without_prefix(
                WbDatabase._DJANGO_MODEL)
        django_namespace_property_id = self.create_property_if_not_found_by_name_and_get_id_without_prefix(
            WbDatabase._DJANGO_NAMESPACE, 'string')
        django_application_property_id = self.create_property_if_not_found_by_name_and_get_id_without_prefix(
            WbDatabase._DJANGO_APPLICATION, 'string')
        django_field_property_id = self.create_property_if_not_found_by_name_and_get_id_without_prefix(
            WbDatabase._DJANGO_FIELD, 'wikibase-property')

        mediawiki_info = self.api.mediawiki_info()
        wikibase_conceptbaseuri = mediawiki_info['query']['general']['wikibase-conceptbaseuri']
        # https://avangard.testo.click/api.php?action=query&meta=siteinfo&siprop=extensions&format=json
        self.wikibase_info = {
            WbDatabase._BASE_URL: wikibase_conceptbaseuri,
            WbDatabase._MEDIAWIKI_VERSION: mediawiki_info['query']['general']['generator'],
            WbDatabase._INSTANCE_OF: WbLink(instance_of_property_id, 'property', wikibase_conceptbaseuri),
            WbDatabase._SUBCLASS_OF: WbLink(subclass_of_property_id, 'property', wikibase_conceptbaseuri),
            WbDatabase._DJANGO_MODEL: WbLink(django_model_item_id, 'item', wikibase_conceptbaseuri),
            WbDatabase._DJANGO_NAMESPACE: WbLink(django_namespace_property_id, 'property', wikibase_conceptbaseuri),
            WbDatabase._DJANGO_APPLICATION: WbLink(django_application_property_id, 'property', wikibase_conceptbaseuri),
            WbDatabase._DJANGO_FIELD: WbLink(django_field_property_id, 'property', wikibase_conceptbaseuri),
            WbDatabase._SPARQL_ENDPOINT: wdqs_sparql_endpoint if wdqs_sparql_endpoint else f'{url}/sparql'
        }
        self.transactions = []

    def create_item_if_not_found_by_name_and_get_id_without_prefix(self, item_name: str) -> int:
        entities = self.api.search_items({'label': item_name})
        if len(entities) == 1:
            return int(entities[0]['id'][1:])
        if len(entities) == 0:
            entity = self.api.new_item(
                {'labels': {'en': {'language': 'en', 'value': item_name}}})
            return int(entity['id'][1:])
        # Exact matching
        for entity in entities:
            if entity['label'] == item_name:
                return int(entity['id'][1:])
        raise WbDatabase.InternalError(
            f'The entity {item_name} has another one (i.e. not unique)')

    def create_property_if_not_found_by_name_and_get_id_without_prefix(self, property_name: str, data_type_name: str):
        entities = self.api.search_properties({'label': property_name})
        if len(entities) == 1:
            return int(entities[0]['id'][1:])
        if len(entities) == 0:
            entity = self.api.new_property(
                {'labels': {'en': {'language': 'en', 'value': property_name}}, 'datatype': data_type_name})
            return int(entity['id'][1:])
        # Exact matching
        for entity in entities:
            if entity['label'] == property_name:
                return int(entity['id'][1:])
        raise WbDatabase.InternalError(
            f'The entity {property_name} has another one (i.e. not unique)')

    def db_info(self, key):
        return self.wikibase_info.get(key)

    def cursor(self):
        return WbCursor(self.django_namespace, self.wikibase_info, self.api)

    def rollback(self):
        ...

    def commit(self):
        ...

    def close(self):
        ...

    def trans(self) -> List:
        return self


class TransactionContext:

    def __init__(self, connection: WbDatabaseConnection):
        self.connection = connection

    def __enter__(self):
        # make a database connection and return it
        ...
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the dbconnection gets closed
        self.connection.close()
        ...
