from flask_app import app
@app.route('/')
def hello_world():
    return "hello World!"


if __name__=="__main__":
    app.run(debug=True)
