import os
import uuid

def get_next_filename(folder, original_filename):
    existing_files = os.listdir(folder)
    numbers = [int(f.split('.')[0]) for f in existing_files if f.split('.')[0].isdigit()]
    next_number = max(numbers) + 1 if numbers else 1
    ext = os.path.splitext(original_filename)[1].lower() or '.jpg'
    return f"{next_number}{ext}"
