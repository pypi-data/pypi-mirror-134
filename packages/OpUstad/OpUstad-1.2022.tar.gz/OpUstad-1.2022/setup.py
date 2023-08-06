import setuptools

requirements = [
    "heroku3==4.2.3",
    "python-decouple==3.4",
    "telethon==1.13.0",
    "cryptg",
    "psycopg2==2.9.1",
    "sqlalchemy==1.3.20",
    "gitpython==3.1.18",
]

setuptools.setup(
    #Here is the module name.
    name="OpUstad",
 
    #version of the module
    version="1.2022",
 
    #Name of Author
    author="Ustad-Op",
 
    #your Email address
    author_email="jtatagaga@gmail.com",
 
    #Small Description about module
    description="OpUstad",
 
  
 
    #Specifying that we are using markdown file for description
    install_requires=requirements,
    #Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/Ustad-Op",
    packages=setuptools.find_packages(),
 
    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
