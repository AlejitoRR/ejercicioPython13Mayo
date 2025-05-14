
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



#Esta condicion siempre va en los proyectos de python 
#e indica que por defecto el metodo principal es el main 
#y entonces corre la aplicacion. 
if __name__ == "__main__":
    app.run(debug=True)