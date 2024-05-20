# swagger_client.MovieApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_movie**](MovieApi.md#add_movie) | **POST** /movies | Добавить новый фильм
[**delete_movie_by_id**](MovieApi.md#delete_movie_by_id) | **DELETE** /movies/{movieId} | Удалить фильм по ID
[**get_movie_by_id**](MovieApi.md#get_movie_by_id) | **GET** /movies/{movieId} | Получить информацию о фильме по ID
[**get_movies_list**](MovieApi.md#get_movies_list) | **GET** /movies | Получить список всех фильмов
[**update_movie_by_id**](MovieApi.md#update_movie_by_id) | **PUT** /movies/{movieId} | Обновить информацию о фильме по ID

# **add_movie**
> add_movie(body)

Добавить новый фильм

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MovieApi()
body = swagger_client.Movie() # Movie | Новый фильм

try:
    # Добавить новый фильм
    api_instance.add_movie(body)
except ApiException as e:
    print("Exception when calling MovieApi->add_movie: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Movie**](Movie.md)| Новый фильм | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_movie_by_id**
> delete_movie_by_id(movie_id)

Удалить фильм по ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MovieApi()
movie_id = 789 # int | ID фильма

try:
    # Удалить фильм по ID
    api_instance.delete_movie_by_id(movie_id)
except ApiException as e:
    print("Exception when calling MovieApi->delete_movie_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**| ID фильма | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_movie_by_id**
> Movie get_movie_by_id(movie_id)

Получить информацию о фильме по ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MovieApi()
movie_id = 789 # int | ID фильма

try:
    # Получить информацию о фильме по ID
    api_response = api_instance.get_movie_by_id(movie_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MovieApi->get_movie_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**| ID фильма | 

### Return type

[**Movie**](Movie.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_movies_list**
> list[Movie] get_movies_list()

Получить список всех фильмов

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MovieApi()

try:
    # Получить список всех фильмов
    api_response = api_instance.get_movies_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MovieApi->get_movies_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Movie]**](Movie.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_movie_by_id**
> update_movie_by_id(body, movie_id)

Обновить информацию о фильме по ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MovieApi()
body = swagger_client.Movie() # Movie | Обновленная информация о фильме
movie_id = 789 # int | ID фильма

try:
    # Обновить информацию о фильме по ID
    api_instance.update_movie_by_id(body, movie_id)
except ApiException as e:
    print("Exception when calling MovieApi->update_movie_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Movie**](Movie.md)| Обновленная информация о фильме | 
 **movie_id** | **int**| ID фильма | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

