from ..extensions import db
from ..association import association_table

class Turma(db.Model):
    __tablename__ = 'turma'
    id = db.Column(db.Integer, primary_key=True)
    horario = db.Column(db.String(100), nullable=False)

    materia_id = db.Column(db.Integer, db.ForeignKey('materia.id'))
    materia = db.relationship("Materia", backref="turma")

    professores = db.relationship("Professor", backref="turma")

    aluno = db.relationship("Aluno", secondary=association_table, backref="turma")

