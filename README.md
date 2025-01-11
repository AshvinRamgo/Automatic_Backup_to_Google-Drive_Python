# Google Drive Automatic Backup API

## Description
This project provides a FastAPI-based web API that integrates with the Google Drive API to backup files from your local computer to a specified folder on Google Drive. It utilizes the Google Drive API client library to authenticate users, upload new files, and update existing files in a Google Drive folder.

## Functionalities
1. **Backup Files:** Automatically back up files from a local folder to a specified Google Drive folder.
2. **Authentication:** Uses Google Drive API client library to authenticate users and manage file uploads.
3. **File Management:** Upload new files and update existing files in the Google Drive folder.

## Notes
- The code ignores hidden files in the original folder.
- `filepath` is the path of the folder that contains the files to be backed up on your local device.
- `folder_id` is the ID of the Google Drive folder where you want the backed-up files to be placed.

## Requirements
- Python 3.7 or later
- FastAPI
- Google Drive API client library
- Pip packages: `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`, `google-api-python-client`

The `credentials.json` file can be created by following the steps found at: [Google Drive API Quickstart](https://developers.google.com/drive/api/quickstart/python).

Once created, install the necessary packages:
```
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## Usage
1. **Set up the environment:**
   - Create a `.env` file in the root directory and add your Google Drive API credentials.
   - More notes on how to do this can be found at: [Google Drive API Quickstart](https://developers.google.com/drive/api/quickstart/python)
   - 
2. **Run the API:**
   ```
   fastapi dev main.py
   ```
   
3. **Access the Documentation:**
   - Open your browser and navigate to documentation Server.

4. **Send a POST request:**
   - Send a POST request to the `/upload` endpoint with the `filepath` as a parameter to back up files to your Google Drive folder.

