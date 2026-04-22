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

        flatpak_path = Path.home() / ".var/app/org.ppsspp.PPSSPP/config/ppsspp/PSP/SYSTEM/ppsspp.ini"

        if flatpak_path.exists():
            print(f"Found config at {flatpak_path}")
            return flatpak_path

        print(f"couldn't find ppsspp's config automatically at {flatpak_path}.")
        return ask_path()

    # theorically MacOS is supported: https://hunstermonter.net/directions-mac.php
    # however i can't be bothered to test it since i will be the only one to use this script anyways
    raise OSError("this OS is not supported")

def ask_path():
    user_path = input("manually insert the path to ppsspp/PSP/SYSTEM/: ").strip()
    path = Path(user_path)

    if not path.exists():
        raise FileNotFoundError("could not find the config file 'ppsspp.ini' in the specified path")

    return path


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
