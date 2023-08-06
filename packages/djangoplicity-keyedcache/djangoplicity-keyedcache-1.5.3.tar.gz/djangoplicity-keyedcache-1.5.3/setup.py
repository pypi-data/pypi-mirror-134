from setuptools import setup, find_packages

VERSION = (1, 5, 3)

# Dynamically calculate the version based on VERSION tuple
if len(VERSION)>2 and VERSION[2] is not None:
    str_version = "%d.%d.%s" % VERSION[:3]
else:
    str_version = "%d.%d" % VERSION[:2]

version= str_version

setup(
    name = 'djangoplicity-keyedcache',
    version = version,
    description = "keyedcache",
    long_description = open('README.rst').read(),
    author = 'Bruce Kroeze',
    author_email = 'brucek@ecomsmith.com',
    url = 'https://github.com/djangoplicity/djangoplicity-keyedcache',
    download_url = 'https://github.com/djangoplicity/djangoplicity-keyedcache/archive/refs/tags/1.5.3.tar.gz',
    license = 'New BSD License',
    platforms = ['any'],
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Framework :: Django'],
    packages = find_packages(),
    install_requires = ['django'],  # >=1.4 <1.6
    include_package_data = True,
)
