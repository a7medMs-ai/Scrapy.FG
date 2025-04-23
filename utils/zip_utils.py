import zipfile
import os

def zip_html_folder(folder_path="html_pages", output_zip_path="exports/html_pages.zip"):
    os.makedirs(os.path.dirname(output_zip_path), exist_ok=True)

    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".html"):
                    full_path = os.path.join(root, file)
                    arcname = os.path.relpath(full_path, folder_path)
                    zipf.write(full_path, arcname=arcname)
