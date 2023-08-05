from setuptools import setup, find_packages
import os
import sys

requirements = ["bs4", "requests", "lxml"]
if sys.platform == "win32":
    requirements.append("windows-curses")

setup(
    name="bdtheme",
    author="TheAmmiR",
    license="MIT",
    description="Console BeautifulDiscord theme manager",
    version="0.0.1",
    packages=find_packages(
        exclude=["themes", "venv"]),
    install_requires=requirements,
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "bdtheme=bdtheme.src.main:cmd_bdtheme"
        ]
    }
)

os.system("pip3 install ./BeautifulDiscord 2>nul | pip install ./BeautifulDiscord")
