

from setuptools import setup, find_packages


setup(name='docpkg',
      use_scm_version = True,
      author='Ian Good',
      author_email='icgood@gmail.com',
      packages=find_packages(),
      setup_requires=[
          "setuptools_scm"
          ]
)


# vim:et:fdm=marker:sts=4:sw=4:ts=4
