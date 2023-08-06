"""
Some helpful tools
"""


class Setup:
    def __init__(self, path: str):
        with open(path, 'r+') as setup:
            setup.write("""
from setuptools import setup, find_packages


setup(
    name='UNKnownDB',
    version='1.6.6',
    author='CleaverCreator',
    author_email='liuhanbo333@icloud.com',
    packages=find_packages(),
    zip_safe=False,
    platforms=['Linux'],
    install_requires=['PyQt5'],
    python_requires='>=3.9',
    description=DESCRIPTION,
    long_description=<LONG_DESCRIPTION>,
    license=<LICENSE>,
    url=<URL>,
    classifiers=[],
    scripts=['./start.py']
)

            """)
