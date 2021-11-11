import os

from flask import Flask, render_template, request, json, redirect, url_for, session, jsonify
from flask.wrappers import Response
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery
from pathlib import Path
import time

class MyResponse(Response):
    default_mimetype = 'application/json'

# CONFIGURACION DE LA APP
app = Flask(__name__)
app.secret_key = 'clave secreta'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["CACHE_TYPE"] = "null"

# RDFLIB

g = Graph()
g.namespace_manager.bind('fountain', Namespace("http://www.smartCityParks.es/group07/resource/Fountain/"), override=False)
path = g.parse("./rdf/output.nt", format="nt")


# MAIN Y METODOS PARA MOSTRAR PAGINAS

@app.route("/")
def main():
    return render_template('index.html')
@app.route("/results", methods=['POST', 'GET'])
def results():
    return render_template("results.html")

@app.route("/busqueda", methods=['POST', 'GET'])
def busqueda():
    try:
        hora=time.strftime("%d%m%Y_%H%M%S")
        filename=str(hora)+".json"
        fileroute="../static/"+hora+".json"
        filepath=Path(fileroute)
        filetoOpne=filepath/filename
        _request=request.args.get('districName')
        #_districName = str(request.form['districName'])
        _districName=str(_request)
        _districName = _districName.lower()
        if _districName=="fuencarral" or _districName=="el pardo" or _districName=="fuencarral-el pardo" or _districName=="fuencarral el pardo" or _districName=="fuencarral-elpardo":
            _districName="Fuencarral-El Pardo"
        elif _districName=="la latina" or _districName=="lalatina":
            _districName=="Latina"
        elif _districName=="villa de vallecas" or _districName=="villadevallecas" or _districName=="villa-de-vallecas":
            _districName="Villa de Vallecas"
        elif _districName=="puente de vallecas" or _districName=="puentedevallecas" or _districName=="puente-de-vallecas":
            _districName="Puente de Vallecas"
        elif _districName=="ciudad lineal" or _districName=="ciudadlineal" or _districName=="ciudad-lineal":
            _districName="Ciudad Lineal"
        elif _districName == "San Blas" or _districName == "sanblas" or _districName == "san-blas":
            _districName = "San Blas"
        elif _districName == "Chamberi" or _districName == "chamberi" or _districName == "Chamberí" or _districName == "chamberí":
            _districName = "Chamberí"
        elif _districName == "Chamartín" or _districName == "Chamartín" or _districName == "Chamartin" or _districName == "chamartin":
            _districName = "Chamartín"
        elif _districName == "Tetuán" or _districName == "tetuán" or _districName == "tetuan" or _districName == "Tetuan":
            _districName = "Chamartín"
        elif _districName == "Vicálvaro" or _districName == "Vicalvaro" or _districName == "vicálvaro" or _districName == "vicalvaro":
            _districName = "Vicálvaro"
        elif _districName == "Moncloa-Aravaca" or _districName == "Moncloa" or _districName == "Aravaca" or _districName == "moncloa-aravaca" or _districName == "moncloa" or _districName == "aravaca":
            _districName = "Moncloa-Aravaca"
        else:
            _districName=_districName.capitalize()
        _jsonList= []
        wikiDataLink=None

        # SPARQL query

        g.parse(path, format="turtle")

        q1 = prepareQuery('''
        SELECT ?p
        WHERE {
        ?p <http://ww.smartCityParks.es/group07/ontology/Font#isInDistrict> <http://www.smartCityParks.es/group07/resource/District/PUENTE-DE-VALLECAS> 
        }
        '''
)       fountainList = g.query(q1) #LISTA CON LA QUERY

        if(len(_jsonList)==0):
            return render_template("error.html",error="El distrito introducido no es correcto o no existe")
        return render_template("results.html",distrito=_districName,enlace=wikiDataLink)
    except Exception as e:
        return json.dumps({'error': e})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=5000)