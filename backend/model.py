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
