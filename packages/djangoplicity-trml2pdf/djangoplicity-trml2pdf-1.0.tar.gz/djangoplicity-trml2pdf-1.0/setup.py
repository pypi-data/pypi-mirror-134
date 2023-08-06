
from distutils.core import setup
setup(name="djangoplicity-trml2pdf",
      version="1.0",
      author="Fabien Pinckaers",
      author_email="fp@tiny.be",
      license="LGPL",
      description="Tiny RML2PDF is a tool to easily create PDF document without programming.",
      long_description = open('README.rst').read(),
      url = 'https://github.com/djangoplicity/djangoplicity-trml2pdf',
      download_url = 'https://github.com/djangoplicity/djangoplicity-trml2pdf/archive/refs/tags/1.0.tar.gz',
      packages = ['trml2pdf'],
      package_dir = {'trml2pdf': 'trml2pdf'}
     )
