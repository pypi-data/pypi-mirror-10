import re
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

version = ''

with open('schematec/contrib/__init__.py', 'r') as fd:
    regex = re.compile(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]')
    for line in fd:
        m = regex.match(line)
        if m:
            version = m.group(1)
            break

setup(
    name='schematec.contrib',
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    version=version,
    description='Schematec contrib package',
    author='Andrey Gubarev',
    author_email='mylokin@me.com',
    url='https://github.com/mylokin/schematec.contrib',
    keywords=['schema'],
    license='MIT',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
        'Topic :: Database :: Database Engines/Servers',
    ),
    namespace_packages=['schematec', 'schematec.contrib'],
)
