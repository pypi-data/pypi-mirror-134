
from setuptools import setup
 
setup(
    name='SmileRating',
    packages=['SmileRating'], # Mismo nombre que en la estructura de carpetas de arriba
    version='0.1',
    license='LGPL v3', # La licencia que tenga tu paquete
    description='Smile Rating is a custom Widget for Qt Designer',
    author='RDCH106',
    author_email='pedro13087@gmail.com',
    url='https://github.com/PedroGM80/SmileRating.git', # Usa la URL del repositorio de GitHub
    download_url='https://codeload.github.com/PedroGM80/SmileRating/zip/refs/heads/main', # Te lo explico a continuación
    keywords='custom Widget for Qt Designer', # Palabras que definan tu paquete
    classifiers=['Programming Language :: Python',  # Clasificadores de compatibilidad con versiones de Python para tu paquete
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7']
)