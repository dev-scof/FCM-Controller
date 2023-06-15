import os
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path, verbose=True)
APP_NAME="SCOF"
class Config:
    FCM_CRED_PATH = os.environ[APP_NAME+"_FCM_CRED_PATH"]