from setuptools import setup, find_packages
from typing import List

FILEPATH = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements(filepath:str)->List[str]:
    requirements = []
    with open(filepath) as file_object:
        requirements = file_object.readlines()
        requirements =[i.replace("\n","") for i in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        # return requirements


# print(get_requirements(filepath))

setup( 
    name='MLOps_End_To_End_Project', 
    version='0.0.1', 
    description='Machine Learning Operations end to end project', 
    author='Moududur Shamim', 
    author_email='sfgrahman35@gmail.com', 
    url="https://github.com/sfgrahman",
    packages=find_packages(), 
    install_requires=get_requirements(FILEPATH),
) 