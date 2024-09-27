from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_project',
    packages=find_packages(),
    install_requires=[
        'Flask>=1.0,<4.0',
        'flask-migrate>=4.0.7',
        'flask-sqlalchemy>=3.1.1',
        'flask-jwt-extended>=4.1.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)