from setuptools import setup

setup(
    name='sportyfin',
    version='0.1.4',
    author='Axel Mierczuk',
    author_email='axelmierczuk@gmail.com',
    packages=['sportyfin', 'sportyfin.util'],
    scripts=[],
    url='http://pypi.python.org/pypi/sportyfin/',
    license='LICENSE.txt',
    description='Scrapes popular streaming sites and compiles m3u/xml files for viewing.',
    long_description=open('README.md').read(),
    install_requires=[
        "async-generator",
        "attrs",
        "beautifulsoup4",
        "bs4",
        "certifi",
        "cffi",
        "charset-normalizer",
        "chromedriver-binary",
        "cryptography",
        "h11",
        "idna",
        "lxml",
        "outcome",
        "Pillow",
        "pycparser",
        "pyOpenSSL",
        "python-dotenv",
        "regex",
        "requests",
        "selenium",
        "six",
        "sniffio",
        "sortedcontainers",
        "soupsieve",
        "trio",
        "trio-websocket",
        "urllib3",
        "wsproto",
        "ruamel_yaml"
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.9',
    ],
)
