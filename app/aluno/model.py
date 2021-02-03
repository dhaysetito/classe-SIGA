from ..extensions import db
from ..association import association_table

class Aluno(db.Model):
    __tablename__ = 'aluno'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    periodo_ingresso = db.Column(db.String(6), nullable=False)
    curso = db.Column(db.String(50), nullable=False)

    boletim = db.relationship("Boletim", backref="aluno",)

    turma = db.relationship("Turma", secondary=association_table, backref="aluno")

    professores = db.relationship("Professor", secondary=association_table, backref="aluno")