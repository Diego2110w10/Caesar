from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home (name= 'Home'):
        return render_template ('index.html', name=name)

    @app.route("/encode")
    def encode (name='encode'):
        return render_template('encode.html', name=name)
        
    return app