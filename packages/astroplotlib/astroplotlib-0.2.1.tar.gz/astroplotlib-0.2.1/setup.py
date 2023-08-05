from distutils.core import setup 

setup(name='astroplotlib',                                                      
      version='0.2.1',                                                            
      description='Utilities to handle astronomy data (images, cube, etc).',     
      author='J. A. Hernandez-Jimenez',                                          
      author_email='hernandez.jimenez@ufrgs.br',                                 
      packages=['plot_functions', 'plot_slit', 'plot_ellipse', 'cata', 'sky'],
      scripts = ['scripts/guicata.py', 'scripts/calculate_sky.py', 
                 'scripts/mag.sh', 'scripts/guiregions.py', 'scripts/slit.py',
                 'scripts/calibration.py', 'scripts/guiellipse.py', 
                 'scripts/elme_images.py']
      )           
