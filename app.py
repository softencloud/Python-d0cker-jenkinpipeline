from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Jenkins Tutorials</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')  # Host set to 0.0.0.0 to make the app accessible from any IP

