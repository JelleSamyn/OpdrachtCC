import os
import zipfile
from datetime import datetime

# Project folder (current directory)
project_dir = os.getcwd()

# Backup folder
backup_dir = os.path.join(project_dir, "backups")
os.makedirs(backup_dir, exist_ok=True)

# Timestamp voor unieke naam
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
zip_filename = os.path.join(backup_dir, f"backup_{timestamp}.zip")

# Maak zip
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
    for foldername, subfolders, filenames in os.walk(project_dir):
        # Sla de backups folder zelf over om geen recursive zip te maken
        if foldername.startswith(backup_dir):
            continue
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            arcname = os.path.relpath(file_path, project_dir)
            backup_zip.write(file_path, arcname)

print(f"Backup created: {zip_filename}")
