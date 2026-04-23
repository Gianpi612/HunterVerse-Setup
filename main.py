import os
from pathlib import Path
import platform
import shutil
import subprocess

# WIP
def install_ppsspp_linux():

    if shutil.which("flatpak"):
        print("using Flatpak...")
        subprocess.run(["flatpak", "install", "-y", "flathub", "org.ppsspp.PPSSPP"])
    else:
        raise EnvironmentError("test")

def get_ppsspp_config():
    system = platform.system()
    # TODO: boot windows and actually check that the config is there

    # WINDOWS
    if system == "Windows":
        windows_default_path = Path(os.environ["USERPROFILE"]) / "Documents/PPSSPP/PSP/SYSTEM/ppsspp.ini"

        if windows_default_path.exists():
            print(f"Found config at {windows_default_path}")
            return windows_default_path

        print(f"couldn't find ppsspp's config automatically at {windows_default_path}.")
        return ask_path()
    
    # LINUX
    if system == "Linux":
        print("Linux OS detected")

        possible_paths = [
            # Flatpak
            Path.home() / ".var/app/org.ppsspp.PPSSPP/config/ppsspp/PSP/SYSTEM/ppsspp.ini",

            # AppImage
            Path.home() / ".config/ppsspp/PSP/SYSTEM/ppsspp.ini",
        ]

        for p in possible_paths:
            if p.exists():
                print(f"Found config at {p}")
                return p

        print("Couldn't find PPSSPP config automatically. Did you open PPSSPP at least once?")
        return ask_path()
        # theorically MacOS is supported: https://hunstermonter.net/directions-mac.php
        # however i can't be bothered to test it since i will be the only one to use this script anyways
        raise OSError("this OS is not supported")

def ask_path():
    while True:
        user_path = input("Manually insert the path to PPSSPP/PSP/SYSTEM/: ").strip()
        path = Path(user_path) / "ppsspp.ini"

        if path.is_file():
            return path

        print("Could not find 'ppsspp.ini' in that folder. Try again.")


file = get_ppsspp_config()
nickname = input("Choose your nickname for hunterverse (obligatory)\n | NOTE: DO NOT USE THE NICKNAME PPSSPP OR YOU WON'T BE ABLE TO CONNECT!\n").strip()
while len(nickname) == 0:
    nickname = input("The nickname must have at least 1 character!\n").strip()

changes = {
    "EnableWlan": "True",
    "EnableAdhocServer": "True",
    "NickName": nickname,
    "PortOffset": "60000",
    "FastMemoryAccess" : "False",
    "proAdhocServer" : "10.42.0.1",
    "AutoLoadSaveState" : "0",
    "EnableCheats" : "False"
}

with open(file) as f:
    lines = f.readlines()

with open(file, "w") as f:
    for line in lines:
        key = line.split(" = ")[0]
        if key in changes:
            f.write(f"{key} = {changes[key]}\n")
        else:
            f.write(line)

print("PPSSPP settings are setup, follow the instruction for openVPN here:\nhttps://hunstermonter.net/directions-pc.php")
