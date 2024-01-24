from setuptools import setup 
  
setup( 
    name='reversing_tabletop', 
    version='0.1', 
    description='A python package to extract and format tabletop simulator assets onto A4 pages for print and play', 
    author='Ido Koren', 
    author_email='2003idodo@gmail.com', 
    packages=['reversing_tabletop'], 
    install_requires=[ 
        'pillow',
    ], 
) 