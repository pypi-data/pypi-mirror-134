from setuptools import setup, find_packages

VERSION = (1, 4, 17)

# Dynamically calculate the version based on VERSION tuple
if len(VERSION) > 2 and VERSION[2] is not None:
    str_version = "%d.%d.%s" % VERSION[:3]
else:
    str_version = "%d.%d" % VERSION[:2]

version = str_version

setup(
    name = 'djangoplicity-livesettings',
    version = version,
    description = "livesettings",
    long_description = open('README.rst').read(),
    author = 'Bruce Kroeze',
    author_email = 'bruce@ecomsmith.com',
    url = 'https://github.com/djangoplicity/djangoplicity-livesettings.git',
    download_url = 'https://github.com/djangoplicity/djangoplicity-livesettings/archive/refs/tags/1.4.17.tar.gz',
    license = 'New BSD License',
    platforms = ['any'],
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Framework :: Django'],
    packages = find_packages(),
    include_package_data = True,
)
