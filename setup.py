from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.ATClamAV',
      version=version,
      description="Provides ClamAV antivirus integration for Archetypes based "
          "content types",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Plone',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
        ],
      keywords='plone antivirus archetypes',
      author='Yiorgis Gozadinos',
      author_email='ggozad@jarn.com',
      url='http://pypi.python.org/pypi/collective.ATClamAV',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      platforms='Any',
      zip_safe=False,
      install_requires=[
          'setuptools',
          'archetypes.schemaextender',
          'plone.app.testing',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
