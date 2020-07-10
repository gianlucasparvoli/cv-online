from flask import Flask,render_template,json
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
PORT = 5000
app.secret_key = 'some_secret'

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port = PORT,debug=False)