from flask import request,jsonify
from flask_restx import Resource,fields,Namespace
from model import Benchmark
from flask_jwt_extended import jwt_required

benchmark_ns = Namespace("benchmark",description="benchmark namespace")

benchmark_model = benchmark_ns.model(
    "benchmark",
    {
        "id": fields.Integer(),
        "benchmark_id": fields.String(),
        "benchmark_description": fields.String()
    }
)
@benchmark_ns.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"Message": "HelloWorld"}