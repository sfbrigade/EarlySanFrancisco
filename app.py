import os
from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 8080.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
