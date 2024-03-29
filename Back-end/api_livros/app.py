"""
    - Objetivo - api que disponibiliza crud de livros
    - URL base - localhost
    - Endpoint:
        - localhost/livros (GET)
        - localhost/livros (POST)
        - localhost/livros/id (GET)
        - localhost/livors/id (PUT)
        - localhost/livros (DELETE)
    - Recursos - livros
""" 

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [  
    {
        'id': 1,
        'titulo': 'The Witcher - O último desejo',
        'autor': 'Andrzej Sapkowski'
    },
        {
        'id': 2,
        'titulo': 'The Witcher - A espada do destino',
        'autor': 'Andrzej Sapkowski'
    },
    {
        'id': 3,
        'titulo': 'The Witcher - O sangue dos elfos',
        'autor': 'Andrzej Sapkowski'
    },  
]
#consultar
@app.route('/livros', methods = ['GET'])
def get_livros():
    return jsonify(livros)

#consultar (id)
@app.route('/livros/<int:id>', methods = ['GET'])
def get_livro_by_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#Alterar
@app.route('/livros/<int:id>', methods = ['PUT'])
def editar_livro_by_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice]. update(livro_alterado)
            return jsonify(livros[indice])

#Criar
@app.route('/livros', methods = ['POST'])
def add_new_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

@app.route('/livros/<int:id>', methods={'DELETE'})
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)

