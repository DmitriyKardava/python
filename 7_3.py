import os
from shutil import copy
project_base = "my_project"
templates_path = os.path.join(project_base, "templates")
template_extensions = ('html', 'htm', 'css', 'js')
for root, dirs, files in os.walk("my_project"):
    if (root.find(templates_path)) != 0:
        for file in files:
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            if ext in template_extensions:
                t_dir = os.path.split(root)[1]
                if not os.path.exists(os.path.join(templates_path, t_dir)):
                    os.makedirs(os.path.join(templates_path, t_dir))
                copy(os.path.join(root, file), os.path.join(os.path.join(templates_path, t_dir), file))
