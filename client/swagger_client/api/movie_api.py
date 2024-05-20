# coding: utf-8

"""
    Movies API

    API для работы с фильмотекой  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class MovieApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_movie(self, body, **kwargs):  # noqa: E501
        """Добавить новый фильм  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_movie(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Movie body: Новый фильм (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_movie_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_movie_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_movie_with_http_info(self, body, **kwargs):  # noqa: E501
        """Добавить новый фильм  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_movie_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Movie body: Новый фильм (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_movie" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_movie`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/movies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_movie_by_id(self, movie_id, **kwargs):  # noqa: E501
        """Удалить фильм по ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_movie_by_id(movie_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int movie_id: ID фильма (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_movie_by_id_with_http_info(movie_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_movie_by_id_with_http_info(movie_id, **kwargs)  # noqa: E501
            return data

    def delete_movie_by_id_with_http_info(self, movie_id, **kwargs):  # noqa: E501
        """Удалить фильм по ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_movie_by_id_with_http_info(movie_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int movie_id: ID фильма (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['movie_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_movie_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'movie_id' is set
        if ('movie_id' not in params or
                params['movie_id'] is None):
            raise ValueError("Missing the required parameter `movie_id` when calling `delete_movie_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'movie_id' in params:
            path_params['movieId'] = params['movie_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/movies/{movieId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_movie_by_id(self, movie_id, **kwargs):  # noqa: E501
        """Получить информацию о фильме по ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_movie_by_id(movie_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int movie_id: ID фильма (required)
        :return: Movie
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_movie_by_id_with_http_info(movie_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_movie_by_id_with_http_info(movie_id, **kwargs)  # noqa: E501
            return data

    def get_movie_by_id_with_http_info(self, movie_id, **kwargs):  # noqa: E501
        """Получить информацию о фильме по ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_movie_by_id_with_http_info(movie_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int movie_id: ID фильма (required)
        :return: Movie
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['movie_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_movie_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'movie_id' is set
        if ('movie_id' not in params or
                params['movie_id'] is None):
            raise ValueError("Missing the required parameter `movie_id` when calling `get_movie_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'movie_id' in params:
            path_params['movieId'] = params['movie_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/movies/{movieId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Movie',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_movies_list(self, **kwargs):  # noqa: E501
        """Получить список всех фильмов  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_movies_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Movie]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_movies_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_movies_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_movies_list_with_http_info(self, **kwargs):  # noqa: E501
        """Получить список всех фильмов  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_movies_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Movie]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_movies_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/movies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Movie]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_movie_by_id(self, body, movie_id, **kwargs):  # noqa: E501
        """Обновить информацию о фильме по ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_movie_by_id(body, movie_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Movie body: Обновленная информация о фильме (required)
        :param int movie_id: ID фильма (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_movie_by_id_with_http_info(body, movie_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_movie_by_id_with_http_info(body, movie_id, **kwargs)  # noqa: E501
            return data

    def update_movie_by_id_with_http_info(self, body, movie_id, **kwargs):  # noqa: E501
        """Обновить информацию о фильме по ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_movie_by_id_with_http_info(body, movie_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Movie body: Обновленная информация о фильме (required)
        :param int movie_id: ID фильма (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'movie_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_movie_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_movie_by_id`")  # noqa: E501
        # verify the required parameter 'movie_id' is set
        if ('movie_id' not in params or
                params['movie_id'] is None):
            raise ValueError("Missing the required parameter `movie_id` when calling `update_movie_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'movie_id' in params:
            path_params['movieId'] = params['movie_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/movies/{movieId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
