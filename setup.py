from setuptools import setup
import os
 
setup(
    name='exoplasim',
    version='2.0.5',
    packages=['exoplasim',],
    zip_safe=False,
    install_requires=["numpy","netCDF4","matplotlib"],
    include_package_data=True,
    author='Adiv Paradise',
    author_email='paradise.astro@gmail.com',
    license='GNU General Public License',
    url='https://github.com/alphaparrot/ExoPlaSim',
    description='Exoplanet GCM',
    long_description_content_type='text/x-rst',
    long_description=open('README.rst').read(),
    )
