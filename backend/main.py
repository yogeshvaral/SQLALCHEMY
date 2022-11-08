from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_restx import Api,Resource,fields
from exts import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from model import Benchmark
from benchmark import benchmark_ns

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    api = Api(app=app,doc='/docs')
    migrate = Migrate(app=app,db=db)
    JWTManager(app=app)
    api.add_namespace(benchmark_ns)

    @app.shell_context_processor
    def make_shell_context():
        return {
            "db":db,
            "Benchmark":Benchmark
        }

    return app
