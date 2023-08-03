from setuptools import setup, find_packages

setup(name='montecarlo',
      version='1.0',
      url='https://github.com/rachel-holman/',
      description='A Monte Carlo dice game simulator.',
      author='Rachel Holman',
      author_email='dnw9qk@virginia.edu',
      packages = find_packages(),
      install_requires = ['pandas', 'numpy']
     )