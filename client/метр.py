from __future__ import print_function
import logging
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

# Настройка логгера
logging.basicConfig(filename='C:/Users/Мария/Desktop/сервер/var/log/123.log', level=logging.INFO)

registry = CollectorRegistry()
gauge_movies_added = Gauge('movies_added_total', 'Total number of movies added', registry=registry)
gauge_movies_deleted = Gauge('movies_deleted_total', 'Total number of movies deleted', registry=registry)

# Инициализация трассировочного провайдера
trace.set_tracer_provider(TracerProvider())

# Инициализация экспортера Jaeger
jaeger_exporter = JaegerExporter(
    agent_host_name='127.0.0.1',
    agent_port=14268,
)

# Создание процессора спанов и добавление его к трассировочному провайдеру
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

tracer = trace.get_tracer(__name__)
configuration = swagger_client.Configuration()
configuration.host = 'http://127.0.0.1:8080/'
api_client = swagger_client.ApiClient(configuration=configuration)
api_instance = swagger_client.MovieApi(api_client=api_client)
body = swagger_client.Movie()  # Movie | Новый фильм
movie_id = 789  # int | ID фильма

with tracer.start_as_current_span("http_request"):
    try:
        # Добавить новый фильм
        api_instance.add_movie(body)
        gauge_movies_added.inc()
        logging.info('Added a new movie successfully')
    except ApiException as e:
        print("Exception when calling MovieApi->add_movie: %s\n" % e)
        logging.error('Exception when calling MovieApi->add_movie: %s\n' % e)

with tracer.start_as_current_span("delete_movie"):
    try:
        api_instance.delete_movie_by_id(movie_id)
        gauge_movies_deleted.inc()
        logging.info('Deleted movie with ID %d successfully' % movie_id)
    except ApiException as e:
        print("Exception when calling MovieApi->delete_movie_by_id: %s\n" % e)
        logging.error('Exception when calling MovieApi->delete_movie_by_id: %s\n' % e)

with tracer.start_as_current_span("get_movie"):
    try:
        api_response = api_instance.get_movie_by_id(movie_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MovieApi->get_movie_by_id: %s\n" % e)

with tracer.start_as_current_span("get_movies_list"):
    try:
        api_response = api_instance.get_movies_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MovieApi->get_movies_list: %s\n" % e)

with tracer.start_as_current_span("update_movie"):
    try:
        api_instance.update_movie_by_id(body, movie_id)
    except ApiException as e:
        print("Exception when calling MovieApi->update_movie_by_id: %s\n" % e)

push_to_gateway('localhost:9090', job='movie_api', registry=registry)
