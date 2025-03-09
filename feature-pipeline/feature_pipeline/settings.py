import os
from pathlib import Path
from typing import Union  # used for type hinting - allows you to specify the type of the variable,function argumemnts and function return values
#Union is a type constructor that allows you to specify that a variable or function can accept values of multiple types.

from dotenv import load_dotenv


def load_env_vars (root_dir: Union[str, Path]) -> dict:
    """
    Load environment variables from .env.default and env files
    """

    # Convert root_dir to Path object if it is a string
    root_dir = Path(root_dir) if isinstance(root_dir,str) else root_dir

    load_dotenv(dotenv_path=root_dir / '.env.default')
    load_dotenv(dotenv_path=root_dir / '.env',override=True)

    return dict(os.environ)

def get_root_dir (default_value:str=".") -> Path:
    """
    Get the root directory of the project
    """

    return Path(os.getenv("ML_PIPELINE_ROOT_DIR",default_value)).resolve()

ML_PIPELINE_ROOT_DIR = get_root_dir()
OUTPUT_DIR = ML_PIPELINE_ROOT_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SETTINGS = load_env_vars(root_dir=ML_PIPELINE_ROOT_DIR)