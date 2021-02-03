from .extensions import db

association_table = db.Table('association', db.Model.metadata, 
                    db.Column('aluno', db.Integer, db.ForeignKey('aluno.id')),
                    db.Column('turma', db.Integer, db.ForeignKey('turma.id')))