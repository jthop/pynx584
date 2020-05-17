from setuptools import setup

setup(name='pynx584',
      version='0.7',
      description='NX584/NX8E Interface Library and Server',
      author='Jamie',
      author_email='jh@oil.io',
      url='https://github.com/jthop/pynx584.git',
      packages=['nx584'],
      install_requires=['requests', 'stevedore', 'prettytable', 'pyserial', 'flask'],
      scripts=['nx584_server', 'nx584_client'],
  )
