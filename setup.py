from setuptools import setup, find_packages

setup(
    name='test_bot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'aniso8601==4.0.1',
        'asn1crypto==0.24.0',
        'certifi==2018.11.29',
        'cffi==1.11.5',
        'chardet==3.0.4',
        'Click==7.0',
        'cryptography==2.4.1',
        'envparse==0.2.0',
        'Flask==1.0.2',
        'flask-restplus==0.12.1',
        'idna==2.7',
        'itsdangerous==1.1.0',
        'Jinja2==2.10',
        'jsonschema==2.6.0',
        'MarkupSafe==1.1.0',
        'pycparser==2.19',
        'pyflakes==2.0.0',
        'pyOpenSSL==18.0.0',
        'PySocks==1.6.8',
        'pytz==2018.7',
        'requests==2.20.1',
        'six==1.12.0',
        'urllib3==1.23',
        'Werkzeug==0.14.1',
        'win-inet-pton==1.0.1',
        'wincertstore==0.2',
    ],
    entry_points={
        'console_scripts': [
            'startapp = app.main:run_server'
        ]
    }
)
