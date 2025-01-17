import ctypes
import os
import random
import time
import schedule
from datetime import datetime

# Path to the directory containing wallpapers
WALLPAPER_DIRECTORY = "C:\\Path\\To\\Your\\Wallpapers"

# Define the schedule (e.g., change wallpaper every 10 minutes)
CHANGE_INTERVAL = 10  # in minutes

def get_random_wallpaper(directory):
    """Select a random wallpaper from the specified directory."""
    wallpapers = [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    if not wallpapers:
        raise Exception("No wallpapers found in the specified directory.")
    return os.path.join(directory, random.choice(wallpapers))

def set_wallpaper(wallpaper_path):
    """Set the desktop wallpaper to the specified image."""
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 3)

def change_wallpaper():
    """Change the wallpaper at scheduled intervals."""
    try:
        new_wallpaper = get_random_wallpaper(WALLPAPER_DIRECTORY)
        set_wallpaper(new_wallpaper)
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Wallpaper changed to: {new_wallpaper}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main function to initiate the wallpaper changer."""
    schedule.every(CHANGE_INTERVAL).minutes.do(change_wallpaper)
    print("WallpaperChanger is running...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()