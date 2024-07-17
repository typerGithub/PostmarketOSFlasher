''' Copyright [postmarketOSFlasher] [Alex]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. '''

''' Это свободная программа: вы можете перераспространять ее и/или изменять ее на условиях Стандартной общественной лицензии GNU в том виде, в каком она была опубликована Фондом свободного программного обеспечения; либо версии 3 лицензии, либо (по вашему выбору) любой более поздней версии.
Эта программа распространяется в надежде, что она будет полезной, но БЕЗО ВСЯКИХ ГАРАНТИЙ; даже без неявной гарантии ТОВАРНОГО ВИДА или ПРИГОДНОСТИ ДЛЯ ОПРЕДЕЛЕННЫХ ЦЕЛЕЙ. Подробнее см. в Стандартной общественной лицензии GNU.
Вы должны были получить копию Стандартной общественной лицензии GNU вместе с этой программой. Если это не так, см. <https://www.gnu.org/licenses/>. '''

''' This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. '''

import os
import apt
from sys import platform
from time import sleep
from tqdm import tqdm

linux = "На какой девайс установить PostmarketOS?"
x = [5]*1000

cache = apt.Cache()

input(linux)

if linux == "Lenovo A6000":
    if platform == "win32":
        for i in tqdm(x, desc="Downloading Bootloader image"):
            os.system("curl -O https://github.com/msm8916-mainline/lk2nd/releases/download/0.16.0/lk2nd-msm8916.img")
        for i in tqdm(x, desc="Flashing bootloader"):
            os.system("fastboot flash:raw boot lk2nd-msm8916.img")
            
        for i in tqdm(x, desc="Downloading Postmarketos"):
            os.system("curl -O https://images.postmarketos.org/bpo/v24.06/lenovo-a6000/gnome-mobile/20240710-2046/20240710-2046-postmarketOS-v24.06-gnome-mobile-2-lenovo-a6000.img.xz")
        for i in tqdm(x, desc="Unarchiving image"):
            os.system("unxz --keep 20240619-1424-postmarketOS-v24.06-phosh-22.3-lenovo-a6000.img")
        print("Please power phone in to Ik2nd mode")
        time.sleep(8)
        for i in tqdm(x, desc="Flashing POSTmarketOS image"):
    os.system("fastboot flash userdata 20240619-1420-postmarketOS-v24.06-gnome-mobile-2-lenovo-a6000.img")
        for i in tqdm(x, desc="Erasing folder system on phone"):
            os.system("fastboot erase system")
        for i in tqdm(x, desc="Rebooting"):
            os.system("fastboot reboot")

if platform == "linux":
        if cache['android-tools-fastboot'].is_installed:
        print "Android tools it's installed"
    else:
        print "Android tools it's NOT installed"
        for i in tqdm(x, desc="Downloading Bootloader image"):
            os.system("curl -O https://github.com/msm8916-mainline/lk2nd/releases/download/0.16.0/lk2nd-msm8916.img")
        for i in tqdm(x, desc="Flashing bootloader"):
            os.system("fastboot flash:raw boot lk2nd-msm8916.img")
            
        for i in tqdm(x, desc="Downloading Postmarketos"):
            os.system("curl -O https://images.postmarketos.org/bpo/v24.06/lenovo-a6000/gnome-mobile/20240710-2046/20240710-2046-postmarketOS-v24.06-gnome-mobile-2-lenovo-a6000.img.xz")
        for i in tqdm(x, desc="Unarchiving image"):
            os.system("unxz --keep 20210202-0502-postmarketOS-edge-plasma-mobile-3.2-samsung-a5lte-mainline-modem.img.xz")
        print("Please power phone in to Ik2nd mode")
        time.sleep(8)
        for i in tqdm(x, desc="Flashing POSTmarketOS image"):
            os.system("fastboot flash userdata 20240619-1420-postmarketOS-v24.06-gnome-mobile-2-lenovo-a6000.img")
        for i in tqdm(x, desc="Erasing folder system on phone"):
            os.system("fastboot erase system")
        for i in tqdm(x, desc="Rebooting"):
            os.system("fastboot reboot")


