from flask import Flask
import requests
import random

app = Flask(__name__)

backend_urls = ['http://backend1:5001/backend1', 'http://backend2:5002/backend2']

@app.route('/')
def index():
    # Randomly choose a backend
    chosen_backend = random.choice(backend_urls)

    print(f"Chosen backend: {chosen_backend}")
    
    # Make a request to the chosen backend
    backend_response = requests.get(chosen_backend)
    
    return f"Request sent to: {chosen_backend}\nResponse from backend: {backend_response.text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
