#!/usr/bin/env python3
import os
os.chdir(f"/home/xlab-app-center")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/uwg/upscaler/resolve/main/Face_Restore/FaceFusion/retinaface_10g.onnx -d /home/xlab-app-center/.assets/models -o retinaface_10g.onnx")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ninjawick/webui-faceswap-unlocked/resolve/main/simswap_512_unofficial.onnx -d /home/xlab-app-center/.assets/models -o simswap_512_unofficial.onnx")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ninjawick/webui-faceswap-unlocked/resolve/main/simswap_256.onnx -d /home/xlab-app-center/.assets/models -o simswap_256.onnx")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://huggingface.co/ninjawick/webui-faceswap-unlocked/resolve/main/inswapper_128_fp16.onnx -d /home/xlab-app-center/.assets/models -o inswapper_128_f16.onnx")
from facefusion import core

if __name__ == '__main__':
    core.cli()
