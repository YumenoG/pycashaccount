from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = [l for l in f.readlines() if l.strip()]

setup(
    name='cashaccount',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points='''
        [console_scripts]
        cashaccount=cashaccount.cli:run
    ''',
)
