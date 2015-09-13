from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    adrs = request.form['address']
    return render_template('index.html')

if __name__ == "__main__":
	app.run()