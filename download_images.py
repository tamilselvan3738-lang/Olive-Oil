import urllib.request
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

images = {
    "bal_aged.png": "barrel",
    "bal_white1.png": "vinegar",
    "bal_white2.png": "salad",
    "bal_fruit_main.png": "fruit",
    "bal_fruit_fig.png": "fig",
    "bal_fruit_berry.png": "raspberry",
    "bal_specialty.png": "truffle",
    "bal_reserve_bottle.png": "bottle",
    "bal_fav_fig.png": "fig",
    "bal_fav_peach.png": "peach",
    "bal_fav_garlic.png": "garlic",
    "bal_giftset.png": "gift"
}

images_dir = "d:/Projects/olive oil/images"
os.makedirs(images_dir, exist_ok=True)

for filename, keyword in images.items():
    url = f"https://loremflickr.com/800/600/{keyword}"
    filepath = os.path.join(images_dir, filename)
    try:
        print(f"Downloading {filename}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

print("Done downloading placeholders.")
