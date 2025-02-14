import requests
import base64
import os
from dotenv import load_dotenv

# ✅ Load GitHub Token from .env file
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# ✅ GitHub Repository Info
USERNAME = "ganesh2427"
REPO = "images"
BRANCH = "main"

def get_file_sha(file_name):
    """Fetches the SHA of an existing file in the GitHub repo."""
    url = f"https://api.github.com/repos/{USERNAME}/{REPO}/contents/{file_name}"
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:  # File exists
        return response.json()["sha"]
    return None  # File does not exist

def upload_image(file_path):
    """Uploads an image to GitHub and returns the HTTPS link."""
    if not os.path.exists(file_path):
        print("❌ Error: File not found!")
        return None

    file_name = os.path.basename(file_path)
    url = f"https://api.github.com/repos/{USERNAME}/{REPO}/contents/{file_name}"

    with open(file_path, "rb") as file:
        content = base64.b64encode(file.read()).decode()

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    # ✅ Check if file exists and fetch its SHA
    sha = get_file_sha(file_name)
    
    payload = {
        "message": f"Uploading {file_name}",
        "content": content,
        "branch": BRANCH
    }
    
    if sha:  # If file exists, add 'sha' to update
        payload["sha"] = sha

    response = requests.put(url, json=payload, headers=headers)

    if response.status_code in [200, 201]:  # Success
        print(f"✅ Successfully uploaded {file_name}")
        raw_url = f"https://raw.githubusercontent.com/{USERNAME}/{REPO}/{BRANCH}/{file_name}"
        print(f"🔗 Image URL: {raw_url}")
        return raw_url
    else:
        print(f"❌ Failed to upload {file_name}")
        print(response.json())  # Print error details
        return None
