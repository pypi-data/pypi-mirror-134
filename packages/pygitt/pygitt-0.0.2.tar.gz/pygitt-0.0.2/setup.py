from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pygitt',
  version='0.0.2',
  description='A module in pip where you can use git commands',
  long_description='A module in pip where you can use git commands',
  url='',  
  author='Mohammed Daniyal',
  author_email='danides450@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='git', 
  packages=find_packages(),
  install_requires=[''] 
)