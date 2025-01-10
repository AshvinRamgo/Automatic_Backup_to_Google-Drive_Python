import os
from drive import MyDrive
from fastapi import FastAPI

app = FastAPI()

@app.post("/upload")
async def upload_all_files(filepath: str):
    my_drive = MyDrive()
    try:
        files = os.listdir(filepath)
    except FileNotFoundError:
        return {
            "status": "failed",
            "message": "Filepath not found."
        }
    except Exception as e:
        return {
            "status": "failed",
            "message": f"An error occurred: {str(e)}"
        }

    # Filter out hidden files
    files = [f for f in files if not f.startswith('.')]
    
    if not files:
        return {
            "status": "failed",
            "message": "No files found."
        }
    
    uploaded_filepaths = [] 
    new_files_created = [] 
    updated_files = []    

    for item in files:
        response = my_drive.upload_file(item, filepath)
        uploaded_filepaths.append(item)
        print(f"Uploaded: {item}")
        
        if "A new File was created" in response["message"]: 
            new_files_created.append(item) 
        elif "Updated File" in response["message"]: 
            updated_files.append(item)

    if not uploaded_filepaths: 
        return { 
          "status": "failed", 
          "message": "No files were uploaded." 
        }

    return {
        "status": "success",
        "message": "Files uploaded successfully",
        "uploaded_files": uploaded_filepaths,
        "new_files_created": new_files_created,
        "updated_files": updated_files
    }
