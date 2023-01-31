from setuptools import find_packages, setup

setup(
    name="iptoken-flask",
    version="0.9.1",
    description="Decorator system for generating and requiring access tokens for your routes in your Flask application.",
    url="https://github.com/romuro-pauliv/IPT-Token",
    author="Rômulo Pauliv",
    author_email="romulopauliv@bk.ru",
    license="BSD 3-Clause License",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['flask', 'PyJWT']
)