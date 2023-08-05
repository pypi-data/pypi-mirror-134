from setuptools import setup, find_packages, Extension

setup(name='statest',
      version='0.0.1',
      url='https://github.com/ryu577/statest',
      license='MIT',
      author='Rohit Pandey',
      author_email='rohitpandey576@gmail.com',
      description='Statistical estimation.',
      packages=find_packages(exclude=['tests','plots','experiments']),
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      zip_safe=False)
