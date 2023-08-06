import sys
from setuptools import setup, find_packages

setup(
    name = "djangoplicity-html2text",
    version = "3.200.3",
    description = "Turn HTML into equivalent Markdown-structured text.",
    long_description = open('README.rst').read(),
    author = "Aaron Swartz",
    author_email = "me@aaronsw.com",
    url='https://github.com/djangoplicity/djangoplicity-html2text',
    download_url = 'https://github.com/djangoplicity/djangoplicity-html2text/archive/refs/tags/3.200.3.tar.gz',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2'
    ],
    entry_points="""
    [console_scripts]
    html2text=html2text:main
    """,
    license='GNU GPL 3',
    packages=find_packages(),
    py_modules=['html2text'],
    include_package_data=True,
    zip_safe=False,
)
