# coding: utf-8

"""
    Movies API

    API для работы с фильмотекой  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.movie_api import MovieApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMovieApi(unittest.TestCase):
    """MovieApi unit test stubs"""

    def setUp(self):
        self.api = MovieApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_movie(self):
        """Test case for add_movie

        Добавить новый фильм  # noqa: E501
        """
        pass

    def test_delete_movie_by_id(self):
        """Test case for delete_movie_by_id

        Удалить фильм по ID  # noqa: E501
        """
        pass

    def test_get_movie_by_id(self):
        """Test case for get_movie_by_id

        Получить информацию о фильме по ID  # noqa: E501
        """
        pass

    def test_get_movies_list(self):
        """Test case for get_movies_list

        Получить список всех фильмов  # noqa: E501
        """
        pass

    def test_update_movie_by_id(self):
        """Test case for update_movie_by_id

        Обновить информацию о фильме по ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
