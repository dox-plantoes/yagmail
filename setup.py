from setuptools import setup
import sh
# run updater like: python setup.py sdist bdist_wininst upload

try:
    MAJOR_VERSION = '0'
    MINOR_VERSION = '3'
    MICRO_VERSION = sh.git('rev-list', ['--all']).count('\n')
    VERSION = "{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION)
    with open('VERSION', 'w') as f: 
        f.write(VERSION)
except sh.ErrorReturnCode_128:
    with open('VERSION') as f: 
        VERSION = f.read().strip()

setup(name = 'yagmail',
      version = VERSION,
      description = 'Yet Another GMAIL client',
      url = 'https://github.com/kootenpv/yagmail',
      author = 'Pascal van Kooten',
      author_email = 'kootenpv@gmail.com',
      license = 'GPL',
      packages = ['yagmail'],
      install_requires = [ 
          'keyring',
      ],
      entry_points = { 
          'console_scripts': ['yagmail = yagmail.yagmail:main'] 
          },
      zip_safe = False)
