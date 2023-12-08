# Clash Of Clans Links

Navigate Clash Of Clans via links sent through Android Debug Bridge (ADB).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Jonas-VN/clash-of-clans-links.git
    cd clash-of-clans-links
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python main.py --ip <device_ip> --adb <path_to_adb_exe>
    ```

    - `--ip`: IP address of the Android device (required).
    - `--adb`: Full path to your ADB executable (optional, only required if ADB is not in this directory or it is not set as a PATH variable).
