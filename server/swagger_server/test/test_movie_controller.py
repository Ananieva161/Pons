# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMovieController(BaseTestCase):
    """MovieController integration test stubs"""

    def test_add_movie(self):
        """Test case for add_movie

        Добавить новый фильм
        """
        body = Movie()
        response = self.client.open(
            '/movies',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_movie_by_id(self):
        """Test case for delete_movie_by_id

        Удалить фильм по ID
        """
        response = self.client.open(
            '/movies/{movie_id}'.format(movie_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_movie_by_id(self):
        """Test case for get_movie_by_id

        Получить информацию о фильме по ID
        """
        response = self.client.open(
            '/movies/{movie_id}'.format(movie_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_movies_list(self):
        """Test case for get_movies_list

        Получить список всех фильмов
        """
        response = self.client.open(
            '/movies',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_movie_by_id(self):
        """Test case for update_movie_by_id

        Обновить информацию о фильме по ID
        """
        body = Movie()
        response = self.client.open(
            '/movies/{movie_id}'.format(movie_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
