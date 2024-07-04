from flask import Flask, render_template

app = Flask(__name__)
# route = linktanana.com
# funcao = o que voce quer exibir naquela pagina
# template = para colocar htmls o nome tem que ser templates!

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):                   #nome_usuario =nome_usuario : passa o valor da variavel python para a variavel com o mesmo nome para o template html usuarios.html
    return render_template("usuarios.html", nome_usuario =nome_usuario)
    
#if _name verifica se o codigo esta sendo executado diretamente
#debug=true : faz o site atualizar as mudanças quase automaticamente | app.run coloca o site no ar
if __name__ == '__main__':
    app.run(debug=True)


