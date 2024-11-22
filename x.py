import zipfile
import os

# Path to the zip file
zip_file_path = "ABBASSI.zip"

# Path to the destination (HOME directory)
home_dir = os.path.expanduser("~")

# Extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(home_dir)

# Delete the zip file after extraction
os.remove(zip_file_path)

print("Extraction complete and the zip file has been deleted successfully.")
