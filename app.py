from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Flask Task App!</h1>"

@app.route('/tasks')
def tasks():
        return "this is the task list page."


@app.route('/about')
def about():
    return "<h1>About Task Flask App</h1>" \
    "<p>This is a simple Flask application to manage tasks.</p>" \
    "<p>It allows users to create, view, and manage their tasks efficiently.</p>" \



if __name__ == '__main__':
    app.run(debug=True)
