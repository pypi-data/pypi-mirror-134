from setuptools import setup  
requirements = ["Pygame==2.1.1","keyboard","pyttsx3"]
setup(name='GRPgraph',
       version='9.11',
       description='small and compact graphick distributions',
       packages=['GRPgraph'],       
       author_email='pvana621@gmail.com', 
       install_requires=requirements,      
       zip_safe=False)