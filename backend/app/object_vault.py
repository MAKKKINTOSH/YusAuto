import os

from minio import Minio
from dotenv import load_dotenv

load_dotenv()

vault = Minio(
    os.getenv("MINIO_CONNECTION_STRING")
)