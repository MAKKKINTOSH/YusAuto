from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(
    os.getenv("SQLALCHEMY_CONNECTION_STRING"),
    echo=True
)
