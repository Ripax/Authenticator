import os
import platform
import json
import getpass  # For getting the system username

class AuthFileManager:
    def __init__(self):
        self.system = platform.system()
        self.username = getpass.getuser()  # Get the current system username
        self.auth_path = self._determine_auth_path()
        self.ensure_auth_file()

    def _determine_auth_path(self):
        """Determines the correct path for the .auth file based on OS."""
        if self.system == "Windows":
            auth_dir = os.environ["USERPROFILE"]
        else:  # Linux or macOS (Darwin)
            auth_dir = os.path.join(os.environ["HOME"], "config/authenticator/configs")

        return os.path.join(auth_dir, ".auth")

    def ensure_auth_file(self):
        """Ensures the directory and .auth file exist, and initializes with default JSON if empty."""
        auth_dir = os.path.dirname(self.auth_path)

        # Ensure the directory exists
        if not os.path.exists(auth_dir):
            os.makedirs(auth_dir, exist_ok=True)

        # Ensure the file exists and has default JSON structure
        if not os.path.exists(self.auth_path):
            self._write_default_json()
        else:
            self._ensure_json_structure()

    def _write_default_json(self):
        """Writes the default JSON structure if the file does not exist."""
        default_data = {
            self.username: {
            }
        }
        with open(self.auth_path, "w") as f:
            json.dump(default_data, f, indent=4)

    def _ensure_json_structure(self):
        """Ensures that the existing .auth file contains the necessary structure."""
        try:
            with open(self.auth_path, "r") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = {}  # Reset to empty if file is corrupted

        # Ensure the user section exists
        if self.username not in data:
            data[self.username] = {}

        # # Ensure "appname" exists within the user section
        # if "appname" not in data[self.username]:
        #     data[self.username]["appname"] = ""
        #
        # # Ensure "site" exists within the user section
        # if "site" not in data[self.username]:
        #     data[self.username]["site"] = ""

        # Write back the updated structure
        with open(self.auth_path, "w") as f:
            json.dump(data, f, indent=4)

    def get_auth_path(self):
        """Returns the .auth file path."""
        return self.auth_path

    def load_stylesheet(self, app):
        home_path = os.path.expanduser("~")  # Expands `~` to the user's home directory
        custom_qss = os.path.join(home_path, "config/authenticator/configs", "mainUI.qss")
        default_qss = "ui/qss/mainUI.qss"

        qss_file = custom_qss if os.path.exists(custom_qss) else default_qss

        try:
            with open(qss_file, "r") as file:
                app.setStyleSheet(file.read())
        except Exception as e:
            print(f"Error loading stylesheet: {e}")


if __name__ == '__main__':
    # Example usage
    auth_manager = AuthFileManager()
    print(f"Auth file path: {auth_manager.get_auth_path()}")
