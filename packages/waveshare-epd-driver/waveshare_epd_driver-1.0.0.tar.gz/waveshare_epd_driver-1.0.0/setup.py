import sys, os
from setuptools import setup

dependencies = ['Pillow', 'numpy']

if os.path.exists('/sys/bus/platform/drivers/gpiomem-bcm2835'):
    dependencies += ['RPi.GPIO', 'spidev']
else:
    dependencies += ['Jetson.GPIO']

setup(
    name='waveshare_epd_driver',
    description='Waveshare e-Paper Display',
    author='Waveshare',
    version='1.0.0',
    package_dir={'': 'lib'},
    packages=['waveshare_epd_driver'],
    install_requires=dependencies,
)

