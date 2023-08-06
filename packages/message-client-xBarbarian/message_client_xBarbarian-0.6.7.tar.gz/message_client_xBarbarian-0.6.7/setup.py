from setuptools import setup, find_packages

setup(name="message_client_xBarbarian",
      version="0.6.7",
      description="message_client",
      author="Ivan Ivanov",
      author_email="test@test.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
