# Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".
from sqlalchemy.orm import sessionmaker
from genera_base import PaisMetadata, engine
from sqlalchemy import or_

Session = sessionmaker(bind=engine)
session = Session()

# Filtro para encontrar caracteres en los nombres de los paises

filtro_parte = session.query(PaisMetadata).filter(\
    or_(
        PaisMetadata.nombre_pais.ilike('%uador%'), 
        PaisMetadata.capital.ilike('%ito%')
        )
).all()

# Presentar nombre del pais

print('Países que contienen "uador" en el nombre o "ito" en la capital:')
for pais in filtro_parte:
    print("-----------------------------------------")
    print(pais.nombre_pais, "Capital: ", pais.capital)



