from setuptools import setup

long_description = (
    open('README.txt').read()
    + '\n' +
    open('CHANGES.txt').read())

setup(
    name='fanstatic',
    version='0.13dev',
    description="Flexible static resources for web applications.",
    classifiers=[],
    keywords='',
    author='Fanstatic Developers',
    author_email='fanstatic@googlegroups.com',
    long_description=long_description,
    license='BSD',
    url='http://fanstatic.org',
    packages=['fanstatic'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['WebOb'],
    extras_require = dict(
        test=['pytest >= 2.0'],
        ),
    )
