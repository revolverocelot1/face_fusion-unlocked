#!/usr/bin/env python3
import os
import urllib.request
# List of URLs to download
urls = ["https://huggingface.co/uwg/upscaler/resolve/main/Face_Restore/FaceFusion/retinaface_10g.onnx",
        "https://huggingface.co/ninjawick/webui-faceswap-unlocked/resolve/main/simswap_512_unofficial.onnx",
        "https://huggingface.co/ninjawick/webui-faceswap-unlocked/resolve/main/simswap_256.onnx",
        "https://huggingface.co/ninjawick/webui-faceswap-unlocked/resolve/main/inswapper_128_fp16.onnx"]
# Change the current working directory to the destination directory
os.chdir("/home/xlab-app-center/.assets/models")
# Loop through the URLs and download the files
for url in urls:
    # Get the file name from the URL
    file_name = url.split("/")[-1]
    # Download the file and save it locally
    urllib.request.urlretrieve(url, file_name)
# Import the facefusion module
from facefusion import core


if __name__ == '__main__':
    core.cli()
