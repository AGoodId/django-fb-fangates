#!/usr/bin/env python
from distutils.core import setup

setup(name='django-fb-fangates',
      version='0.1',
      description='Django app for creating Facebook Fan Gates to be embedded in Facebook Fan Page Tabs',
      author='AGoodId',
      author_email='teknik@agoodid.se',
      url='http://github.com/AGoodId/django-fb-fangates/',
      packages=['fb_fangates',],
      package_data = {
          'fb_fangates': [
              'static/*',
              'templates/*.html',
              'templates/*/*.html',
          ],
      },
      license='BSD',
      include_package_data = False,
      zip_safe = False,
      classifiers = [
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Environment :: Web Environment',
          'Framework :: Django',
      ],
)
