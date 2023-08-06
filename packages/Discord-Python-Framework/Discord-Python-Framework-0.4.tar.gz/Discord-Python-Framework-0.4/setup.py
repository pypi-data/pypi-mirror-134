from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
     name='Discord-Python-Framework',  
     version='0.4',
     author="Icy Flames",
     author_email="icyflames@gmail.com",
     description="Discord python tools",
     long_description=long_description,
     classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
     ],
)