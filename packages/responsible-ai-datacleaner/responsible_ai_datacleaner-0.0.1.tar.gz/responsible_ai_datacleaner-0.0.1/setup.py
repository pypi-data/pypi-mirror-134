from setuptools import setup, find_packages

setup(
    name='responsible_ai_datacleaner',
    version='0.0.1',
    author='Sem',
    author_email='no@example.com',
    packages=find_packages(),
    url='http://pypi.python.org/pypi/responsible_ai_datacleaner/',
    license='LICENSE.txt',
    description='Package that can clean text for the resp-ai project',
    long_description="Package that can clean text for the resp-ai project",
    install_requires=[
        "nltk",
        "re",
        "preprocessor",
        "pandas",
        "emoji",
    ],
)