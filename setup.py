from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_qrcode/__init__.py
from frappe_qrcode import __version__ as version

setup(
	name="frappe_qrcode",
	version=version,
	description="Frappe QR Code built by Upeosoft Limited",
	author="Upeosoft Limited",
	author_email="consult@upeosoft.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
