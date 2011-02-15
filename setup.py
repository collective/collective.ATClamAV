from setuptools import setup, find_packages

version = '1.1'

setup(name='collective.ATClamAV',
      version=version,
      description="Provides ClamAV antivirus integration for Archetypes based "
          "content types",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
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
          'plone.app.blob',
          'plone.app.controlpanel',
          'plone.app.testing',
          'Products.Archetypes',
          'Products.ATContentTypes',
          'Products.CMFCore',
          'Products.CMFDefault',
          'Products.validation',
          'unittest2',
          'zope.component',
          'zope.formlib',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.schema',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
