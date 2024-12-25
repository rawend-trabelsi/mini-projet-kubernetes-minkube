
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Bienvenue Rawend sur application Flask déployée sur Kubernetes"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
