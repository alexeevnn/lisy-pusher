from flask import Flask, request
import requests

app = Flask(__name__)

MAKE_WEBHOOK_URL = 'https://hook.eu2.make.com/dc9z0xqyl7gqxljdstah31r83rx3s9ht'

@app.route('/', methods=['POST'])
def push():
    data = request.json
    if 'text' in data:
        requests.post(MAKE_WEBHOOK_URL, json={"text": data['text']})
        return 'OK'
    return 'No text', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
