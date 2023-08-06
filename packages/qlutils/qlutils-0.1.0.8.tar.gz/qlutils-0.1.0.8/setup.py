from setuptools import setup, find_packages

setup(name='qlutils',
      packages=find_packages(),
      version='0.1.0.8',
      author='Victor Polevoy',
      author_email='contact@vpolevoy.com',
      url='https://bitbucket.org/fx_/qlutils',
      install_requires=['qllauncher'],
      description='QuakeLive Utilities.',
      entry_points = {
          'console_scripts': [
              'qllserver = qlutils.qllserver:main',
          ],              
      },
      )
