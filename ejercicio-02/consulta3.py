# Presentar los lenguajes de cada país.
from sqlalchemy.orm import sessionmaker
from genera_base import PaisMetadata, engine

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(PaisMetadata).all()

print("Lenguaje de los paises:")

for pais in paises:
    print("----------------------------------------------")
    print(pais.nombre_pais, "- Lenguaje: ", pais.lenguajes)