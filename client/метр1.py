from opentelemetry import metrics
from opentelemetry.exporter.prometheus import PrometheusMetricsExporter
from opentelemetry.sdk.metrics import MeterProvider

# Создание провайдера метрик
metrics.set_meter_provider(MeterProvider())
meter = metrics.get_meter(__name__)

# Создание экспортера Prometheus и его регистрация
exporter = PrometheusMetricsExporter(endpoint="http://localhost:9090/metrics")
metrics.get_meter_provider().start_pipeline(meter, exporter, interval=5)

# Создание метрик и запись значений
counter = meter.create_counter("example_counter", "The example counter", int)
counter.add(100)

