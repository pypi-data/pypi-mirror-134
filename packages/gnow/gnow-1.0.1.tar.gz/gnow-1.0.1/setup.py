from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='gnow',
    version='1.0.1',
    description='This command makes it easy to git add / commit /push and auto-increment tagging.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/addshlab/gnow',
    author='addshlab',
    license='MIT',
    keywords='git',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Topic :: Software Development :: Version Control :: Git',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts':[
            'gnow=gnow.command:run',
        ],
    },
)
