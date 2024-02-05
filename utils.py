import time
import json
import shutil

def move_file(source_path, output_folder):
    try:
        shutil.move(source_path, output_folder)
    except Exception as e:
        print(f"Error moving file: {e}")

def create_metadata(file_path, output_folder, text):
    try:
        file_name = file_path.split('/')[1]
        metadata = {
            "file": f"{file_name}",
            "created_at": f"{time.time()}",
            "speech": f"{text}",
            "category":""
        }
        base_name = '.'.join(file_name.split('.')[:-1])
        metadata_file_path = f"{output_folder}/{base_name}.json"
        
        with open(metadata_file_path, 'w') as metadata_file:
            json.dump(metadata, metadata_file, indent=2)
        return metadata_file_path
    except Exception as e:
        print(f"Error creating metadata: {e}")