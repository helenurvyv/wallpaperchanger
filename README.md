# WallpaperChanger

WallpaperChanger is a Python program that automatically rotates your desktop wallpaper based on a user-defined schedule and a collection of images on your Windows machine.

## Features

- Randomly selects a wallpaper from a specified directory.
- Changes the wallpaper at a user-defined interval (e.g., every 10 minutes).
- Supports common image file formats: `.png`, `.jpg`, `.jpeg`, and `.bmp`.

## Requirements

- Windows operating system.
- Python 3.x.
- `ctypes` and `schedule` Python libraries.

## Installation

1. Ensure you have Python 3.x installed on your Windows machine.
2. Install the `schedule` library if you haven't already:

   ```bash
   pip install schedule
   ```

3. Clone this repository or download the `WallpaperChanger.py` file.

## Usage

1. Update the `WALLPAPER_DIRECTORY` variable in `WallpaperChanger.py` with the path to your wallpaper images.
2. Adjust the `CHANGE_INTERVAL` variable to set how often you want the wallpaper to change (in minutes).
3. Run the script:

   ```bash
   python WallpaperChanger.py
   ```

4. The program will run in the background and change your wallpaper at the specified interval.

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is open-source and available under the MIT License. See the `LICENSE` file for more information.