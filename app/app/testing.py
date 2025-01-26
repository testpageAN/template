import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'app', 'static')
]

print(STATICFILES_DIRS)
print(BASE_DIR)
