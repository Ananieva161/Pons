# # coding: utf-8

# from __future__ import absolute_import

# from flask import json
# from six import BytesIO

# from swagger_server.models.movie import Movie  # noqa: E501
# from swagger_server.test import BaseTestCase


# class TestMovieController(BaseTestCase):
#     """MovieController integration test stubs"""

#     def test_add_movie(self):
#         """Test case for add_movie

#         Добавить новый фильм
#         """
#         body = Movie()
#         response = self.client.open(
#             '/movies',
#             method='POST',
#             data=json.dumps(body),
#             content_type='application/json')
#         self.assert200(response,
#                        'Response body is : ' + response.data.decode('utf-8'))

#     def test_delete_movie_by_id(self):
#         """Test case for delete_movie_by_id

#         Удалить фильм по ID
#         """
#         response = self.client.open(
#             '/movies/{movie_id}'.format(movie_id=789),
#             method='DELETE')
#         self.assert200(response,
#                        'Response body is : ' + response.data.decode('utf-8'))

#     def test_get_movie_by_id(self):
#         """Test case for get_movie_by_id

#         Получить информацию о фильме по ID
#         """
#         response = self.client.open(
#             '/movies/{movie_id}'.format(movie_id=789),
#             method='GET')
#         self.assert200(response,
#                        'Response body is : ' + response.data.decode('utf-8'))

#     def test_get_movies_list(self):
#         """Test case for get_movies_list

#         Получить список всех фильмов
#         """
#         response = self.client.open(
#             '/movies',
#             method='GET')
#         self.assert200(response,
#                        'Response body is : ' + response.data.decode('utf-8'))

#     def test_update_movie_by_id(self):
#         """Test case for update_movie_by_id

#         Обновить информацию о фильме по ID
#         """
#         body = Movie()
#         response = self.client.open(
#             '/movies/{movie_id}'.format(movie_id=789),
#             method='PUT',
#             data=json.dumps(body),
#             content_type='application/json')
#         self.assert200(response,
#                        'Response body is : ' + response.data.decode('utf-8'))


# if __name__ == '__main__':
#     import unittest
#     unittest.main()

import logging
from flask import json
from six import BytesIO
from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server.test import BaseTestCase
from unittest.mock import patch

logging.basicConfig(level=logging.DEBUG)

def add_movie(body):
    try:
        if connexion.request.is_json:
            movie = Movie.from_dict(connexion.request.get_json())
            # Логика для сохранения нового фильма
            logging.info("New movie added: %s", movie.title)
            return None, 201
    except Exception as e:
        logging.error("Error adding movie: %s", e)
        return {"error": "Internal server error"}, 500

def delete_movie_by_id(movie_id):
    try:
        # Логика для удаления фильма по ID
        logging.info("Deleted movie with ID: %s", movie_id)
        return None, 200
    except Exception as e:
        logging.error("Error deleting movie: %s", e)
        return {"error": "Internal server error"}, 500

def get_movie_by_id(movie_id):
    try:
        # Логика для получения фильма по ID
        movie = Movie(id=movie_id, title="Example Movie")
        logging.info("Retrieved movie with ID: %s", movie_id)
        return movie
    except Exception as e:
        logging.error("Error getting movie by ID: %s", e)
        return {"error": "Internal server error"}, 500

def get_movies_list():
    try:
        # Логика для получения списка всех фильмов
        movies = [Movie(id=1, title="Movie 1"), Movie(id=2, title="Movie 2")]
        logging.info("Retrieved list of movies")
        return movies
    except Exception as e:
        logging.error("Error getting list of movies: %s", e)
        return {"error": "Internal server error"}, 500

def update_movie_by_id(movie_id, body):
    try:
        # Логика для обновления фильма по ID
        logging.info("Updated movie with ID: %s", movie_id)
        return None, 200
    except Exception as e:
        logging.error("Error updating movie: %s", e)
        return {"error": "Internal server error"}, 500

class TestMovieController(BaseTestCase):
    """MovieController integration test stubs"""

    def test_add_movie(self):
        """Test case for add_movie"""
        body = Movie()
        response = self.client.open(
            '/movies',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_movie_by_id(self):
        """Test case for delete_movie_by_id"""
        response = self.client.open(
            '/movies/{movie_id}'.format(movie_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_movie_by_id(self):
        """Test case for get_movie_by_id"""
        response = self.client.open(
            '/movies/{movie_id}'.format(movie_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_movies_list(self):
        """Test case for get_movies_list"""
        response = self.client.open(
            '/movies',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_movie_by_id(self):
        """Test case for update_movie_by_id"""
        body = Movie()
        response = self.client.open(
            '/movies/{movie_id}'.format(movie_id=789),

            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @patch('swagger_server.controllers.movie_controller.Movie')
    def test_get_movie_by_id_mock(self, mock_movie):
        mock_movie.return_value = Movie(id=1, title="Example Movie")
        response = get_movie_by_id(1)
        self.assertIsInstance(response, Movie)
        self.assertEqual(response.id, 1)
        self.assertEqual(response.title, "Example Movie")

    @patch('swagger_server.controllers.movie_controller.Movie')
    def test_add_movie_mock(self, mock_movie):
        mock_movie.from_dict.return_value = Movie(id=1, title="New Movie")
        response, status = add_movie({"title": "New Movie"})
        self.assertIsNone(response)
        self.assertEqual(status, 201)

if __name__ == '__main__':
    import unittest
    unittest.main()

