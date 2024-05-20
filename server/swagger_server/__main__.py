#!/usr/bin/env python3

import connexion
from flask import Flask

from swagger_server import encoder

from prometheus_flask_exporter import PrometheusMetrics



def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    metrics = PrometheusMetrics(app.app)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Movies API'}, pythonic_params=True)
    app.run(port=8080)
    # metrics = PrometheusMetrics(app.app)



if __name__ == '__main__':
    main()
