from setuptools import setup, find_packages

setup(name="ship_messenger_server",
      version="0.8.7",
      description="ship messenger server",
      author="Vladimir Ruzhelovich",
      author_email="Ruzhelovich.Vladimir@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
