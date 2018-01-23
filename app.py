from flask import Flask
app = Flask(__name__)

@app.route("/sample/api/v1.0/")
def hello():
    return "Hello World! This is Ram!"

if __name__ == "__main__":
	app.run()
