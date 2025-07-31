import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

FIGMA_TOKEN = os.getenv("FIGMA_TOKEN")
FILE_ID = os.getenv("FIGMA_FILE_ID")

headers = {
    "X-Figma-Token": FIGMA_TOKEN
}

url = f"https://api.figma.com/v1/files/{FILE_ID}"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    figma_data = response.json()
    
    # 書き出し先ファイル
    output_path = "figma_file_output.json"
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(figma_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ JSONファイルとして保存しました: {output_path}")
else:
    print("❌ Error:", response.status_code, response.text)