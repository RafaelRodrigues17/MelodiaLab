from flask import Flask, render_template, request, url_for, redirect, flash, session
import database

database.criar_tabelas()

app = Flask(__name__)
app.secret_key = "chave_muito_segura"

@app.route('/') #rota para a página inicial
def index():
    return render_template('index.html')

# Cria um dicionário e usuários e senha, SERÁ MIGRADO PARA O BANCO DE DADOS
@app.route("/home")
def home():
    email = session.get("usuario")  # agora está correto
    if not email:
        return redirect(url_for('login'))

    musicas = database.obter_musicas_usuario(email)
    return render_template("home.html", musicas=musicas)

# VERFIFICAR O LOGIN
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form = request.form  # Coletando os dados do formulário de login
        # Chamando a função 'login' do arquivo database para verificar a senha
        if database.login(form) == True:
            session['usuario'] = form['email'] # Armazena o email do usuário na sessão
            return redirect(url_for('home'))
        else:
            return "Ocorreu um erro ao fazer o login do usuário"  # Caso contrário, exibe mensagem de erro
    else:
        return render_template('login.html')  # Se for GET, renderiza o formulário de login

# Rota de cadastro ('/cadastro') que também pode ser acessada por GET ou POST
@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        form = request.form  # Coletando os dados do formulário de cadastro
        # Chamando a função 'criar_usuario' do arquivo database para cadastrar o usuário
        if database.criar_usuario(form) == True:
            return render_template('login.html')  # Se cadastro for bem-sucedido, redireciona para o login
        else:
            return "Ocorreu um erro ao cadastrar usuário"  # Caso contrário, exibe mensagem de erro
    else:
        return render_template('cadastro.html')  # Se for GET, renderiza o formulário de cadastro
 
@app.route('/excluir_usuario')
def excluir_usuario():
    email = session['usuario']
    
    if database.excluir_usuario(email):
        return redirect(url_for('login'))
    else:
        return "Ocorreu um erro ao excluir o usuário"
    
@app.route('/nova_musica', methods=["GET", "POST"])
def nova_musica():
    if request.method == "POST":
        form = request.form
        if database.nova_musica(form):
            return redirect(url_for('home'))  # redireciona para a função `home`
        else:
            return "Ocorreu um erro ao criar a música"
    else:
        return render_template('nova_musica.html')
    
@app.route('/editar_musica/<int:id>', methods=["GET", "POST"])
def editar_musica(id):
    email = session.get("usuario")
    if not email:
        return redirect(url_for('login'))

    if request.method == "POST":
        form = request.form
        form = dict(form)
        form['id'] = id
        if database.editar_musica(form):
            return redirect(url_for('home'))
        else:
            return "Erro ao editar música"
    else:
        musica = database.obter_musica_por_id(id, email)
        if not musica:
            return "Música não encontrada"
        return render_template('editar_musica.html', musica=musica)

@app.route("/excluir_musica/<int:id>")
def excluir_musica(id):
    email = session.get("usuario")
    if not email:
        return redirect(url_for("login"))

    database.excluir_musica(id)
    return redirect(url_for("home"))

# parte principal do programa
if __name__ == '__main__':
    app.run(debug=True) 