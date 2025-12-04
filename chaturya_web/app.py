from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chaturya")
def chaturya_page():
    # Put your current ngrok/colab API base URL here (no trailing /chat)
    api_url = "https://makenzie-suspensible-unmellifluously.ngrok-free.dev"
    return render_template("chaturya.html", api_url=api_url)

if __name__ == "__main__":
    app.run(debug=True)
