from setuptools import setup

setup(
    name="my_package",
    install_requires=[
        'numpy',
        'pandas'],
    extras_require={
        'docs': [
            'sphinx >= 1.4',
            'sphinx_rtd_theme']}
)
