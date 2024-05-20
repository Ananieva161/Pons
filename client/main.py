from __future__ import print_function
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

try:
    # Добавить новый фильм
    api_instance.add_movie(body)
    gauge_movies_added.inc()
    logging.info('Added a new movie successfully')  # Записываем лог об успешном добавлении фильма
except ApiException as e:
    print("Exception when calling MovieApi->add_movie: %s\n" % e)
    logging.error(
        'Exception when calling MovieApi->add_movie: %s\n' % e)  # Записываем лог об ошибке при добавлении фильма

# create an instance of the API class
api_instance = swagger_client.MovieApi(swagger_client.ApiClient(configuration))
movie_id = 789 # int | ID фильма

try:
    # Удалить фильм по ID
    gauge_movies_deleted.inc()
    api_instance.delete_movie_by_id(movie_id)
    logging.info('Deleted movie with ID %d successfully' % movie_id)  # Записываем лог об успешном удалении фильма
except ApiException as e:
    print("Exception when calling MovieApi->delete_movie_by_id: %s\n" % e)
    logging.error(
        'Exception when calling MovieApi->delete_movie_by_id: %s\n' % e)  # Записываем лог об ошибке при удалении фильма
# create an instance of the API class
api_instance = swagger_client.MovieApi(swagger_client.ApiClient(configuration))
movie_id = 789 # int | ID фильма

try:
    # Получить информацию о фильме по ID
    api_response = api_instance.get_movie_by_id(movie_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MovieApi->get_movie_by_id: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.MovieApi(swagger_client.ApiClient(configuration))

try:
    # Получить список всех фильмов
    api_response = api_instance.get_movies_list()
    pprint(api_response)

except ApiException as e:
    print("Exception when calling MovieApi->get_movies_list: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.MovieApi(swagger_client.ApiClient(configuration))
body = swagger_client.Movie() # Movie | Обновленная информация о фильме
movie_id = 789 # int | ID фильма

try:
    # Обновить информацию о фильме по ID
    api_instance.update_movie_by_id(body, movie_id)
except ApiException as e:
    print("Exception when calling MovieApi->update_movie_by_id: %s\n" % e)

# push_to_gateway('http://localhost:9090', job='Movie_Api', registry=registry)
# Отправка метрик в VictoriaMetrics
# push_to_gateway('http://127.0.0.1:8428', job='movies', registry=registry)
# Отправляем метрики в vmagent
# push_to_gateway('http://localhost:8080', job='movies', registry=registry)

#
# from prometheus_client import start_http_server, Gauge, CollectorRegistry
# import time
# import swagger_client
# from swagger_client.rest import ApiException
# import requests
#
# # Создаем реестр коллекторов
# registry = CollectorRegistry()
# # Создаем метрику для добавленных фильмов
# gauge_movies_added = Gauge('movies_added_total', 'Total number of movies added', registry=registry)
# # Создаем метрику для удаленных фильмов
# gauge_movies_deleted = Gauge('movies_deleted_total', 'Total number of movies deleted', registry=registry)
#
# # Запускаем HTTP-сервер Prometheus для сбора метрик
# start_http_server(9090, registry=registry)
#
# # Функция для обновления значений метрик
# def update_metrics():
#     try:
#         # Добавляем новый фильм
#         api_instance.add_movie(body)
#         gauge_movies_added.inc()
#     except ApiException as e:
#         print("Exception when calling MovieApi->add_movie: %s\n" % e)
#
#     try:
#         # Удаляем фильм по ID
#         gauge_movies_deleted.inc()
#         api_instance.delete_movie_by_id(movie_id)
#     except ApiException as e:
#         print("Exception when calling MovieApi->delete_movie_by_id: %s\n" % e)

# # # Конфигурация сервера Swagger
# # configuration = swagger_client.Configuration(host='http://127.0.0.1:8080')
# # api_client = swagger_client.ApiClient(configuration=configuration)
# # api_instance = swagger_client.MovieApi(api_client=api_client)
# # body = swagger_client.Movie() # Movie | Новый фильм
# # movie_id = 789 # int | ID фильма
#
# # Вызываем функцию для обновления значений метрик
# update_metrics()
#
# # Функция для выполнения PromQL-запроса и вывода результата
# def execute_promql_query(query):
#     url = 'http://localhost:9090/api/v1/query'
#     params = {'query': query}
#     response = requests.get(url, params=params)
#     data = response.json()
#     print(data)
#
# # Выполняем PromQL-запросы
# execute_promql_query('movies_added_total')
# execute_promql_query('movies_deleted_total')
# execute_promql_query('movies_added_total - movies_deleted_total')
# execute_promql_query('sum(movies_added_total) by (label)')
# execute_promql_query('rate(movies_added_total[1h])')
# execute_promql_query('increase(movies_added_total[1h])')
# execute_promql_query('avg_over_time(movies_added_total[5m])')
# execute_promql_query('max_over_time(movies_deleted_total[1d])')
# execute_promql_query('sum(movies_added_total) + sum(movies_deleted_total)')
# execute_promql_query('100 * (increase(movies_added_total[1h]) / movies_added_total[1h] offset 1h)')

