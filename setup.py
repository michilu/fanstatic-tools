from setuptools import setup

setup(
    name='fanstatic-tools',
    version='0.1',
    description="fanstatic tools",
    classifiers=[],
    keywords='',
    author='ENDOH takanao',
    long_description=open('README.rst').read(),
    license='BSD',
    url='http://fanstatic.org',
    packages=['fanstatic'],
    py_modules=['mkfanstaticsymlink'],
    entry_points={
      'console_scripts': [
        'mkfanstaticsymlink = mkfanstaticsymlink:main',
        ]
    },
    zip_safe=False,
)
