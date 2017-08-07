from setuptools import setup, find_packages
from jessie_bot import __version__

setup(
    name='jessie-bot',
    description='Jessie Bot',
    version=__version__,
    packages=["jessie_bot"],
    author = "Kien Pha,",
    author_email = "kien@knncreative.com",
    url = "https://github.com/KNNCreative/jessie-bot",
    include_package_data=True,
    zip_safe=True,
    entry_points={
        "console_scripts": [
            "jessie = jessie_bot.cli:main"
      ]
    },
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
