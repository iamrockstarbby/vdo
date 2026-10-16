
import requests
from pathlib import Path
import re
import time

folder = Path.home() / "Desktop" / "Wedding_Dataset" / "Hindu"
folder.mkdir(parents=True, exist_ok=True)

api = "https://commons.wikimedia.org/w/api.php"
headers = {
    "User-Agent": "WeddingDatasetCollector/1.0 (educational project)"
}

session = requests.Session()
session.headers.update(headers)

params = {
    "action": "query",
    "generator": "search",
    "gsrsearch": 'filetype:bitmap "Hindu wedding"',
    "gsrnamespace": 6,
    "gsrlimit": 50,
    "prop": "imageinfo",
    "iiprop": "url|extmetadata",
    "format": "json"
}

data = session.get(api, params=params, timeout=30)
data.raise_for_status()
pages = data.json().get("query", {}).get("pages", {})

count = 0

for page in pages.values():
    if count >= 50:
        break

    info = page.get("imageinfo", [{}])[0]
    url = info.get("url", "")
    if not url:
        continue

    ext = Path(url.split("?")[0]).suffix.lower()
    if ext not in [".jpg", ".jpeg", ".png", ".webp"]:
        continue

    try:
        response = session.get(url, timeout=30)
        response.raise_for_status()

        if len(response.content) < 5000:
            continue

        name = re.sub(r'[<>:"/\\|?*]', "_", page["title"])
        if not name.lower().endswith(ext):
            name += ext

        (folder / name).write_bytes(response.content)
        count += 1

        print(f"Downloaded {count}/50: {name}")
        time.sleep(0.2)

    except requests.RequestException as error:
        print("Skipped:", error)

print(f"Finished: {count} candidate images downloaded.")
print("Please review each image and its license.")
