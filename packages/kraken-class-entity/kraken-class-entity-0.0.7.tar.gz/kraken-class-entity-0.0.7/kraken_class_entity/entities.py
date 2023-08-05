
from kraken_class_entity.entity import Entity
import json
import os
import requests
import aiohttp
import asyncio



class Entities:


    def __init__(self):

        self.entities = []
        a=1


    def __add__(self, other):
    
        e = Entities()

        e.entities = self.entities + other.entities
        
        return e 

    def __contains__(self, other):

        for i in self.entities:
            if i == other:
                return True
        return False


    """
    Attr
    """

    @property
    def ref_ids(self):
        records = []
        for i in self.entities:
            records.append(i.ref_id)
        return records

    @property
    def records(self):
        return self.dump()
    @records.setter
    def records(self, value):
        return self.load(value)

    @property
    def json(self):
        records = json.dumps(self.dump(), default = str)
        return records
    @json.setter
    def json(self, value):
        records = json.loads(value)
        self.load(records)
        return



    """
    Methods
    """

    def load(self, records):
        for i in records:
            entity = Entity()
            entity.load(i)
            self.entities.append(entity)

    def dump(self):
        records = []
        for i in self.entities:
            records.append(i.record)
        return records

    """
    Methods api
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
            records = r.json()
            self.load(records)

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
    
    def search_api(self, search_terms = None, limit = 20, offset = 0, order_by = None, order_direction = None):

        params = {}
        params['limit'] = limit
        params['offset'] = offset
        params['order_by'] = order_by
        params['order_direction'] = order_direction

        for i in search_terms:
            params[i] = search_terms[i]

        headers = {
            'Content-Type': 'application/json'
        }
        r = requests.get(self.api_url + '/search', headers = headers, params = params)

        try:
            records = r.json()
            self.load(records)

        except:
            print('error')
            return

        return


    async def get_api_async(self):
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url, headers=headers, params = self.ref_id) as resp:
                try:
                    records = await resp.json()
                except Exception as e:
                    print('error', e)
                    return

        self.load(records)
        return

    async def post_api_async(self):
        
        headers = {
            'Content-Type': 'application/json'
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.api_url, headers=headers, data = self.json) as resp:
                await resp.text()
        
        return




    