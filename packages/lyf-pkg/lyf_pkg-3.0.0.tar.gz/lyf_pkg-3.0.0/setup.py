from distutils.core import setup
from setuptools import find_packages


with open("README.rst","r",encoding='utf-8') as f:
    long_description = f.read()



setup(name='lyf_pkg',
      version='3.0.0',
      description = 'A small example package',
      long_description = long_description,
      author= 'lyf',
      author_email='694153922@qq.com',
      url= 'https://github.com/lyf',
      install_requires = [],
      license='MIT Licenese',
      packages=find_packages(),
      platforms=['all'],
      classifiers=['Programming Language :: Python',
                   'Topic :: Software Development :: Libraries'
                   ],
      )

