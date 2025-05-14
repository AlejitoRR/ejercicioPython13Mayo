
#se importa las librerias a usar en el proyecto
import requests
import configparser


# habilita capacidades de servidor.
#es la libreria encargada de gestionar la renderizacion de las vistas 


from flask import Flask, render_template, request


#el objeto principal de la aplicacion se llama app 
app = Flask(__name__)


#se gestiona la ruta inicial de la aplicacion
@app.route('/')
#aqui va el nombre de la funcion o metodo que gestiona la ruta

def weather_dashboard():
    return render_template('home.html')

#ruta que pinta los resultados
@app.route('/results', methods=['POST'])
def render_results():
    cityname = request.form['city']

    #ESTA VARIABLE ESTA ALMACENANDO EL VALOR DEL API KEY
    #que se encuentra en el archivo config.ini
    api = get_api_key();

    #vamos a conectarnos al api y a consumirlo
    data = get_weather_results(cityname, api)

    #se toma la temperatura del json   
    temp = "{0:.2f}".format(data['main']['temp'])
 
    #se toma la humedad del json
    feels_like = "{0:.2f}".format(data['main']['feels_like']) #se pone format porque es un numero decimal

    #se toma la condicion de la temperatura del json
    weather = data['weather'][0]['main']

    location = data['name']

    return render_template('results.html', location=location,temp=temp, feels_like=feels_like, weather=weather, location=location)

#aqui ya consumimos el servicio web 

def get_weather_results(cityname, api_key):
    url =' https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cityname, api_key)

    r = requests.get(url)
    return r.json()





def get_api_key():
    #esta funcion obtiene el valor del api key que se va a utilizar


    #se lee el archivo que guarda la api key del servicio web    
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config ['openweathermap']['api'] 

#Esta condicion siempre va en los proyectos de python 
#e indica que por defecto el metodo principal es el main 
#y entonces corre la aplicacion. 
if __name__ == "__main__":
    app.run(debug=True)