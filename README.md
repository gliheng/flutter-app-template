# flutter-app-template [![Join Gitter Chat Channel](https://badges.gitter.im/flutter-rs/community.svg)](https://gitter.im/flutter-rs/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


Example app built using flutter-rs.
![screenshot](https://user-images.githubusercontent.com/741807/72479965-2c200580-37f6-11ea-8ddd-b91fa8759c94.png)


- Support Hot reload
- MethodChannel, EventChannel
- Async runtime using tokio
- System dialogs
- Clipboard support
- Cross platform support, Runs on mac, windows, linux
- Support distribution format: (windows NSIS, mac app, mac dmg, linux snap)

# Get Started

## Install requirements

- [Rust](https://www.rust-lang.org/tools/install)

- libglfw:
    - Install on Mac with: `brew install glfw`
    - Install on Debian/Ubuntu with `apt install libglfw3`
    - Install on Arch Linux (AUR) with `pacman -S glfw-x11 glfw-wayland`
- cmake:
    - Install on Mac with: `brew install cmake`
    - Install on Debian/Ubuntu with `apt install cmake`
    - Install on Arch Linux (AUR) with `pacman -S cmake`
    
- [flutter sdk](https://flutter.io)

## Config flutter engine version
flutter-rs need to know your flutter engine version.
You can set this using any of the following methods.
- If you have flutter cli in your PATH, you're set.
- Set FLUTTER_ROOT environment variable to your flutter sdk path
- Set FLUTTER_ENGINE_VERSION environment variable to your engine version

## Clone this repo

    git clone git@github.com:gliheng/flutter-app-template.git flutter-app
    cd flutter-app
    python ./scripts/init.py

## Develop
- To develop with cli hot-reloading, simple run:

    `python ./scripts/run.py`

- To debug using VS Code dart tools:

    Start process using `cargo run`

    Then attach to debugger using
    `flutter attach --debug-uri=DEBUG_URI`

## Distribute
- To build distribution, use:
    `python ./scripts/build.py mac|dmg|nsis|snap`

    **Note:**
    Build scripts are written in python3. Install python depenendencies using `pip3 install -r scripts/requirements.txt`
    Build on Windows require [NSIS3](https://sourceforge.net/projects/nsis/files/NSIS%203/)
