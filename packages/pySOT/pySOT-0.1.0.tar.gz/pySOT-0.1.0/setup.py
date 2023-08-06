from setuptools import setup

setup(
    name='pySOT',
    version='0.1.0',
    packages=['pySOT','pySOT.test'],
    url='http://pypi.python.org/pypi/pySOT/',
    license='LICENSE.txt',
    author='David Bindel, David Eriksson',
    author_email='bindel@cornell.edu, dme65@cornell.edu',
    description='Surrogate Optimization Toolbox',
    install_requires=['pyDOE', 'pyKriging', 'POAP'],
    classifiers=[
        'Programming Language :: Python :: 2.7',  
    ],
)
