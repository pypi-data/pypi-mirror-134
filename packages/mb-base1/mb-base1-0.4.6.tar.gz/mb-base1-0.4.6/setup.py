import codecs
import os
import re

import setuptools


def find_version(*file_paths):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *file_paths), "r") as fp:
        version_file = fp.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name="mb-base1",
    version=find_version("mb_base1/__init__.py"),
    python_requires=">=3.10",
    packages=["mb_base1"],
    install_requires=[
        "fastapi==0.72.0",
        "Jinja2==3.0.3",
        "aiofiles==0.8.0",
        "itsdangerous==2.0.1",
        "WTForms==3.0.1",
        "python-multipart==0.0.5",
        "uvicorn[standard]==0.17.0",
        "gunicorn==20.1.0",
        "pyTelegramBotAPI==4.3.1",
        "pyee==8.2.2",
        "mb-std~=0.2.0",
    ],
    extras_require={"dev": ["pytest==6.2.5", "pre-commit==2.16.0", "wheel==0.37.1", "twine==3.7.1", "pip-audit==1.1.2"]},
    include_package_data=True,
)
