# Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
# - id_socio: entero (clave primaria, auto-incremental, unico)
# - dni: entero (unico)
# - nombre: string (longitud 250)
# - apellido: string (longitud 250)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Socio(Base):
    __tablename__ = 'socios'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    dni = Column('dni', String(30))
    nombre = Column('nombre', String(30))
    apellido = Column('apellido', String(30))

engine = create_engine('sqlite:///socios.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
Base.metadata.create_all(engine)
