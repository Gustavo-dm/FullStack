from flask import Flask, render_template, request, url_for, redirect

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Gusta/Desktop/Impacta/Fullstack/25_02/base.sqlite'

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(20))

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


db.create_all()


@app.route("/")
def index():
    return {'Acesse': '/cadastrar ou /lista'}


@app.route("/cadastrar")
def cadastrar():
    return render_template("index.html")


@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("password")

        if nome and email and senha:
            f = User(nome, email, senha)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("index"))


@app.route("/lista")
def lista():
    users = User.query.all()
    return render_template("lista.html", users=users)


if __name__ == "__main__":

    app.run()
