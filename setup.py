from setuptools import setup, find_packages

setup(
    name='brooks',
    version='0.1',
    packages=find_packages(),

    # metadata for upload to PyPI
    author='Sixty North AS',
    author_email='rob@sixty-north.com',
    description="A Brooks' Law simulator",
    license='MIT',
    keywords='simulation',
    url='https://github.com/sixty-north/brooks',
    # download_url = '',
    long_description="Tools for simulating the effect of Brooks' Law in "
                     "software development.",
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    platforms='any',
    # setup_requires=[],
    install_requires=[
        'numpy',
        'docopt',
        'matplotlib',
        'pandas',
        'seaborn',
    ],

    # entry_points={
    #     'console_scripts': [
    #         'yapga = yapga.app.main:main',
    #     ],
    # },
)
