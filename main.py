from flask import Flask
import time

from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

app = Flask(__name__)

trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({SERVICE_NAME: "flask-jaeger-demo"})
    )
)
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

FlaskInstrumentor().instrument_app(app)

@app.route("/")
def index():
    return "Главная страница"

@app.route("/slow")
def slow():
    time.sleep(2)
    return "Это медленная страница"

if __name__ == "__main__":
    app.run(port=5000)