from setuptools import setup

setup(
    name='simplebus',
    version='0.3.2',
    packages=[
        'simplebus',
        'simplebus.transports'],
    url='https://github.com/viniciuschiele/simplebus',
    license='Apache 2.0',
    author='Vinicius Chiele',
    author_email='vinicius.chiele@gmail.com',
    description='A simple message bus for python 3',
    keywords=['simplebus', 'messagebus', 'message bus',
              'messaging', 'queue', 'topic', 'pubsub'],
    install_requires=['simplejson>=3.6.5']
)
