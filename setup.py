from setuptools import setup, find_packages


setup(name='crawlers_sm',
      version='0.1.0',
      description='Gathering anime data',
      author='Dragan Matesic',
      author_email='dragan.matesic@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      install_requires=['requests', 'bs4', 'lxml', 'html5lib', 'stem', 'psutil', 'pysocks'],
       )
