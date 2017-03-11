from flask import Flask
app = Flask(__name__)


@app.route('/add/<int:n1>,<int:n2>')
def add(n1,n2):
	sum - n1 + n2
	return "%d" % (sum)


if __name__ == '__main__':
    app.run()
