**Automatic Backup to Google Drive**

Description:
This Python script provides a simple integration with the Google Drive API to backup files from your local computer to a specified folder on Google Drive. It utilizes the Google Drive API client library to authenticate users, upload new files and update existing files to a Google Drive Folder.

Notes:   
The code ignore hidden files in the orginal folder  
path is the file path of the folder that contains the files to backup on your local device  
folder_id is the ID of the google drive folder that you want the backed up files to be placed  


Requirements:   
- The credientials.json file can be created by following the steps found https://developers.google.com/drive/api/quickstart/python
- Once created pip3 install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client and edit code to suit
  
