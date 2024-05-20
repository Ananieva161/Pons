from prometheus_client import start_http_server, Gauge, CollectorRegistry
import time
import swagger_client
from swagger_client.rest import ApiException
import requests

# Создаем реестр коллекторов
registry = CollectorRegistry()
# Создаем метрику для добавленных фильмов
gauge_movies_added = Gauge('movies_added_total', 'Total number of movies added', registry=registry)
# Создаем метрику для удаленных фильмов
gauge_movies_deleted = Gauge('movies_deleted_total', 'Total number of movies deleted', registry=registry)

# Запускаем HTTP-сервер Prometheus для сбора метрик
start_http_server(9090, registry=registry)

# Функция для обновления значений метрик
def update_metrics():
    try:
        # Добавляем новый фильм
        api_instance.add_movie(body)
        gauge_movies_added.inc()
    except ApiException as e:
        print("Exception when calling MovieApi->add_movie: %s\n" % e)

    try:
        # Удаляем фильм по ID
        gauge_movies_deleted.inc()
        api_instance.delete_movie_by_id(movie_id)
    except ApiException as e:
        print("Exception when calling MovieApi->delete_movie_by_id: %s\n" % e)

# Конфигурация сервера Swagger
configuration = swagger_client.Configuration(host='http://localhost:8080')
api_client = swagger_client.ApiClient(configuration=configuration)
api_instance = swagger_client.MovieApi(api_client=api_client)
body = swagger_client.Movie() # Movie | Новый фильм
movie_id = 789 # int | ID фильма

# Вызываем функцию для обновления значений метрик
update_metrics()

# Функция для выполнения PromQL-запроса и вывода результата
def execute_promql_query(query):
    url = 'http://localhost:9090/api/v1/query'
    params = {'query': query}
    response = requests.get(url, params=params)
    data = response.json()
    print(data)

# Выполняем PromQL-запросы
execute_promql_query('movies_added_total')
execute_promql_query('movies_deleted_total')
execute_promql_query('movies_added_total - movies_deleted_total')
execute_promql_query('sum(movies_added_total) by (label)')
execute_promql_query('rate(movies_added_total[1h])')
execute_promql_query('increase(movies_added_total[1h])')
execute_promql_query('avg_over_time(movies_added_total[5m])')
execute_promql_query('max_over_time(movies_deleted_total[1d])')
execute_promql_query('sum(movies_added_total) + sum(movies_deleted_total)')
execute_promql_query('100 * (increase(movies_added_total[1h]) / movies_added_total[1h] offset 1h)')



# from swagger_client import MovieApi, Movie
#
# def main():
#     # Создание экземпляра клиента API
#     client = MovieApi()
#
#     # Получение списка всех фильмов
#     movies = client.get_movies_list()
#
#     # Вывод списка всех фильмов на экран
#     if movies is not None:
#         for movie in movies:
#             print(f"ID: {movie.id}")
#             print(f"Название: {movie.title}")
#             print(f"Описание: {movie.description}")
#             print("-------------")
#     else:
#         print("Ошибка при получении списка фильмов")
#
#     # Добавление новых русских фильмов
#     new_movies = [
#         Movie(id="11", title="Матильда", description="Драма о любви и страсти"),
#         Movie(id="12", title="Левиафан", description="Драма о судьбе человека, сражающегося с бюрократией"),
#         Movie(id="13", title="Брат", description="Драматический фильм о жизни бандитов 90-х годов"),
#         Movie(id="14", title="Стиляги", description="Музыкальная комедия о стилягах 50-х годов"),
#         Movie(id="15", title="Бандитский Петербург", description="Криминальная драма о мире преступности в Санкт-Петербурге"),
#         Movie(id="16", title="Ирония судьбы, или С легким паром!", description="Комедия о путанице, связанной с путешествиями"),
#         Movie(id="17", title="Экипаж", description="Драма о героях воздушного флота"),
#         Movie(id="18", title="Карнавальная ночь", description="Музыкальная комедия о приключениях в Новый год"),
#         Movie(id="19", title="Москва слезам не верит", description="Драма о любви и жизни в Москве"),
#         Movie(id="20", title="Совершенно серьезно", description="Комедия о молодежной жизни")
#     ]
#
#     for movie in new_movies:
#         added_movie = client.add_movie(movie)
#         if added_movie is not None:
#             print("Новый фильм успешно добавлен")
#             print(f"ID: {added_movie.id}")
#             print(f"Название: {added_movie.title}")
#             print(f"Описание: {added_movie.description}")
#         else:
#             print("Ошибка при добавлении нового фильма")
#
# if __name__ == "main":
#     main()

# from prometheus_client import CollectorRegistry, Summary, Counter, push_to_gateway, generate_latest
# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
# # Создаем инстанс коллекторного регистра, на котором будут храниться метрики
# registry = CollectorRegistry()
#
# # Создаем счетчики для метрик
# requests_counter = Counter('http_requests_total', 'Total number of HTTP requests', ['method'], registry=registry)
# request_time = Summary('http_request_duration_seconds', 'HTTP Request duration in seconds', registry=registry)
#
# # Route для получения списка всех фильмов
# @app.route('/movies', methods=['GET'])
# @request_time.time()
# def get_movies():
#     requests_counter.labels(method='GET').inc()
#     # Ваш код для получения списка всех фильмов
#     movies = [
#         {'id': '1', 'title': 'Брат', 'description': 'Драматический фильм о бандитском мире 90-х годов в России'},
#         {'id': '2', 'title': 'Москва слезам не верит', 'description': 'Романтическая комедия о любви в Москве'},
#         {'id': '3', 'title': 'Левиафан', 'description': 'Драма о судьбе человека, сражающегося с коррупцией в России'}
#     ]
#     return jsonify(movies)
#
# # Route для добавления нового фильма
# @app.route('/movies', methods=['POST'])
# @request_time.time()
# def add_movie():
#     requests_counter.labels(method='POST').inc()
#     # Ваш код для добавления нового фильма
#     return jsonify({'message': 'Фильм успешно добавлен'}), 201
#
# # Route для получения информации о фильме по ID
# @app.route('/movies/<int:movie_id>', methods=['GET'])
# @request_time.time()
# def get_movie_by_id(movie_id):
#     requests_counter.labels(method='GET').inc()
#     # Ваш код для получения информации о фильме по ID
#     movie = {'id': str(movie_id), 'title': 'Фильм', 'description': 'Описание фильма'}
#     return jsonify(movie)
#
# # Route для обновления информации о фильме по ID
# @app.route('/movies/<int:movie_id>', methods=['PUT'])
# @request_time.time()
# def update_movie_by_id(movie_id):
#     requests_counter.labels(method='PUT').inc()
#     # Ваш код для обновления информации о фильме по ID
#     return jsonify({'message': 'Информация о фильме успешно обновлена'})
#
# # Route для удаления фильма по ID
# @app.route('/movies/<int:movie_id>', methods=['DELETE'])
# @request_time.time()
# def delete_movie_by_id(movie_id):
#     requests_counter.labels(method='DELETE').inc()
#     # Ваш код для удаления фильма по ID
#     return jsonify({'message': 'Фильм успешно удален'}), 204
#
# # Route для сбора метрик Prometheus
# @app.route('/metrics', methods=['GET'])
# def get_metrics():
#     return generate_latest(registry), 200, {'Content-Type': 'text/plain'}
#
# if __name__ == 'main':
#     # Запуск приложения Flask
#     app.run()
#
# # Отправка метрик в VictoriaMetrics после остановки приложения
# @app.teardown_appcontext
# def push_metrics(response):
#     push_to_gateway('victoriametrics.example.com:9091', job='movies-api', registry=registry)
#     return response



# from prometheus_client import start_http_server, Counter, Summary, generate_latest, push_to_gateway, CollectorRegistry
# from flask import Flask, jsonify, request
#
# app = Flask(__name__)
#
# # Создание инстанса коллекторного регистра, на котором будут храниться метрики
# registry = CollectorRegistry()
#
# # Создание счетчика для метрик
# requests_counter = Counter(
#     'http_requests_total',
#     'Total number of HTTP requests',
#     ['method'],
#     registry=registry
# )
#
# # Создание summary для метрик
# request_time = Summary(
#     'http_request_duration_seconds',
#     'HTTP Request duration in seconds',
#     registry=registry
# )
#
# # Route для получения списка всех фильмов
# @app.route('/movies', methods=['GET'])
# @request_time.time()
# def get_movies():
#     requests_counter.labels(method='GET').inc()
#     # Ваш код для получения списка всех фильмов
#     movies = [
#         {'id': '1', 'title': 'Брат', 'description': 'Драматический фильм о бандитском мире 90-х годов в России'},
#         {'id': '2', 'title': 'Москва слезам не верит', 'description': 'Романтическая комедия о любви в Москве'},
#         {'id': '3', 'title': 'Левиафан', 'description': 'Драма о судьбе человека, сражающегося с коррупцией в России'}
#     ]
#     return jsonify(movies)
#
# # Route для добавления нового фильма
# @app.route('/movies', methods=['POST'])
# @request_time.time()
# def add_movie():
#     requests_counter.labels(method='POST').inc()
#     # Ваш код для добавления нового фильма
#     return jsonify({'message': 'Фильм успешно добавлен'}), 201
#
# # Route для получения информации о фильме по ID
# @app.route('/movies/<int:movie_id>', methods=['GET'])
# @request_time.time()
# def get_movie_by_id(movie_id):
#     requests_counter.labels(method='GET').inc()
#     # Ваш код для получения информации о фильме по ID
#     movie = {'id': str(movie_id), 'title': 'Фильм', 'description': 'Описание фильма'}
#     return jsonify(movie)
#
# # Route для обновления информации о фильме по ID
# @app.route('/movies/<int:movie_id>', methods=['PUT'])
# @request_time.time()
# def update_movie_by_id(movie_id):
#     requests_counter.labels(method='PUT').inc()
#     # Ваш код для обновления информации о фильме по ID
#     return jsonify({'message': 'Информация о фильме успешно обновлена'})
#
# # Route для удаления фильма по ID
# @app.route('/movies/<int:movie_id>', methods=['DELETE'])
# @request_time.time()
# def delete_movie_by_id(movie_id):
#     requests_counter.labels(method='DELETE').inc()
#     # Ваш код для удаления фильма по ID
#     return jsonify({'message': 'Фильм успешно удален'}), 204
#
# if __name__ == '__main__':
#     # Запуск HTTP-сервера Prometheus и вашего приложения
#     start_http_server(8000)
#     app.run(host='127.0.0.1', port=8080)
#
# # Отправка метрик в VictoriaMetrics после остановки приложения
# @app.teardown_appcontext
# def push_metrics(error):
#     push_to_gateway('victoriametrics.example.com:9091', job='movies-api', registry=registry)
#     return None

from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)

# Инициализируем объект PrometheusMetrics
metrics = PrometheusMetrics(app)

# Создаем счетчики для каждой метрики
request_counter = Counter('http_requests_total', 'Total number of HTTP requests')
movie_counter = Counter('movies_total', 'Total number of movie requests')
user_counter = Counter('users_total', 'Total number of user requests')

@app.route('/movies', methods=['GET'])
def get_movies():
    """
    Get a list of all movies
    ---
    responses:
      200:
        description: A list of movies
    """
    movie_counter.inc()
    movies = [
        {'id': '1', 'title': 'Брат', 'description': 'Драматический фильм о бандитском мире 90-х годов в России'},
        {'id': '2', 'title': 'Москва слезам не верит', 'description': 'Романтическая комедия о любви в Москве'},
        {'id': '3', 'title': 'Левиафан', 'description': 'Драма о судьбе человека, сражающегося с коррупцией в России'}
    ]
    return jsonify(movies)

@app.route('/users', methods=['GET'])
def get_users():
    """
    Get a list of all users
    ---
    responses:
      200:
        description: A list of users
    """
    user_counter.inc()
    users = [
        {'id': '1', 'name': 'John'},
        {'id': '2', 'name': 'Mary'},
        {'id': '3', 'name': 'Bob'}
    ]
    return jsonify(users)

if __name__ == 'main':
    app.run(host='127.0.0.1', port=8080)
