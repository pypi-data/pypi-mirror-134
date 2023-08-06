from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_desc = fh.read()

setup (
    name='re_roll',
    version='0.1.0',
    license='GPL',
    author='Anon TG',
    author_email="justyouraveragejoe@outlook.com",
    packages=find_packages(),
    description="CLI-based random encounter roller for Tabletop RPGs",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/ganelonhb/re-roll",
    install_requires=[
        'argparse>=1.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    entry_points = {
        'console_scripts' : [
            're-roll=re_roll.main:main'
        ],
    },
    python_requires=">=3.9.9"
)
