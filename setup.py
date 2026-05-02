import subprocess
import sys


def install_requirements():
    print("Checking and installing required libraries...")
    try:
        # Upgrades pip and installs speedtest-cli
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip"]
        )
        subprocess.check_call([sys.executable, "-m", "pip", "install", "speedtest-cli"])
        print("\n[SUCCESS] Environment is set up correctly.")
    except Exception as e:
        print(f"\n[ERROR] Failed to install dependencies: {e}")


if __name__ == "__main__":
    install_requirements()
