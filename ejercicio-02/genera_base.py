from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///basepaismetada.db', echo=True)
Base = declarative_base()

class PaisMetadata(Base):
    __tablename__ = 'pais_metadata'

    id = Column(Integer, primary_key=True)
    nombre_pais = Column(String(100))        # "CLDR display name"
    capital = Column(String(100))            # "Capital"
    continente = Column(String(10))          # "Continent"
    dial = Column(String(10))                # "Dial"
    geoname_id = Column(Integer)             # "Geoname ID"
    itu = Column(String(10), nullable=True)  # "ITU"
    lenguajes = Column(String(200))          # "Languages"
    es_independiente = Column(String(10))    # "is_independent"

    def __str__(self):
        return f"{self.nombre_pais} - {self.capital} - {self.continente}"

Base.metadata.create_all(engine)

