from setuptools import setup
from ceres import __version__

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='ceres-nav',
      version=__version__,
      long_description=long_description,
      long_description_content_type='text/markdown',
      description='Celestial Estimation for Research, Exploration, and Science',
      author='Chris Gnam',
      author_email='crgnam@buffalo.edu',
      license='MIT',
      download_url='https://pypi.org/project/ceres-nav/',
      url='https://ceresnavigation.org/',
      packages=['ceres','ceres.constants','ceres.objects','ceres.models','ceres.models.gravity'],
      project_urls={
        'Source': 'https://github.com/ceres-navigation/ceres',
        'Documentation': 'https://docs.ceresnavigation.org/',
        'Bug Reports': 'https://github.com/ceres-navigation/ceres/issues'
      },
      install_requires=[
          'numpy'
      ]
     )
