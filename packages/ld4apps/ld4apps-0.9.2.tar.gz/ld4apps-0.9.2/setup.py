from setuptools import setup

setup(
    name='ld4apps',
    version='0.9.2',
    description='Linked Data for Applications Server Library',
    long_description='Python library for Linked Data for Applications (LDA). See http://ld4apps.github.io/.',
    author='LD4Apps Team',
    author_email='frankb@ca.ibm.com',
    url='http://pypi.python.org/pypi/ld4apps/',
    packages=['ld4apps', 'ld4apps.mongodbstorage', 'ld4apps.test'],
    install_requires=['requests==2.2.1',
                      'python-dateutil==2.2',
                      'PyJWT==0.2.1',
                      'webob==1.4',
                      #'pycrypto==2.6.1',
                      'pymongo==2.7',
                      'isodate==0.5.0',
                      'rdflib==4.2.0',
                      'rdflib-jsonld==0.2',
                      'werkzeug==0.9.4'
                      ],
    license='Apache Software License',
    platforms='any'
)