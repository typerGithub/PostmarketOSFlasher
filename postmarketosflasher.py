import os
from sys import platform
from time import sleep
from tqdm import tqdm

linux = "На какой девайс установить PostmarketOS?"
x = [5]*1000

input(linux)

if linux == "Lenovo A6000":
    if platform == "win32":
        for i in tqdm(x, desc="Downloading Bootloader image"):
            pass
            os.system("curl -O https://github.com/msm8916-mainline/lk2nd/releases/download/0.16.0/lk2nd-msm8916.img")
        for i in tqdm(x, desc="Flashing bootloader"):
            pass
            os.system("fastboot flash:raw boot lk2nd-msm8916.img")
            
        for i in tqdm(x, desc="Downloading Postmarketos"):
            pass
            os.system("curl -O https://images.postmarketos.org/bpo/v24.06/lenovo-a6000/gnome-mobile/20240710-2046/20240710-2046-postmarketOS-v24.06-gnome-mobile-2-lenovo-a6000.img.xz")
        for i in tqdm(x, desc="Unarchiving image"):
            pass
            os.system("unxz --keep 20210202-0502-postmarketOS-edge-plasma-mobile-3.2-samsung-a5lte-mainline-modem.img.xz")
        print("Please power phone in to Ik2nd mode")
for i in tqdm(x, desc="Flashing POSTmarketOS image"):
    pass
    os.system("fastboot flash userdata 20240619-1420-postmarketOS-v24.06-gnome-mobile-2-lenovo-a6000.img")
for i in tqdm(x, desc="Erasing folder system on phone"):
    pass
    os.system("fastboot erase system")
for i in tqdm(x, desc="Rebooting"):
    os.system("fastboot reboot")

if platform == "linux":
        for i in tqdm(x, desc="Downloading Bootloader image"):
            pass
            os.system("curl -O https://github.com/msm8916-mainline/lk2nd/releases/download/0.16.0/lk2nd-msm8916.img")
        for i in tqdm(x, desc="Flashing bootloader"):
            pass
            os.system("fastboot flash:raw boot lk2nd-msm8916.img")
            
        for i in tqdm(x, desc="Downloading Postmarketos"):
            pass
            os.system("curl -O https://images.postmarketos.org/bpo/v24.06/lenovo-a6000/gnome-mobile/20240710-2046/20240710-2046-postmarketOS-v24.06-gnome-mobile-2-lenovo-a6000.img.xz")
        for i in tqdm(x, desc="Unarchiving image"):
            pass
            os.system("unxz --keep 20210202-0502-postmarketOS-edge-plasma-mobile-3.2-samsung-a5lte-mainline-modem.img.xz")
        print("Please power phone in to Ik2nd mode")
for i in tqdm(x, desc="Flashing POSTmarketOS image"):
    pass
    os.system("fastboot flash userdata 20240619-1420-postmarketOS-v24.06-gnome-mobile-2-lenovo-a6000.img")
for i in tqdm(x, desc="Erasing folder system on phone"):
    pass
    os.system("fastboot erase system")
for i in tqdm(x, desc="Rebooting"):
    os.system("fastboot reboot")


