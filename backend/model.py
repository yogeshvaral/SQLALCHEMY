from exts import db

"""
class Benchmark
id: int primary key
Benchmark id: String
Benchmark Description:String
"""

class Benchmark(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    benchmark_id = db.Column(db.String(),nullable=False)
    benchmark_description = db.Column(db.String(), nullable=False)

    def __repr__(self) -> str:
        return f"< Benchmark {self.Benchmark_id}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self,benchmark_id,benchmark_description):
        print(benchmark_id+""+"_"+benchmark_description)
        self.benchmark_id = benchmark_id
        self.benchmark_description = benchmark_description
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

"""
class Rule
id:int
name:String
description:String
config:String
"""
class Rule(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(),nullable=False)
    description = db.Column(db.String(),nullable=False)
    config = db.Column(db.String(),nullable=False)

    def __repr__(self) -> str:
        return f"< Rule {self.id}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self,name,description,config):
        self.name = name
        self.description = description
        self.config = config
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

class User(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(),nullable=False)
    password = db.Column(db.String(),nullable=False)
    email = db.Column(db.String(),nullable=False)
    type = db.Column(db.String(),nullable=False)

    def __repr__(self)-> str:
        return f'<User {self.username}>'

    def save(self):
        db.session.add(self)
        db.session.commit()