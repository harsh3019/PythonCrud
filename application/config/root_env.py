from dotenv import load_dotenv
from pathlib import Path
import os

__BASE_DIR__ = Path(__file__).resolve().parent
__PARENT_DIR__ = os.path.dirname(__BASE_DIR__)
__ENV_PATH = os.path.join(__PARENT_DIR__,"application/config",".env")

def env_get(var: str, default = None) -> str:
    load_dotenv(__ENV_PATH)
    val = os.getenv(var, default=default)
    return val