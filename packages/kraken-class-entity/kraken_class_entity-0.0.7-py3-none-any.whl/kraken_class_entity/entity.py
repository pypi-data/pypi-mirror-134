from dateutil import parser
import datetime
import uuid
import json
import kraken_schema_org as norm 
import kraken_datatype as dt
import os
import requests
import aiohttp
import asyncio

class Entity:
    def __init__(self, record = {}):
        
        if record:
            self.load(record)
        self._date_created = datetime.datetime.now()

    def __str__(self):
        return json.dumps(self.dump(), indent = 4, default = str)


    def __repr__(self):
        self.dump()


    def __eq__(self, other):
        if self.record_type == other.record_type:
            if self.record_id == other.record_id:
                return True

        return False


    def __add__(self, other):
        if self.record_type != other.record_type:
            return False
        if self.record_id != other.record_id:
            return False
        

        new_entity = Entity()
        new_entity.record_type = self.record_type
        new_entity.record_Id = self.record_id

        for k in self.keys:
            value_self = self.get(k)
            if not isinstance(value_self, list):
                value_self = [value_self]

            value_other = other.get(k)
            if not isinstance(value_other, list):
                value_other = [value_other]

            new_values = list(set(value_self + value_other))

            if len(new_values) == 0:
                new_entity.set(k, None)
            elif len(new_values) == 1:
                new_entity.set(k, new_values[0])
            else:
                new_entity.set(k, new_values)

        return True

    """
    Helper attributes
    """

    
    @property 
    def ref_id(self):
        record = {}
        record['@type'] = self.record_type
        record['@id'] = self.record_id
        return record

    @property
    def record_type(self):
        return self.get('@type')
    
    @record_type.setter
    def record_type(self, value):
        norm_type = norm.normalize_type(value)
        if norm_type:
            return self.set('@type', norm_type)
        else:
            return self.set('@type', value)
    
    @property
    def record_id(self):
        return self.get('@id')
    
    @record_id.setter
    def record_id(self, value):
        return self.set('@id', value)

    @property
    def record(self):
        return self.dump()

    @record.setter
    def record(self, value):
        self.load(value)
        return

    @property
    def json(self):
        return json.dumps(self.dump(), indent = 4, default = str)
    
    @json.setter
    def json(self, value):
        record = json.loads(value)
        self.load(record)
        return


    """
    Schema attributes
    """

    @property 
    def url(self):
        return self.get('schema:url')
    @url.setter
    def url(self, value):
        return self.set('schema:url', value)

    @property 
    def name(self):
        return self.get('schema:name')
    @name.setter
    def name(self, value):
        return self.set('schema:name', value)

    @property 
    def object(self):
        return self.get('schema:object')
    @object.setter
    def object(self, value):
        return self.set('schema:object', value)

    @property 
    def agent(self):
        return self.get('schema:agent')
    @agent.setter
    def agent(self, value):
        return self.set('schema:agent', value)


    

    """
    APIs
    """


    def get(self, key):

        # Normalize key
        norm_key = self._normalize_key(key)

        value = getattr(self, norm_key, None)
        #value = self._record.get(norm_key, None)

        return value


    def set(self, key, value):

        if value and 'Time' in key:
            try:
                value = parser.parse(value)
            except:
                a=1

        # Normalize key
        norm_key = self._normalize_key(key)

        norm_value = self._normalize_value(norm_key, value)
        setattr(self, norm_key, norm_value)

        return


    def load(self, record):

        if isinstance(record, list) and len(record) == 1:
            record = record[0]

        if not record:
            return

        if not isinstance(record, dict):
            return None
            
        for k in record.keys():
            value = record.get(k, None)
            self.set(k, value)
        
        self._normalize_type()
        self._normalize_id()

        return True

    def dump(self):
        record = {}
        keys = [i for i in self.__dict__.keys() if i[:1] != '_']

        for k in keys:
            value = self.get(k)
            if type(value) is Entity:
                value = value.record
            record[k] = value
        return record

    """
    API methods
    """

    @property
    def api_url(self):
        return os.getenv('API_URL')

    @api_url.setter
    def api_url(self, value):
        """set environment variable for api call
        """ 
        os.environ['API_URL'] = value


    def get_api(self):
        
        headers = {
            'Content-Type': 'application/json'
        }
        r = requests.get(self.api_url, headers = headers, params = self.ref_id)

        try:
            record = r.json()
            if len(record) == 1:
                self.load(record[0])

        except:
            print('error')
            return

        return

    def post_api(self):
        
        headers = {
            'Content-Type': 'application/json'
        }
        try:
            r = requests.post(self.api_url, headers = headers, data = self.json)
        except Exception as e:
            print('error', e)

        
        return
    
    async def get_api_async(self):
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url, headers=headers, params = self.ref_id) as resp:
                try:
                    record = await resp.json()
                except Exception as e:
                    print('error', e)
                    return

        self.load(record)
        return

    async def post_api_async(self):
        
        headers = {
            'Content-Type': 'application/json'
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.api_url, headers=headers, data = self.json) as resp:
                await resp.text()
        
        return





    """
    Methods data norm
    """

    def _normalize_type(self):
        
        norm_type = norm.normalize_type(self.get('@type'))
        
        if norm_type:
            self.set('@type', norm_type)
        return

    def _normalize_id(self):

        record_type = self.get('@type')

        if not record_type:
            return

        norm_record_type = record_type.lower().replace('schema:', '')

        if norm_record_type in ['webpage', 'website', 'datafeed']:
            url = self.get('url')
            if url:
                hash_url = str(uuid.uuid3(uuid.NAMESPACE_URL, url))
                self.set('@id', hash_url)

        elif norm_record_type in ['imageobject', 'videoobject']:
            url = self.get('contenturl')
            if url:
                hash_url = str(uuid.uuid3(uuid.NAMESPACE_URL, url))
                self.set('@id', hash_url)
        else:
            a=1

        return 


    def _normalize_key(self, key):
        
        norm_key = norm.normalize_key(key)
        if norm_key:
            return norm_key
        else:
            return key


    def _normalize_value(self, key, value):
        
        if key in ['@type', '@id']:
            return value

        if not key or not value:
            return value

        if isinstance(value, Entity):
            return value


        # if value is list:
        if isinstance(value, list) and not isinstance(value, str):
            new_value = []
            for i in value:
                new_value.append(self._normalize_value(key, i))
            return new_value

        # if value is dict:
        if isinstance(value, dict):
            new_value = {}
            for k in value:
                norm_k = self._normalize_key(k)
                new_value[norm_k] = self._normalize_value(norm_k, value[k])
            # if entity
            if '@type' in new_value.keys():
                new_entity = Entity()
                new_entity.record =  new_value
                return new_entity
            else:
                return new_value

        # if value is neither dict or list

        datatypes = norm.get_datatype(self.record_type, key)

        if not datatypes:
            return value

        for i in datatypes:
            try:
                k = i.lower().replace('schema:', '')
                n_value = dt.normalize(k, value)
                if n_value:
                    return n_value
            except Exception as e:
                a=1
                #print('error', i, e)
        return value
