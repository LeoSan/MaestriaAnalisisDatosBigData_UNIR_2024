import os
from PIL import Image

dataset_dir = '/Users/fernando/Documents/DEV/AgenteIA/IAOficina/dataset'
invalid_files = []

for root, dirs, files in os.walk(dataset_dir):
    for file in files:
        if file.startswith('.'): continue
        path = os.path.join(root, file)
        try:
            with Image.open(path) as img:
                img.verify()
        except Exception as e:
            print(f"Invalid image: {path} - {e}")
            invalid_files.append(path)

if not invalid_files:
    print("All scanned images seem valid.")
else:
    print(f"Found {len(invalid_files)} invalid files.")

