from flask import Flask, render_template, request # type: ignore
import requests # type: ignore

app = Flask(__name__)
API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # <-- Reemplaza con tu clave

@app.route('/', methods=['GET', 'POST'])
def index():
    clima = None
    error = None

    if request.method == 'POST':
        ciudad = request.form['ciudad']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            datos = respuesta.json()
            clima = {
                'ciudad': ciudad,
                'temperatura': datos['main']['temp'],
                'descripcion': datos['weather'][0]['description'],
                'humedad': datos['main']['humidity'],
                'viento': datos['wind']['speed']
            }
        else:
            error = "No se pudo obtener el clima. Verifica el nombre de la ciudad o tu API key."

    return render_template('index.html', clima=clima, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
