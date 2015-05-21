from setuptools import setup

setup(name='juicypipe',
      version='0.0.1',
      description='Large log file processing library for ltsv/pig',
      author='dwango',
      author_email='',
      url='',
      packages=['juicypipe', 'juicypipe.tools'],
      install_requires=open('requirements.txt').read().splitlines(),
      entry_points="""
      [console_scripts]
      pig2sqlite = juicypipe.tools.pig2sqlite:main
      """)
