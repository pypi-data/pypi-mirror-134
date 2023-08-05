import os
from pathlib import Path

ROOT_DIR = Path(os.path.abspath(__file__)).parent.parent

RASTLESS_TABLE_NAME = os.getenv("RASTLESS_TABLE_NAME", "rastless-prod")
RASTLESS_BUCKET_NAME = os.getenv("RASTLESS_BUCKET_NAME", "rastless-prod")
