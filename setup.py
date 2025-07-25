
from setuptools import setup, find_packages

setup(
    name='ansi_art',
    version='1.0.0-alpha',
    packages=find_packages(),
    install_requires=[
        'imageio',
        'numpy',
        'pillow',
    ],
    entry_points={
        'console_scripts': [
            'ansi_text=ansi_art.text:main',
            'ansi_image=ansi_art.image:main'
        ]
    }
)
