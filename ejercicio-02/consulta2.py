# Presentar los países de Asía, ordenados por el atributo Dial.
from sqlalchemy.orm import sessionmaker
from genera_base import PaisMetadata, engine

Session = sessionmaker(bind=engine)
session = Session()

#Filtro
paises_asia = session.query(PaisMetadata).filter(PaisMetadata.continente == 'AS').order_by(PaisMetadata.dial).all()

print("Paises de Asia, ordenados por DIAL")
for pais in paises_asia:
    print(pais.nombre_pais, "Dial:", (pais.dial))
