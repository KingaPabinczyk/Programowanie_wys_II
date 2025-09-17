from flask import Flask, render_template_string, abort

app = Flask(__name__)

users = {
    1: {"name": "Ala", "age": 22},
    2: {"name": "Bartek", "age": 25},
    3: {"name": "Celina", "age": 30}
}

@app.route("/")
def home():
    return render_template_string("""
        <h1>Witaj na mini portalu!</h1>
        <ul>
            <li><a href="/about">O nas</a></li>
            <li><a href="/users">Lista użytkowników</a></li>
        </ul>
    """)

@app.route("/about")
def about():
    return render_template_string("""
        <h1>O nas</h1>
        <p>To jest prosty mini portal stworzony w Flasku.</p>
        <a href="/">Powrót do strony głównej</a>
    """)

@app.route("/users")
def list_users():
    user_links = "".join([f'<li><a href="/user/{uid}">{user["name"]}</a></li>'
                          for uid, user in users.items()])
    return render_template_string(f"""
        <h1>Lista użytkowników</h1>
        <ul>
            {user_links}
        </ul>
        <a href="/">Powrót do strony głównej</a>
    """)

@app.route("/user/<int:user_id>")
def user_profile(user_id):
    user = users.get(user_id)
    if user:
        return render_template_string(f"""
            <h1>Profil użytkownika</h1>
            <p>{user['name']}, {user['age']} lat</p>
            <a href="/users">Powrót do listy użytkowników</a>
        """)
    else:
        return render_template_string("""
            <h1>Użytkownik nie istnieje</h1>
            <a href="/users">Powrót do listy użytkowników</a>
        """), 404

if __name__ == "__main__":
    app.run(debug=True)
