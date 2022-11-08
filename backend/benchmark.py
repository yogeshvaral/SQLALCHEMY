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
@benchmark_ns.route('/benchmarks')
class BenchmarksResource(Resource):
    @benchmark_ns.marshal_list_with(benchmark_model)
    def get(self):
        benchmarks = Benchmark.query.all()
        return benchmarks

    @benchmark_ns.marshal_with(benchmark_model)
    def post(self):
        data = request.get_json()
        print(data)
        new_benchmark =  Benchmark(
            benchmark_id=data.get('benchmark_id'),
            benchmark_description = data.get('benchmark_description')
        )
        new_benchmark.save()
        return new_benchmark

# @benchmark_ns.route('/benchmark/<id:int>')
# class BenchmarkReport(Resource):
#     @benchmark_ns.marshal_with(benchmark_model)
#     def get(self,id):
#         benchmark = Benchmark.query.get_or_404(id)
#         return benchmark

#     @benchmark_ns.marshal_with(benchmark_model)
#     def put(self,id):
#         benchmark_to_update = Benchmark.query.get_or_404(id)
#         data = request.get_json()
#         benchmark_to_update.update(data.get('benchmark_id'),data.get('benchmark_description'))
#         return benchmark_to_update

