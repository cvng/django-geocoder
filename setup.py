from django_geocoder import __version__
from setuptools import setup, find_packages

version_str = ".".join(str(n) for n in __version__)

requires = ['django>=1.8', 'geocoder==1.15.1']

setup(name='django-geocoder',
      version=version_str,
      description='Python geocoder wrapper for Django, inspired by Ruby geocoder.',
      url='https://github.com/cvng/django-geocoder',
      author='cvng',
      author_email='mail@cvng.io',
      license='MIT',
      packages=find_packages(),
      install_requires=requires,
      zip_safe=False,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          "Framework :: Django",
      ])
