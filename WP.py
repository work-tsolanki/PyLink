from flask import Flask 


class Application():

    def __init__(self):
        
        self.flask_app = Flask(__name__)

        @self.flask_app.route('/<name>')
        def hello_world(name):
            return f"Hello {name}"       
        
        
if __name__ == '__main__':
    
    app = Application()
    app.flask_app.run()
    
