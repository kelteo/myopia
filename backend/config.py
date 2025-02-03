import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:oPPzBpxyfjSGlBzbXlvUjRJmTKQOksGR@postgres.railway.internal:5432/railway")
SECRET_KEY = os.getenv("SECRET_KEY", "10111213")
