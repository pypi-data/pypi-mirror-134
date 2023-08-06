from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='ytdownloader1',
  version='0.0.1',
  description='A ytdownloader1 library',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='sakl Ansari',
  author_email='sakilansari4@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='ytdownloader1', 
  packages=find_packages(),
  install_requires=[''] 
)
