from setuptools import setup, find_packages

setup(name="message_server_xBarbarian",
      version="0.6.7",
      description="message_server_xBarbarian",
      author="Ivan Ivanov",
      author_email="test@test.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
