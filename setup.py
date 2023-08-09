from setuptools import setup

setup(name='approxclock',
      version='0.2',
      description='Report the time, approximately.',
      long_description=open('README.rst').read(),
      url='https://github.org/mrdubya/approxclock.git',
      author='Mike Williams',
      author_email='mrmrdubya@gmail.com',
      license='ISC',
      packages=['approxclock'],
      scripts=['bin/approxclock', 'bin/approxclock.bat'],
      include_package_data=True,
      zip_safe=False)
