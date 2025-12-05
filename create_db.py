# create_db.py
from db import engine
from models import Base

# Cria todas as tabelas definidas em models.py
Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!") 