from ..extensions import db

class Materia(db.Model):
    __tablename__ = 'materia'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    codigo = db.Column(db.String(7), nullable=False)

    turma = db.relationship('Turma', backref="materia")