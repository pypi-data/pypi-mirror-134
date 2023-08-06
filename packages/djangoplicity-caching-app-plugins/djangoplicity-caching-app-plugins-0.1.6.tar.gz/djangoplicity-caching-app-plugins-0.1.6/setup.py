from setuptools import setup, find_packages

setup(
    name='djangoplicity-caching-app-plugins',
    version='0.1.6',
    description='',
    long_description = open('README.rst').read(),
    author='Bruce Kroeze',
    author_email='bruce@ecomsmith.com',
    url='https://github.com/djangoplicity/djangoplicity-caching-app-plugins',
    download_url = 'https://github.com/djangoplicity/djangoplicity-caching-app-plugins/archive/refs/tags/0.1.6.tar.gz',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
