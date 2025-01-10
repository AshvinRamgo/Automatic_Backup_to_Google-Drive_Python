**Google Drive Automatic Backup API**

Description:
This project provides a FastAPI-based web API that integrates with the Google Drive API to backup files from your local computer to a specified folder on Google Drive. It utilizes the Google Drive API client library to authenticate users, upload new files, and update existing files in a Google Drive Folder.

Notes:   
- The code ignores hidden files in the original folder. 
- `filepath` is the path of the folder that contains the files to be backed up on your local device. 
- `folder_id` is the ID of the Google Drive folder where you want the backed-up files to be placed.

Requirements:   
- The credientials.json file can be created by following the steps found https://developers.google.com/drive/api/quickstart/python
- Once created pip3 install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client and edit code to suit
  
Usage:
- Run $fastapi dev main.py
- Click the Documentation Server
- Send a POST request to the `/upload` endpoint with the `filepath` as a parameter to back up files to your Google Drive folder.
