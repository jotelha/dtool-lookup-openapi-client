# dtool-lookup-openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/jotelha/dtool-lookup-openapi-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/jotelha/dtool-lookup-openapi-client.git`)

Then import the package:
```python
import dtool-lookup-openapi-client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import dtool-lookup-openapi-client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import dtool-lookup-openapi-client
from pprint import pprint
from dtool_lookup_openapi_client import base_uri_api
from dtool-lookup-openapi-client.model.base_uri import BaseURI
from dtool-lookup-openapi-client.model.error import Error
from dtool-lookup-openapi-client.model.pagination_metadata import PaginationMetadata
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dtool-lookup-openapi-client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dtool-lookup-openapi-client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with dtool-lookup-openapi-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = base_uri_api.BaseUriApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 10 # int |  (optional) (default to 10)

    try:
        # List all base_uris.
        api_response = api_instance.admin_base_uri_list_get(page=page, page_size=page_size)
        pprint(api_response)
    except dtool-lookup-openapi-client.ApiException as e:
        print("Exception when calling BaseUriApi->admin_base_uri_list_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BaseUriApi* | [**admin_base_uri_list_get**](docs/BaseUriApi.md#admin_base_uri_list_get) | **GET** /admin/base_uri/list | List all base_uris.
*BaseUriApi* | [**admin_base_uri_register_post**](docs/BaseUriApi.md#admin_base_uri_register_post) | **POST** /admin/base_uri/register | Register a base URI.
*ConfigApi* | [**config_info_get**](docs/ConfigApi.md#config_info_get) | **GET** /config/info | Return the JSON-serialized server configuration.
*DatasetApi* | [**dataset_annotations_post**](docs/DatasetApi.md#dataset_annotations_post) | **POST** /dataset/annotations | Request the dataset annotations.
*DatasetApi* | [**dataset_list_get**](docs/DatasetApi.md#dataset_list_get) | **GET** /dataset/list | List the datasets a user has access to.
*DatasetApi* | [**dataset_lookup_uuid_get**](docs/DatasetApi.md#dataset_lookup_uuid_get) | **GET** /dataset/lookup/{uuid} | List all instances of a dataset in any base_uris the user has access to.
*DatasetApi* | [**dataset_manifest_post**](docs/DatasetApi.md#dataset_manifest_post) | **POST** /dataset/manifest | Request the dataset manifest.
*DatasetApi* | [**dataset_readme_post**](docs/DatasetApi.md#dataset_readme_post) | **POST** /dataset/readme | Request the dataset readme.
*DatasetApi* | [**dataset_register_post**](docs/DatasetApi.md#dataset_register_post) | **POST** /dataset/register | Register a dataset. The user needs to have register permissions on the base_uri.
*DatasetApi* | [**dataset_search_post**](docs/DatasetApi.md#dataset_search_post) | **POST** /dataset/search | List datasets the user has access to matching the query.
*DatasetApi* | [**dataset_summary_get**](docs/DatasetApi.md#dataset_summary_get) | **GET** /dataset/summary | Global summary of the datasets a user has access to.
*GraphApi* | [**graph_config_get**](docs/GraphApi.md#graph_config_get) | **GET** /graph/config | Return the JSON-serialized dependency graph plugin configuration.
*GraphApi* | [**graph_lookup_uuid_get**](docs/GraphApi.md#graph_lookup_uuid_get) | **GET** /graph/lookup/{uuid} | List the datasets within the same dependency graph as &lt;uuid&gt;. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.
*GraphApi* | [**graph_lookup_uuid_post**](docs/GraphApi.md#graph_lookup_uuid_post) | **POST** /graph/lookup/{uuid} | List the datasets within the same dependency graph as &lt;uuid&gt;. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.
*MongoApi* | [**mongo_aggregate_post**](docs/MongoApi.md#mongo_aggregate_post) | **POST** /mongo/aggregate | Aggregate the datasets a user has access to.
*MongoApi* | [**mongo_config_get**](docs/MongoApi.md#mongo_config_get) | **GET** /mongo/config | Return the JSON-serialized plugin configuration.
*MongoApi* | [**mongo_query_post**](docs/MongoApi.md#mongo_query_post) | **POST** /mongo/query | Query datasets a user has access to.
*PermissionsApi* | [**admin_permission_info_post**](docs/PermissionsApi.md#admin_permission_info_post) | **POST** /admin/permission/info | Get information about the permissions on a base URI.
*PermissionsApi* | [**admin_permission_update_on_base_uri_post**](docs/PermissionsApi.md#admin_permission_update_on_base_uri_post) | **POST** /admin/permission/update_on_base_uri | Update the permissions on a base URI.
*ScaffoldingApi* | [**scaffolding_config_get**](docs/ScaffoldingApi.md#scaffolding_config_get) | **GET** /scaffolding/config | Return the JSON-serialized plugin configuration.
*UserApi* | [**user_info_username_get**](docs/UserApi.md#user_info_username_get) | **GET** /user/info/{username} | Return a user&#39;s information.
*UserAdminApi* | [**admin_user_list_get**](docs/UserAdminApi.md#admin_user_list_get) | **GET** /admin/user/list | List the users in the dtool lookup server.
*UserAdminApi* | [**admin_user_register_post**](docs/UserAdminApi.md#admin_user_register_post) | **POST** /admin/user/register | Register a user in the dtool lookup server.
*WebhookApi* | [**webhook_config_get**](docs/WebhookApi.md#webhook_config_get) | **GET** /webhook/config | Return the JSON-serialized plugin configuration.
*WebhookApi* | [**webhook_notify_path_post**](docs/WebhookApi.md#webhook_notify_path_post) | **POST** /webhook/notify/{path} | Notify the lookup server about creation, modification or deletion of a dataset.
*WebhookApi* | [**webhook_notify_post**](docs/WebhookApi.md#webhook_notify_post) | **POST** /webhook/notify | Notify the lookup server about creation, modification or deletion of a dataset.


## Documentation For Models

 - [BaseURI](docs/BaseURI.md)
 - [BaseUri](docs/BaseUri.md)
 - [Dataset](docs/Dataset.md)
 - [DependencyKeys](docs/DependencyKeys.md)
 - [Error](docs/Error.md)
 - [Item](docs/Item.md)
 - [Manifest](docs/Manifest.md)
 - [PaginationMetadata](docs/PaginationMetadata.md)
 - [RegisterDataset](docs/RegisterDataset.md)
 - [RegisterUser](docs/RegisterUser.md)
 - [SearchDataset](docs/SearchDataset.md)
 - [Summary](docs/Summary.md)
 - [Uri](docs/Uri.md)
 - [UriPermission](docs/UriPermission.md)
 - [User](docs/User.md)
 - [UserResponse](docs/UserResponse.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication (JWT)


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in dtool-lookup-openapi-client.apis and dtool-lookup-openapi-client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from dtool-lookup-openapi-client.api.default_api import DefaultApi`
- `from dtool-lookup-openapi-client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import dtool-lookup-openapi-client
from dtool-lookup-openapi-client.apis import *
from dtool-lookup-openapi-client.models import *
```

