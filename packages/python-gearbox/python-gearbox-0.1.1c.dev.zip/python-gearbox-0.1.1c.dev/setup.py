from setuptools import setup, find_packages

version = '0.1.1c'

setup(
    name='python-gearbox',
    version=version,
    author='Eduardo M. Firvida Donestevez',
    packages=find_packages(),
    include_package_data=True,
    author_email='efirvida@gmail.com',
    description='Python library for gear transmission design',
    install_requires=['numpy>=0.1', 'scipy>=0.1', 'jinja2>=0.1'],
    url='https://github.com/efirvida/python-gearbox',
    download_url='https://github.com/efirvida/python-gearbox/archive/master.zip',
    keywords=['gearbox', 'gear', 'agma', 'iso', 'gear transmission', 'engineering'],
    platforms='any',
    license='MIT',
    zip_safe=False,
    classifiers=['Intended Audience :: Developers',
                 'Intended Audience :: Manufacturing',
                 'Intended Audience :: Science/Research',
                 'Natural Language :: English',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Scientific/Engineering :: Human Machine Interfaces',
                 'Topic :: Software Development',
                 'Topic :: Software Development :: Libraries',
                 ]
)