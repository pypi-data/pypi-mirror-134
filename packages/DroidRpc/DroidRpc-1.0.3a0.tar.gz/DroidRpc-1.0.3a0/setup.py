from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='DroidRpc',
    url='https://github.com/asklora/DROID-V3.git',
    author='Rede akbar - William',
    author_email='asklora@loratechai.com',
    # Needed to actually package something
    packages=['DroidRpc.modules','DroidRpc.client','DroidRpc.converter'],
    # Needed for dependencies
    install_requires=['grpcio','grpcio-tools'],
    # *strongly* suggested for sharing
    version='1.0.3-alpha',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)