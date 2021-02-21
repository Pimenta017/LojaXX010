from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)
usr = User()


@app.route('/tabela')
def tabela():
    dados = usr.lista()
    return render_template('Utilizadores/tabela.html', tabela=dados, max=len(dados), usr=usr)


@app.route('/registo', methods=['GET', 'POST'])
def route():
    erro = None
    if request.method == 'POST':
        v1 = request.form['utilizador']
        v2 = request.form['email']
        v3 = request.form['passe']
        v4 = request.form['cpasse']
        if usr.existe(v1):
            erro = 'O Utilizador já existe.'
        elif v3 != v4:
            erro = 'A palavra passe não coincide.'
        else:
            erro = 'Conta criada com sucesso.'
            usr.gravar(v1, v2, v3)
    return render_template('Utilizadores/registo.html', erro=erro, usr=usr)


@app.route('/')
def index():
    return render_template('index.html', usr=usr)


@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        v1 = request.form['utilizador']
        v2 = request.form['passe']
        if not usr.existe(v1):
            erro = 'O Utilizador não existe.'
        elif not usr.log(v1, v2):
            erro = 'A palavra passe está errada.'
        else:
            usr.login = v1
            erro = 'Bem-Vindo.'
    return render_template('Utilizadores/login.html', erro=erro, usr=usr)


@app.route('/logout')
def logout():
    usr.reset()
    return redirect('/')


@app.route('/apagar', methods=['GET', 'POST'])
def apagar():
    erro = None
    if request.method == 'POST':
        v1 = request.form['utilizador']
        v2 = request.form['passe']
        if not usr.existe(v1):
            erro = 'O Utilizador não existe.'
        elif not usr.log(v1, v2):
            erro = 'A palavra passe está errada.'
        else:
            usr.apaga(v1)
            erro = 'Conta Eliminada com Sucesso.'
    return render_template('Utilizadores/apagar.html', erro=erro, usr=usr)


@app.route('/newpasse', methods=['GET', 'POST'])
def newpasse():
    erro = None
    if request.method == 'POST':
        v1 = request.form['utilizador']
        v0 = request.form['apasse']
        v2 = request.form['passe']
        v3 = request.form['cpasse']
        if not usr.existe(v1):
            erro = 'O Utilizador não existe.'
        elif not usr.log(v1, v0):
            erro = 'A palavra passe está errada.'
        elif v2 != v3:
            erro = 'A palavra passe não coincide.'
        else:
            usr.alterar(v1, v2)
    return render_template('Utilizadores/newpasse.html', erro=erro, usr=usr)


if __name__ == '__main__':
    app.run(debug=True)
