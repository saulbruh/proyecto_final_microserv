from flask import Flask, session
app = Flask(__name__)

app.secret_key = "clave_secreta"

@app.route("/login")
def login():
    session["usuario"] = "Juan"
    return "Usuario autenticado"

@app.route("/user")
def get_user():
    return session.get("usuario")

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return "Sesión cerrada"