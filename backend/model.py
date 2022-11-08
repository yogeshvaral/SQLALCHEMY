from exts import db

"""
class Benchmark
id: int primary key
Benchmark id: String
Benchmark Description:String
"""

class Benchmark(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Benchmark_id = db.Column(db.String(),primary_key=True, nullable=False)
    Benchmark_description = db.Column(db.String(), nullable=False)

    def __repr__(self) -> str:
        return f"< Benchmark {self.Benchmark_id}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self,description):
        self.Benchmark_description = description
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
