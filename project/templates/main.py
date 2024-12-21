from project.templates.conn import result_filmes
from flask import render_template, request, redirect, url_for
from project.templates.app import app, db
from project.templates.models import Livro


with app.app_context():
    db.create_all()

conteudos = []
registros = []

# localhost:5000        POR PADRÃO É http://127.0.0.1:5000
# localhost:5000/hello
@app.route('/', methods=['GET', 'POST'])  
def index():
    if request.method == 'POST':
        if request.form.get('conteudo'):
            conteudos.append(request.form.get('conteudo'))
    return render_template(
        'index.html',
        conteudos=conteudos,
        livros=livros
    )

@app.route('/livros')
def livros():
    livros = Livro.query.all()
    page = request.args.get('page', 1, type=int)
    per_page = 2
    pagination = Livro.query.paginate(page=page, per_page=per_page)
    return render_template(
        'livros.html',
        livros=pagination
    )

@app.route('/<int:id>/update_livro', methods=['GET', 'POST'])
def update_livro(id):
    livro = Livro.query.filter_by(id=id).first()
    if request.method == 'POST':
        if request.form.get('titulo') and request.form.get('descricao') and request.form.get('valor'):
            titulo = request.form.get('titulo')
            descricao = request.form.get('descricao')
            valor = request.form.get('valor')
            if titulo and descricao and valor:
                livro.titulo = titulo
                livro.descricao = descricao
                livro.valor = int(valor)
                db.session.commit()
                return redirect(url_for('livros'))
                
    return render_template(
        'update_livros.html',
        livro=livro
    )

@app.route('/<int:id>/delete_livro')
def delete_livro(id):
    livro = Livro.query.filter_by(id=id).first()
    db.session.delete(livro)
    db.session.commit()
    return redirect(url_for('livros'))


@app.route('/add_livro', methods=['GET', 'POST'])
def add_livro():
    if request.method == 'POST':
        if request.form.get('titulo') and request.form.get('descricao') and request.form.get('valor'):
            titulo = request.form.get('titulo')
            descricao = request.form.get('descricao')
            valor = request.form.get('valor')
            if titulo and descricao and valor:
                add_livro = Livro(
                    titulo, 
                    descricao, 
                    int(valor)
                )
                db.session.add(add_livro)
                db.session.commit()
                return redirect(url_for('livros'))
                
    return render_template(
        'add_livros.html'
    )


@app.route('/diario', methods=['GET', 'POST'])
def diario():
    if request.method == 'POST':
        if request.form.get('aluno') and request.form.get('nota'):
            aluno = request.form.get('aluno').strip()
            nota = request.form.get('nota').strip()
            if aluno and nota:
                registros.append(
                    {
                        'aluno': aluno, 
                        'nota': nota
                    }
                )

    return render_template(
        'about.html',
        registros=registros

    )
@app.route('/filmes/<propriedade>')
def filmes(propriedade):
        
    return render_template(
        'filmes.html',
        filmes=result_filmes(propriedade)
    )

if __name__ == '__main__':
    app.run(debug=True)