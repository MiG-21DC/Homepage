from flask import Flask, render_template


app = Flask(__name__, template_folder='../template')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return "<h1 style='color:blue'>This site is built with Nginx, uWSGI and Flask on an Amazon Ubuntu server with SSL encrypted</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
