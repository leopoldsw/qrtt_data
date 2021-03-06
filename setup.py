from setuptools import setup, find_packages


setup(name='qrtt_data',
      version='0.0.1',
      description='Datasets for stocks and other financial instruments.',
      url='https://data.qrtt.org',
      download_url = '',
      author='Leopold W.',
      author_email='lsw@lwco.com',
      packages=find_packages(), #exclude=("tests", "tests_dev")
      install_requires=['pandas', 'numpy'],
      )
