from flask import Flask, render_template, request, redirect

app = Flask(__name__)
filmes = []

@app.route('/', methods=['GET', 'POST'])
def adicionar_filme():
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        codigo = len(filmes)
        filmes.append([codigo, nome, genero])
        return render_template('adicionarfilme.html', filmes=filmes)
    else:
        return render_template('adicionarfilme.html')

@app.route('/adicionar', methods=['GET'])
def adicionar():
    return render_template('adicionarfilme.html')

@app.route('/editar_filmes/<int:codigo>', methods=['GET', 'POST'])
def editarfilme(codigo):
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        filmes[codigo] = [codigo, nome, genero]
        return redirect('/editar_filmes')
    else:
        contato = filmes[codigo]
        return render_template('editar_filmes.html', filmes=filmes)  # Renderiza o formulário de edição


@app.route('/apagar_filmes/<int:codigo>')
def apagar_filme(codigo):
    del filmes[codigo]
    for i in rangel(codigo, len(filmes)):
        filmes[i][0] = i
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
