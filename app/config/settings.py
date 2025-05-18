import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, '../uploads')
PROCESSED_FOLDER = os.path.join(BASE_DIR, '../processed')
TRANSCRIPTIONS_FOLDER = os.path.join(BASE_DIR, '../transcriptions')
RESULTS = os.path.join(BASE_DIR, '../results')

SECRET_KEY = "edusync019"