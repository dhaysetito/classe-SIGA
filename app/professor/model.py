from ..extensions import db

class Professor(db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    formacao = db.Column(db.String(50), nullable=False)

    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'))
    #turma = db.relationship("Turma", backref="professores")
    