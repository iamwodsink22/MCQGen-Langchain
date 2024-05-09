from setuptools import setup,find_packages
setup(
    name="MCQ_GEN",
    version='1.0.0',
    author="Araksha",
    author_email="arakshapuri22@gmail.com",
    install_requires=['langchain','streamlit','python-dotenv','PyPDF2'],
    packages=find_packages()
)