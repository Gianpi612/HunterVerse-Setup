# HunterVerse-Setup

This script automatically sets up **PPSSPP** for HunterVerse multiplayer in Patapon 3.
I made this because I got tired of following the same guide every time I had to set up PPSSPP for HunterVerse in Patapon 3.
If you’ve ever followed a guide and had to change PPSSPP settings, this just does it for you.

## What it does

* Finds your PPSSPP config file
* Applies the correct settings in PPSSPP for HunterVerse
* Lets you choose your nickname

## How to use

1. Download the latest release here
2. Run the script
3. Enter your nickname
4. Done

After that, just follow the OpenVPN guide:
https://hunstermonter.net/directions-pc.php
(this process can't be automatized)

## Source

Clone the repo and run:

```bash
git clone https://github.com/Gianpi612/HunterVerse-Setup.git
cd HunterVerse-Setup
python main.py
```

## Notes

* Don’t use "PPSSPP" as your nickname or you won't be able to connect to hunterverse
* If the config file isn’t found automatically, you’ll be asked to select it manually
