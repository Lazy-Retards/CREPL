from setuptools import setup, find_packages

setup(
    name="c-repl",
    version="0.1",
    packages=find_packages(),
    install_requires=["rich"],
    entry_points={"console_scripts": ["c-repl=c_repl.main:main"]},
)
