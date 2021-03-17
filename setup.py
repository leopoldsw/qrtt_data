from setuptools import setup, find_packages


setup(name='stock_data',
      version='0.0.3',
      description='Datasets for stocks.',
      url='https://data.qrtt.org',
      author='Leopold W.',
      author_email='lsw@lwco.com',
      packages=find_packages(), #exclude=("tests", "tests_dev")
      install_requires=['pandas', 'numpy'],
      )
