import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build, MediaFileUpload
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
import google.auth.exceptions  

SCOPES = ["https://www.googleapis.com/auth/drive"]

class MyDrive():
  def __init__(self):
    creds = None
    if os.path.exists('token.json'):
      creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        try:
          creds.refresh(Request())
        except google.auth.exceptions.RefreshError:
          creds = None
      if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
          token.write(creds.to_json())
    self.service = build('drive', 'v3', credentials=creds)

  def list_files(self, page_size=10):
    try:
      results = (
          self.service.files()
          .list(pageSize=page_size, fields="nextPageToken, files(id, name)")
          .execute()
      )
      items = results.get("files", [])
      if not items:
        print("No files found.")
      else:
        print("Files:")
        for item in items:
          print(f"{item['name']} ({item['id']})")
    except HttpError as error:
      print(f"An error occurred: {error}")

  def upload_file(self, filename, path):
    try:
      folder_id = os.getenv('FOLDER_ID')
      media = MediaFileUpload(os.path.join(path, filename))
      response = self.service.files().list(
        q=f"name='{filename}' and parents='{folder_id}'",
        spaces='drive',
        fields='nextPageToken, files(id,name)',
        pageToken=None
      ).execute()
      if len(response['files']) == 0:
        file_metadata = {
          'name': filename,
          'parents' : [folder_id]
        }
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"A new File was created: {file_metadata.get('name')}")
        return {"message": "A new File was created", "file_name": file_metadata.get('name')}
      else:
        for file in response.get('files', []):
          update_file = self.service.files().update(
            fileId=file.get('id'),
            media_body=media,
          ).execute()
          print(f'Updated File')
          return {"message": "Updated File", "file_name": filename}
    except HttpError as error:
      print(f"An error occurred: {error}")
      return {"message": f"An error occurred: {error}"}

load_dotenv()

