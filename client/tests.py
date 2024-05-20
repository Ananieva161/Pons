import unittest
from swagger_client.rest import ApiException
# from __future__ import print_function
import logging
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
from prometheus_flask_exporter import PrometheusMetrics


# Настройка логгера
logging.basicConfig(filename='C:/Users/Мария/Desktop/сервер/var/log/123.log', level=logging.INFO)  # Указываем файл, куда записывать логи, и уровень логирования

registry = CollectorRegistry()
gauge_movies_added = Gauge('movies_added_total', 'Total number of movies added', registry=registry)
gauge_movies_deleted = Gauge('movies_deleted_total', 'Total number of movies deleted', registry=registry)


# create an instance of the API class
# api_instance = swagger_client.MovieApi(swagger_client.ApiClient(configuration))
configuration = swagger_client.Configuration()
configuration.host = 'http://127.0.0.1:8080/'
api_client = swagger_client.ApiClient(configuration=configuration)
api_instance = swagger_client.MovieApi(api_client=api_client)
body = swagger_client.Movie() # Movie | Новый фильм
class TestMovieApi(unittest.TestCase):
    def test_add_movie(self):
        try:
            api_instance.add_movie(body)
            self.assertTrue(True)
        except ApiException as e:
            self.fail("add_movie() raised ApiException unexpectedly: %s" % e)

    def test_delete_movie_by_id(self):
        try:
            api_instance.delete_movie_by_id(movie_id)
            self.assertTrue(True)
        except ApiException as e:
            self.fail("delete_movie_by_id() raised ApiException unexpectedly: %s" % e)

    def test_get_movie_by_id(self):
        try:
            api_response = api_instance.get_movie_by_id(movie_id)
            self.assertIsNotNone(api_response)
        except ApiException as e:
            self.fail("get_movie_by_id() raised ApiException unexpectedly: %s" % e)

    def test_get_movies_list(self):
        try:
            api_response = api_instance.get_movies_list()
            self.assertIsNotNone(api_response)
        except ApiException as e:
            self.fail("get_movies_list() raised ApiException unexpectedly: %s" % e)

    def test_update_movie_by_id(self):
        try:
            api_instance.update_movie_by_id(body, movie_id)
            self.assertTrue(True)
        except ApiException as e:
            self.fail("update_movie_by_id() raised ApiException unexpectedly: %s" % e)

if __name__ == '__main__':
    unittest.main()