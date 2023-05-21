import os
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    api_key = os.environ.get('GIPHY_API_KEY')
    # Busca um GIF aleatório na API do Giphy
    response = requests.get(f'https://api.giphy.com/v1/gifs/random?api_key=SUA_CHAVE_DE_API&tag=&rating=g')
    if response.status_code == 200:
        gif_url = response.json()['data']['images']['original']['url']
        return render_template('index.html', background_image=gif_url)
    else:
        # Trata falha na chamada à API
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
