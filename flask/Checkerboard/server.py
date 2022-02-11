from flask import Flask, render_template
app = Flask(__name__)


@app.route('/checkers/<rows>/<columns>')
def checkers(rows, columns):
    return render_template('index.html', rows=int(rows), col=int(columns))


if __name__ == "__main__":
    app.run(debug=True)
