from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    MESHY_API_KEY = os.getenv('MESHY_API_KEY')
    IMAGE_UPLOAD_URL = os.getenv('IMAGE_UPLOAD_URL')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}