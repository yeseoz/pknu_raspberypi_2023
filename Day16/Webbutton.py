from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return "Button Server test"

app.route('/test')
def get():
	return render_template('test.html') 

if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = '8000', debug = True)
