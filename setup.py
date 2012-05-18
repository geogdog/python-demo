from setuptools import setup, find_packages
import pydemo

setup(
    name = "PythonDemo",
    version = pydemo.__version__,
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'pydemo = pydemo.demo:main',
        ],
    }
)
