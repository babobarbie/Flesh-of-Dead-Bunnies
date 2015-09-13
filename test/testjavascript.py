from flask import Flask,render_template
app = Flask(__name__)

@approute("/")
def main()
	return render_template('testtemplate.html')

if __name__ == "__main__":
	app.run()