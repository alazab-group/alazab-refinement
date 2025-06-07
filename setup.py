from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in alazab_refinement/__init__.py
from alazab_refinement import __version__ as version

setup(
    name="alazab-refinement",
    version=version,
    description="Al-Azab Construction Template Refinement for Frappe",
    author="Al-Azab Construction Company",
    author_email="admin@alazab.online",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
