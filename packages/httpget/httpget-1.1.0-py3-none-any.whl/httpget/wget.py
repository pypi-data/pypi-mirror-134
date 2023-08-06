import tqdm
import requests
import os

def wget(url):
    file_name = os.path.basename(url)
    response = requests.get(url, stream=True)
    file_size = int(response.headers["Content-Length"])
    block_size = 1024
    num_bar = int(file_size / block_size)  # KB
    with open(file_name, "wb") as fp:
        for data in tqdm.tqdm(
            response.iter_content(block_size), total=num_bar, unit="KB", leave=True
        ):
            fp.write(data)
