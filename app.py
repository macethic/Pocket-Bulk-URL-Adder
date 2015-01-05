import pypocket
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug import secure_filename
import threading
app = Flask(__name__)

def add_url(urls):
	for url in urls:
		pypocket.Pocket_Add(url)
		print "\n\nDone " + url + "\n\n"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	urls = request.form['Staff_Address'].split()
	for url in urls:
		pypocket.Pocket_Add(url)
		print "Added" + url
	#t1 = threading.Thread(target=add_url, args = urls)
	#t1.start()
	return "thanks"

if __name__ == '__main__':
	app.run()
