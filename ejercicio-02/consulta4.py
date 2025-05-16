# Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa
from sqlalchemy.orm import sessionmaker
from genera_base import PaisMetadata, engine

Session = sessionmaker(bind=engine)
session = Session()

paises_europa = session.query(PaisMetadata).filter(PaisMetadata.continente =='EU').order_by(PaisMetadata.capital).all()

print("Paises de Europa y su capital:")
for pais in paises_europa:
    print("-----------------------------------------")
    print(pais.nombre_pais, "Capital: ", pais.capital)

    