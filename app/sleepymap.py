from flask import Flask,render_template
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('heatmap.html', crimes = JSONobj)

if __name__ == "__main__":
	app.run()