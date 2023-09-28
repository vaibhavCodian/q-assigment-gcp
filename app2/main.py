from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Vaibhav'

if __name__ == '__main__':
    app.run()
