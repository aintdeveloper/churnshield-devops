from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "ChurnShield is live — DevOps Pipeline Working and CI/CD Pipeline is also working !"

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)