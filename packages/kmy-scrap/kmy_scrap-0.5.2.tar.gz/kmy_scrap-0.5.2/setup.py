import os
from setuptools import setup, find_packages

DESCRIPTION = 'apikey search enggine scraping based.'
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(name='kmy_scrap',
      version='0.5.2',
      packages=find_packages(),
      include_package_data=True,
      description=DESCRIPTION,
      long_description=README,
      author='Exso Kamabay',
      author_email='<lexyong66@gmail.com>',
      url='https://github.com/ExsoKamabay/Api-scrap',
      long_description_content_type='text/markdown',
      license='Apache License 2.0',
      install_requires=['bs4', 'requests', 'youtube-search==2.1.0'],
      keywords=['python', 'free', 'apikey', 'apikey scraping based'],
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities',
      ],
      )
