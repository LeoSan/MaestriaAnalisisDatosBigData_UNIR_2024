import os
import imghdr

dataset_dir = '/Users/fernando/Documents/DEV/AgenteIA/IAOficina/dataset'
invalid_files = []
total_files = 0

for root, dirs, files in os.walk(dataset_dir):
    for file in files:
        if file.startswith('.'): continue
        path = os.path.join(root, file)
        total_files += 1
        
        # Check if the file is a valid image type according to imghdr
        img_type = imghdr.what(path)
        if img_type not in ['jpeg', 'png', 'gif', 'bmp', 'webp']:
            print(f"Invalid image format found: {path} (detected type: {img_type})")
            invalid_files.append(path)

print(f"Total files checked: {total_files}")
if not invalid_files:
    print("All scanned images seem valid according to imghdr.")
else:
    print(f"Found {len(invalid_files)} invalid files.")

