import os

base_dir = r"C:\Users\a880862\OneDrive - ATOS\Desktop\new proj"

folders = ["csvs", "pngs", "sql_datasets", "model_results"]
for folder in folders:
    os.makedirs(os.path.join(base_dir, folder), exist_ok=True)