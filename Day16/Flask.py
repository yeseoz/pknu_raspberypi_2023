from flask import Flask, request

app = Flask(__name__)
@app.route('/'
def home():
	return "Flask Server test"

@app.route('/user/<state>')
def show_username(State):
	if state == 'on':
		return "User : %s" %username
	elif state =='off':
		return "No"

@app.route('/post/<int:post_id>'
def show_post(post_id):
	return "post %d" %post_id

if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 8000 debug = True)

