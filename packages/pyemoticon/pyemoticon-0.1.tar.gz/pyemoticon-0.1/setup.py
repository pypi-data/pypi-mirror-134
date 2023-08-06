from setuptools import setup, find_packages

setup(
    name = "pyemoticon",
    version = "0.1",
    packages = find_packages(),
    install_requires = ["pynput"],
    package_data = {
        "pyemoticon": ["*.json"]
    },

    entry_points = {
        'console_scripts': [
            'pyemoticon = pyemoticon.main:main'
        ]
    }
)