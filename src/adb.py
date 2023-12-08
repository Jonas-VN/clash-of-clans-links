import subprocess

class Adb:
    def __init__(self, ip: str, adb_path: str) -> None:
        self.ip = ip
        self.adb_path = adb_path

    def connect(self) -> bool:
        output = subprocess.check_output([self.adb_path, "connect", self.ip])
        if not f"connected to {self.ip}" in output.decode("utf-8").strip():
            return False
        return True

    def send_link(self, link: str) -> None:
        subprocess.run([self.adb_path, "-s", self.ip, "shell", "am", "start", "-a", "android.intent.action.VIEW", "-d", link],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
