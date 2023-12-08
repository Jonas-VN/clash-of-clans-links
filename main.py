import sys
import argparse
from PyQt5.QtWidgets import QApplication
from src.adb import Adb
from src.gui import Gui


def main(ip: str, adb_path: str) -> None:
    adb = Adb(ip, adb_path)
    success = adb.connect()
    if not success:
        print(f"Could not connect to device with ip {ip} and adb path {adb_path}")
        return

    with QApplication([]) as app:
        gui = Gui(adb)
        sys.exit(app.exec_())


if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument("--ip", help="IP address of the device", required=True)
    argparse.add_argument("--adb", help="Full path to your adb.exe")
    args = argparse.parse_args()
    ip = args.ip
    adb_path = args.adb if args.adb else "adb"
    main(ip, adb_path)