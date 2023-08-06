"""Spawn your personal website."""

import pathlib
import subprocess
import sys
import textwrap
import webbrowser

import canopy
import gunicorn.app.base
from PySide6.QtCore import Slot
from PySide6.QtGui import QAction, QFont, QIcon
from PySide6.QtWidgets import (QApplication, QLabel, QMenu, QPushButton,
                               QSystemTrayIcon, QWidget)
from understory import web

port = 9090
tor_browser_base_url = "https://www.torproject.org/dist/torbrowser/11.0.4/"
tor_browser_archive_name = "tor-browser-linux64-11.0.4_en-US.tar.xz"


def main(port, data_dir="gaea_data"):
    """Install the canopy locally, spawn it at an onion and open it in Tor Browser."""
    data_dir = pathlib.Path(data_dir)
    data_dir.mkdir(exist_ok=True)
    archive = data_dir / tor_browser_archive_name
    onion_dir = data_dir / "onion"
    mozilla_path = f"{data_dir}/tor-browser_en-US/Browser/firefox"
    webbrowser.register("firefox", None, webbrowser.BackgroundBrowser(mozilla_path))

    @Slot()
    def install():
        if archive.exists():
            print("already installed!")
            return
        web.download(f"{tor_browser_base_url}/{tor_browser_archive_name}", archive)
        subprocess.run(["tar", "xf", tor_browser_archive_name], cwd=data_dir)
        browser_dir = data_dir / "tor-browser_en-US/Browser/TorBrowser"
        tor_data_dir = browser_dir / "Data/Tor"
        with (browser_dir / "Data/Browser/profile.default/user.js").open("w") as fp:
            fp.write(
                textwrap.dedent(
                    """
                    user_pref("torbrowser.settings.bridges.enabled", false);
                    user_pref("torbrowser.settings.enabled", true);
                    user_pref("torbrowser.settings.firewall.enabled", false);
                    user_pref("torbrowser.settings.proxy.enabled", false);
                    user_pref("torbrowser.settings.quickstart.enabled", true);
                    """
                )
            )
        try:
            onion_dir.mkdir(0o700)
        except FileExistsError:
            pass
        else:
            with (tor_data_dir / "torrc").open("a") as fp:
                fp.write(
                    textwrap.dedent(
                        f"""
                        HiddenServiceDir {onion_dir}
                        HiddenServiceVersion 3
                        HiddenServicePort 80 127.0.0.1:{port}
                        """
                    )
                )
        webbrowser.get("firefox").open("http://check.torproject.org")
        install_button.hide()
        label = QLabel(window)
        label.setText("Installation is complete. Use the icon in your system tray.")
        label.move(10, 10)
        label.show()

    server = None

    @Slot()
    def show_tree():
        if onion := get_onion():
            nonlocal server
            server = subprocess.Popen(
                ["poetry", "run", "python", "-m", "gaea", str(port)]
            )
            webbrowser.get("firefox").open(f"http://{onion}")
        else:
            print("You must `Install` before you `Show` your site.")

    @Slot()
    def shut_down():
        if server:
            server.kill()
        app.quit()

    def get_onion():
        try:
            with (onion_dir / "hostname").open() as fp:
                return fp.read()
        except FileNotFoundError:
            return None

    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
    icon = QIcon("icon.png")
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
    menu = QMenu()

    if not get_onion():
        window = QWidget()
        window.setFont(QFont("Arial", 10))
        window.setGeometry(400, 400, 250, 250)
        window.setWindowTitle("Gaea")
        window.setWindowIcon(icon)
        install_button = QPushButton(window)
        install_button.setText("Install Canopy")
        install_button.clicked.connect(install)
        install_button.move(10, 10)
        window.show()

    show = QAction("Show Site")
    show.triggered.connect(show_tree)
    menu.addAction(show)
    quit = QAction("Quit")
    quit.triggered.connect(shut_down)
    menu.addAction(quit)
    tray.setContextMenu(menu)

    print(f"app.exec() -> {app.exec()}")
    return 0


class StandaloneCanopy(gunicorn.app.base.BaseApplication):
    """A standalone gunicorn webapp context for the canopy."""

    def __init__(self, port):
        self.options = {"bind": f"localhost:{port}", "workers": 2}
        self.application = canopy.app
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
    except IndexError:
        pass
    else:
        StandaloneCanopy(port).run()
    try:
        sys.exit(main(port))
    except KeyboardInterrupt:
        sys.exit()
