import os.path
from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

class MyDrive(): 
  def __init__(self): 
    SCOPES = ["https://www.googleapis.com/auth/drive"]
    creds = None
    if os.path.exists("token.json"):
      creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
      token.write(creds.to_json())
    self.service = build("drive", "v3", credentials=creds)

  def list_files(self, page_size=10):
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
    
  def upload_file(self, filename, path):
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
      print(f"A new File was created {file.get('id')}")
    else:
      for file in response.get('files', []):
        update_file = self.service.files().update(
          fileId=file.get('id'),
          media_body=media,
        ).execute()
        print(f'Updated File')

load_dotenv()

def main():
  path = os.getenv('FILE_PATH')
  my_drive = MyDrive()
  files = os.listdir(path)
  for item in files: 
    if not item.startswith('.'): 
      my_drive.upload_file(item, path)
      print(item)

if __name__ == "__main__":
  main()
