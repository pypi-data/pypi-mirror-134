# <img src="https://uploads-ssl.webflow.com/5ea5d3315186cf5ec60c3ee4/5edf1c94ce4c859f2b188094_logo.svg" alt="Pip.Services Logo" width="200"> <br/> MySQL components for Python Changelog

## <a name="3.2.7"></a> 3.2.7 (2022-01-10)

### Bug fixes

* Fixed repeats of return value for get_one_random

## <a name="3.2.6"></a> 3.2.6 (2021-12-02)

### Bug fixes
* fixed update operation if item does not exist


## <a name="3.2.5"></a> 3.2.5 (2021-11-28)

### Bug fixes
* **persistence** fixed conversion for get_list_by_ids

## <a name="3.2.4"></a> 3.2.4 (2021-11-25)

### Bug fixes
* Fixed get_one_random method
* Fixed get_list_by_filter method

## <a name="3.2.2-3.2.3"></a> 3.2.2-3.2.3 (2021-11-22)

### Bug fixes
* Updated requirements
* Optimize imports
* Fixed connection timeout

## <a name="3.2.1"></a> 3.2.1 (2021-08-25)

### Featuresquit
* Added _request method for PostgresPersistence

## <a name="3.2.0"></a> 3.2.0 (2021-08-09)

Added support for database schemas
t push
### Features
* Added schemas to MySqlPersistence, IdentifiableMySqlPersistence, IdentifiableJsonMySqlPersistence
* Added _auto_generate_id flag to IdentifiableMySqlPersistence

### Bug fixes
* Fixed MySQLConnection open error logging

## <a name="3.1.0"></a> 3.1.0 (2021-05-14)

### Features
* Moved MySQLConnection to **connect** package
* Added type hints
* Fixed returned types for operations

## <a name="3.0.1"></a> 3.0.1 (2021-03-11)

### Bug fixes
* fixed MySqlPersistence.get_page_by_filter sort param
* fixed MySqlPersistence.get_list_by_filter return value

## <a name="3.0.0"></a> 3.0.0 (2021-02-25) 

Initial public release

### Features
* Added DefaultMySqlFactory
* Added MySqlConnectionResolver
* Added IdentifiableJsonMySqlPersistence
* Added IdentifiableMySqlPersistence
* Added MySqlConnection
* Added MySqlPersistence