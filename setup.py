from setuptools import setup

setup(name="Assignment3",
      version="0.1",
      description="Program to switch on and off lights on an LED grid",
      url="",
      author="Fatima Mohamed",
      author_email="fatima.mohamed@ucdconnect.ie",
      license="GPL3",
      packages=['SE2'],
      entry_points={
          'console_scripts':['solve_led=SE2.main:main']
          }
    )