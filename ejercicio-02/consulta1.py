# Presentar todos los países del continente americano
from sqlalchemy.orm import sessionmaker
from genera_base import PaisMetadata, engine

Session = sessionmaker(bind=engine)
session = Session()

# Filtro para encontrar paises del continente Americano
paises_america = session.query(PaisMetadata).filter(PaisMetadata.continente.in_(['NA', 'SA']))

# Recorrer los datos y presentar los paises que pasen el filtro
for pais in paises_america:
    print(pais)
