from flask import Flask, render_template, send_file


app = Flask(__name__, template_folder='../template')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/download/<filename>')
def download(filename = None):
    if filename is None:
        return render_template('404.html')
    try:
        return send_file('/home/shawn/Homepage/download/'+filename, as_attachment=True)
    except:
        return render_template('404.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0')
