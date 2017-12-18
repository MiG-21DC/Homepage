from flask import Flask, render_template, send_file
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='../template')
Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/testfield/<name>')
def testfield(name='Stranger'):

    return render_template('testfield.html', name=name)

@app.route('/download/<filename>')
def download(filename=None):
    if filename is None:
        return render_template('404.html')
    try:
        return send_file('/home/shawn/Homepage/download/'+filename, as_attachment=True)
    except:
        return render_template('404.html')

@app.route('video/<videoname>')
def video(video_file=None):
    return render_template('videotest.html', video_file='/home/shawn/Homepage/video/'+video_file)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
