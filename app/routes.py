from app import app

@app.route('/')
def home():
    return "<h1>Welcome to Task manager!</h1>"