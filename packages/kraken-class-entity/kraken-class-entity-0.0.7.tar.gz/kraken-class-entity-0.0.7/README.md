# Entity class api

Generic class library to interact with kraken db through api. 

The library handles type and key conversion to ensure compliance. 

## Features
- Automatic schema type correction (imageobject --> schema:ImageObject)
- Automatic record_id assignation if missing
- Automatic variable name (key) correction (familyname --> schema:familyName)
- Automatic value type correction (www.test.com --> https://www.test.com/) 



## How to use:
- entity: single entity record
- entities: collection of entity records

## Entity
### Initialize
`entity = Entity()`

`entity.record_type = 'schema:Person'`

`entity.record_id = 'abc'`

### Get/store data
`name = entity.get('givenName')`

`entity.set('givenName', name)`

### Get/store record / json
`entity.record = record`

`record = entity.record`

`entity.json = json_string`

`json_string = entity.json`

### Get and store data to database
Set once for all subsequent entities

`entity.api_url = 'url_to_use'`

#### Get from db

`entity.get_api()`

`entity.get_api_async()`


#### Post to db

`entity.post_api()`

`entity.post_api_async()`


## Entities
### Initialize
`entities = Entities()`

`entities.record_type = 'schema:Person'`

`entities.record_id = 'abc'`

### Load / dump data
Will convert records to entity

`records = entity.dump()`

`entity.load(records)`

### Attributes
- entity.ref_id: dict reference to record ({'@type': 'record_type', '@id': 'record_id'})

### Get/store record / json
`entities.record = record`

`record = entities.record`

`entities.json = json_string`

`json_string = entities.json`

### Get and store data to database
Set once for all subsequent entities

`entities.api_url = 'url_to_use'`

#### Get from db

`entities.get_api()`

`entities.get_api_async()`


#### Post to db

`entities.post_api()`

`entities.post_api_async()`