from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


# URL de conexión sin especificar la base de datos
#DATABASE_URL = "mysql+pymysql://uetctip1fmcn5wdp:shwaoFGKNmOB2MVn2FqM@bbw4as08rnqsck1swmou-mysql.services.clever-cloud.com:3306/"
# ✅ 1. URL de conexión sin la base de datos para crearla
DATABASE_URL = "mysql+pymysql://root:12345678@localhost:3306/"

# Nombre de la base de datos
#DATABASE_NAME = "bbw4as08rnqsck1swmou"
# ✅ 2. Nombre de la base de datos local
DATABASE_NAME = "jpe"

# ✅ 3. Crear el motor de conexión inicial
engine = create_engine(DATABASE_URL)

# ✅ 4. Crear la base de datos si no existe
with engine.connect() as connection:
    connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME};"))

# Actualizar la URL de la base de datos para incluir el nombre de la base de datos
#DATABASE_URL = f"mysql+pymysql://uetctip1fmcn5wdp:shwaoFGKNmOB2MVn2FqM@bbw4as08rnqsck1swmou-mysql.services.clever-cloud.com:3306/{DATABASE_NAME}"
# ✅ 5. Actualizar la URL para apuntar a la base de datos ya creada
DATABASE_URL = f"mysql+pymysql://root:12345678@localhost:3306/{DATABASE_NAME}"

# ✅ 6. Nuevo engine ya apuntando a la base específica
engine = create_engine(DATABASE_URL)

# ✅ 7. Crear sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ 8. Base para modelos SQLAlchemy
Base = declarative_base()
