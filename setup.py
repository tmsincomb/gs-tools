from setuptools import setup, find_packages

setup(
    name='gs-tools',
    version='0.0.1',
    description='Google Sheet tools with pandas',
    long_description='',
    url='https://github.com/tmsincomb/gs-tools',
    author='Troy Sincomb',
    author_email='troysincomb@gmail.com',
    license='MIT',
    keywords='gspread google sheets pandas gs-tools gs',
    packages=find_packages('interlex_bulk_ingestion'),
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 1 - BETA',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'gspread',
        'pandas',
    ],
    # Not needed, but might be nice to have an example if I need it.
    # entry_points={
    #     'console_scripts': [
    #         'interlex-bulk-ingestion=interlex_bulk_ingestion.interlex_bulk_ingestion:main',
    #     ],
    # },
)