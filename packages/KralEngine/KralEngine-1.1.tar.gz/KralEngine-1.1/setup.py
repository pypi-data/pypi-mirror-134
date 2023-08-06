from setuptools import setup

setup(
    name='KralEngine',
    version='1.1',
    packages=['kralengine'],
    package_dir={"kralengine": "kralengine"},
    url='',
    license='MIT',
    author='thekralgame',
    author_email='mandiracieyuphan@gmail.com',
    description='A game engine based pygame for python',
    install_requires=['pygame', 'reportlab']
)
