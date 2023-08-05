from setuptools import setup, find_packages


setup(
    name='nuisance_alarms_pypi_medium',
    version='0.1',
    license='MIT',
    author="Ram",
    author_email='Ram@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
        'scikit-learn',
    ],

)
