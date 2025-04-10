from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    return f"Usuario: {username}, Contraseña: {password}"


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            error = "El nombre de usuario es obligatorio."
        else:
            return f"Usuario registrado: {username}"
    return render_template("register.html", error=error)

if __name__ = "__main__":
    app.run(debug=True)