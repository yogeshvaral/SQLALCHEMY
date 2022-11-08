from flask import Flask,request,jsonify
from flask_restx import Resource,fields,Namespace
from model import Rule
from flask_jwt_extended import jwt_required

rule_ns = Namespace('rule','Rule Namespace')
rule_model = rule_ns.model(
    "rule",
    {
        "id": fields.Integer(),
        "name": fields.String(),
        "description": fields.String(),
        "config": fields.String()
    }
)

@rule_ns.route('/rules')
class RulesResource(Resource):
    @rule_ns.marshal_list_with(rule_model)
    def get(self):
        rules = Rule.query.all()
        return rules
        
    @jwt_required()
    @rule_ns.marshal_with(rule_model)
    def post(self):
        data = request.get_json()
        new_rule =Rule(name=data.get('name'),description=data.get('description'),config=data.get('config'))
        new_rule.save()
        return new_rule

@rule_ns.route('/rule/<int:id>')
class RuleResource(Resource):
    @jwt_required()
    @rule_ns.marshal_with(rule_model)
    def get(self,id):
        rule = Rule.query.get_or_404(id)
        return rule

    @jwt_required()    
    @rule_ns.marshal_with(rule_model)
    def put(self,id):
        rule_to_update = Rule.query.get_or_404(id)
        data = request.get_json()
        rule_to_update.update(data.get('name'),data.get('description'),data.get('config'))
        return rule_to_update
