from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# ✅ Usa la URL completa de conexión que Railway ya genera.
# Puedes usar MYSQL_URL o MYSQL_PUBLIC_URL, según cuál funcione mejor para tu caso.
# Aquí uso MYSQL_URL como ejemplo:
DATABASE_URL = os.environ.get("MYSQL_URL")

# ✅ Si prefieres construirla manualmente, podrías usar:
# DATABASE_URL = f"mysql+pymysql://{os.environ['MYSQLUSER']}:{os.environ['MYSQLPASSWORD']}@{os.environ['MYSQLHOST']}:{os.environ['MYSQLPORT']}/{os.environ['MYSQLDATABASE']}"

# ❌ Ya NO necesitas conexión sin base de datos:
# DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/"

# ❌ Ya NO necesitas nombre de base de datos local:
# DATABASE_NAME = "jpe"

# ❌ Ya NO necesitas crear la base de datos:
# engine = create_engine(DATABASE_URL_WITHOUT_DB)
# with engine.connect() as connection:
#     connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME};"))

# ✅ Usa solo el motor apuntando a la base de datos ya existente en la nube:
engine = create_engine(DATABASE_URL)

# ✅ Crea la sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Base para los modelos SQLAlchemy
Base = declarative_base()
