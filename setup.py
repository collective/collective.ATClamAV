from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.ATClamAV',
      version=version,
      description="A product  providing ClamAV antivirus integration for AT-based content types",
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
          'Topic :: Software Development :: Libraries :: Python Modules',      
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
      extras_require=dict(
          test=[
            'zope.testing',
            'Products.PloneTestCase',
          ]
      ),
      install_requires=[
          'setuptools',
          'archetypes.schemaextender >=1.0b1'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
