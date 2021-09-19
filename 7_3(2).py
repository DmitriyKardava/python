import os
import shutil
project_base = "my_project"
templates_path = os.path.join(project_base, "templates")
for root, dirs, files in os.walk("my_project"):
    for _dir in dirs:
        if (os.path.join(root, _dir).find(templates_path)) != 0 and _dir == 'templates':
            shutil.copytree(os.path.join(root, _dir), templates_path, dirs_exist_ok=True)
