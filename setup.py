from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='usin.skeletons',
      version=version,
      description="Skeletons for projects at Usinasite",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='skeleton paster django usinasite',
      author='Olivier Larchev\xc3\xaaque',
      author_email='olivier.larcheveque@gmail.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'PasteScript >= 1.7.4.2',
          'Cheetah >= 2.4.4',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      usin_django_buildout = usin.skeletons.django:DjangoBuildout
      """,
      )
