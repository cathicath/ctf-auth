from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Simulerad "databas" med flera användare (endast en är giltig)
USERS = {
    "Anubis": "deathgod123",  # Spelarens konto
    "Khonsu": "moonlight123",  # Målet att hacka
}

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in USERS:
            if USERS[username] == password:
                session["user"] = username

                if username == "Khonsu":
                    return redirect(url_for("account"))  # Endast Khonsu skickas till account

                return render_template("index.html")  # Anubis stannar på index
            else:
                error = "Incorrect password"
        else:
            error = "Invalid username"

    return render_template("index.html", error=error)

@app.route("/account")
def account():
    if "user" in session and session["user"] == "Khonsu":
        return render_template("account.html", username=session["user"])
    return redirect(url_for("login"))

@app.route("/reset-password", methods=["POST"])
def reset_password():
    if "user" not in session:  # Blockera om användaren inte är inloggad
        return jsonify({"success": False, "message": "You must be logged in to reset a password."}), 403

    username = request.form.get("username")  # Användarnamnet tas från requesten
    new_password = request.form.get("new_password")

    if username in USERS:
        USERS[username] = new_password
        return jsonify({"success": True, "message": "Password successfully reset!"})

    return jsonify({"success": False, "message": "User not found."}), 400



@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
