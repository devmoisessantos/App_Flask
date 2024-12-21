from project.app import db

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Integer, nullable=False)
    
    def __init__(self, titulo: str, descricao: str, valor: int):
        if valor < 0:
            raise ValueError("O valor do livro não pode ser negativo.")
        self.titulo = titulo
        self.descricao = descricao
        self.valor = valor
    
    def __repr__(self):
        return f"<Livro {self.titulo} - R$ {self.valor}>"
