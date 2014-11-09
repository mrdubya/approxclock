from setuptools import setup

setup(name='approxclock',
      version='0.1',
      description='Report the time, approximately.',
      long_description=open('README.rst').read(),
      url='https://MrDubya@bitbucket.org/MrDubya/approxclock',
      author='Mike Williams',
      author_email='mrmrdubya@gmail.com',
      license='ISC',
      packages=['approxclock'],
      scripts=['bin/approxclock', 'bin/approxclock.bat'],
      include_package_data=True,
      zip_safe=False)
