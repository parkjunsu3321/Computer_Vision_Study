import shutil
from pathlib import Path

import kagglehub

path = kagglehub.competition_download('global-wheat-detection')
here = Path(__file__).parent
shutil.copytree(path, here, dirs_exist_ok=True)

print("Competition files copied to:", here)
