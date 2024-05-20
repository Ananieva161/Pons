from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter


trace.set_tracer_provider(TracerProvider())
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)
tracer = trace.get_tracer(__name__)
# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.host = 'http://127.0.0.1:8080/'
api_client = swagger_client.ApiClient(configuration=configuration)
api_instance = swagger_client.MovieApi(api_client=api_client)
body = swagger_client.Movie()  # Movie | Новый фильм
movie_id = 789  # int | ID фильма

try:
    with tracer.start_as_current_span("API get_movies_list"):
        # Получить список всех фильмов
        api_response = api_instance.get_movies_list()
        pprint(api_response)

    with tracer.start_as_current_span("API add_movie"):
        # Добавить новый фильм
        api_instance.add_movie(body)

    with tracer.start_as_current_span("API delete_movie_by_id"):
        # Удалить фильм по ID
        api_instance.delete_movie_by_id(movie_id)

    with tracer.start_as_current_span("API get_movie_by_id"):
        # Получить информацию о фильме по ID
        api_response = api_instance.get_movie_by_id(movie_id)
        pprint(api_response)

    with tracer.start_as_current_span("API update_movie_by_id"):
        # Обновить информацию о фильме по ID
        api_instance.update_movie_by_id(body, movie_id)

except ApiException as e:
    print("Exception when calling MovieApi: %s\n" % e)

