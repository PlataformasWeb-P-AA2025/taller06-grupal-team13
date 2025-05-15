import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_base import PaisMetadata, engine

#Lectura de datos en ambiente local con request

url = 'https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json'

respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = respuesta.json()
else:
    print('Error al obtener los datos')

#Guardar los datos en la base de datos local

Session = sessionmaker(bind=engine)
session = Session()

for data in datos:
    pais = PaisMetadata(
                        nombre_pais = data.get('CLDR display name'),
                        capital = data.get('Capital'),
                        continente = data.get('Continent'),
                        dial = data.get('Dial'),
                        geoname_id = data.get('Geoname ID'),
                        itu = data.get(''),
                        lenguajes = data.get('Languages'),
                        es_independiente = data.get('is_independent'))
    session.add(pais)

session.commit()

print("Datos insertados correctamente.")
