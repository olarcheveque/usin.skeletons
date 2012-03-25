from setuptools import setup, find_packages

version = '1.3'
name = 'usin.skeletons'
setup(name=name,
      version=version,
      description="Skeletons used at Usinasite",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='skeleton paster django usinasite',
      author='Olivier Larchev\xc3\xaaque',
      author_email='olivier.larcheveque@gmail.com',
      url='http://pypi.usinasite.com/%s' % name,
      license='GPL',
      namespace_packages = ['usin', ],
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
      usin_django = usin.skeletons.django:DjangoBuildout
      """,
      )
