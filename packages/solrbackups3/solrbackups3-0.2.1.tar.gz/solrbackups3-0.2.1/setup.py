from setuptools import setup, find_packages

setup(
    name='solrbackups3',
    version='0.2.1',
    url='https://github.com/yegortokmakov/solrbackups3',
    license='MIT',
    author='yegortokmakov',
    author_email='yegor@tokmakov.biz',
    dependency_links=['git+https://github.com/yegortokmakov/solrbackup.git#egg=solrbackup-0.1'],
    install_requires=['solrbackup==0.1'],
    description='S3 backup solution for Solr',
    scripts=['solrbackup-s3'],
    packages=find_packages()
)
