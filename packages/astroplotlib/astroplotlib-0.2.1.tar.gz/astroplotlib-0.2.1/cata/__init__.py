#!/usr/bin/env python

# Import Modules
from __future__ import print_function
import numpy as np
#from matplotlib.pyplot import *

#import matplotlib.pyplot as plt
from plot_functions import *


import pyfits           
from astLib import astWCS
from astLib import astCoords	
from astropy.coordinates import SkyCoord
import cata.query as astrometry 



import matplotlib.pyplot as plt



import matplotlib as mpl
mpl.rcParams['axes.labelsize']   = 15
mpl.rcParams['legend.fontsize']  = 15
mpl.rcParams['xtick.major.size'] = 8
mpl.rcParams['xtick.minor.size'] = 4
mpl.rcParams['ytick.major.size'] = 8
mpl.rcParams['ytick.minor.size'] = 4
mpl.rcParams['xtick.labelsize']  = 15
mpl.rcParams['ytick.labelsize']  = 15

def catalog(image, catalog, r, starpix, cent, delta, limt, cmap, outima, label, 
            scale, units, imasz) :
    '''
    Plot catalogue object on images
     
     Parameters
     ----------
      
     image : file or str,
         name of image (.fits)
     catalogue : file or str
         cataogue name  
     r : float,
         radius in user unit 
     starpix : file or str, default: none,
         print a file with coordinates in WCS (if the user want to) 
     cent : array_like,
         [centx,centy], image center in pixels
     delta : array_like,
         [deltax,deltay], width (delta X) and height (delta Y) of the matrix
         figure.
     limt : array_lile,
         [zmin,zmax,0 or 1], minimum and maximum intensity levels to be 
             displayed. Scale to be used (linear=0 or log=1)
     cmap : dict,
        ['colormap','0' or '1']  Color map 
     outima :  file or str, default : none,
        name of the output file
     label : str-bool,
        1 to put a label in each object 0 to none
     scale : float,
         scale of image stick
     units : str,
         name scale
     *Color maps to use: autumn, bone, cool, copper, flag, gray, hot, hsv, jet, 
                         pink, prism, spring, summer, winter and spectral.
     if you want an inversion of the color map, just use the '_r' sufix, 
     e.g, gray_r
    '''
    wcs=astWCS.WCS(image)
   
 
    
    # option for daofind output
    if catalog[0]=='0':   
        sx, sy = np.loadtxt(catalog[1], unpack=True, 
                            usecols=(int(catalog[2])-1, int(catalog[3])-1))
        print ('\nNumber of the star found : %s \n'%(len(sx)))
     
        # print a file with coordinates in WCS (if the user wants to)
        if starpix != 'none' :
            coorh2wcs = [wcs.pix2wcs(sx[m],sy[m]) for m in range(len(sx))]
            coorh2wcs = np.resize(coorh2wcs,(len(sx),2))
            np.savetxt(starpix, coorh2wcs, fmt='%3.12f')

    # option for a coordinate file in degrees or dd:mm:seg or hr:mm:seg
    if catalog[0]=='1':  
        # Reading 
        lma = np.loadtxt(catalog[1], dtype='string')
        ra  = lma[:, int(catalog[2]) - 1] 
        dec = lma[:, int(catalog[3]) - 1] 

        print(ra[0])
        print(ra[0].find('p'))
        if ra[0].find(':') < 0:
            ra2d   = [float(e) for e in ra]
            dec2d  = [float(e) for e in dec]
        else:
            ra2d   = [astCoords.hms2decimal(e,':') for e in ra]
            dec2d  = [astCoords.dms2decimal(e,':') for e in dec]

        pixima  = [wcs.wcs2pix(ra2d[m], dec2d[m]) for m in range(len(dec2d))]
        pixima  = np.resize(pixima, (len(pixima), 2))
        sx, sy  = np.hsplit(pixima, 2)
     
        # Print a file with the coordinates in pixels 
        if starpix != 'none' :
            lma[:,int(catalog[2])-1] = np.transpose(sx) 
            lma[:,int(catalog[3])-1] = np.transpose(sy) 
            np.savetxt(starpix, lma, '%s', delimiter='\t')
    
    # Option to retrieve the data from a given catalog 
    if catalog[0]=='2':
        coord_obj = SkyCoord.from_name(catalog[1])
        print ("Coordinates (RAC, DEC) of {} : ({}, {})".format(catalog[1], 
               coord_obj.ra.degree,  coord_obj.dec.degree))
        ncatalog = catalog[2]
        # [alpha, delta] in degrees
        position = [coord_obj.ra.degree, coord_obj.dec.degree]
        # [boxsize_alpha, boxsize_delta] in arcmin       
        conesize = [float(catalog[3]), float(catalog[4])]  
        s_join = ','     
        constraint = s_join.join(catalog[5::])
        astrometry.send_query_vizier(catalog[2], position, conesize, 
                                     constraint, catalog[2] + ".vot")
        stars = astrometry.read_votable(catalog[2] + ".vot")
        nstars = len(stars)
        #------ printing information --------------------
         
        print ('') 
        print (nstars," stars downloaded")
        print ('')
        print ("catalog fields:")
        print (stars.dtype.names)         
         
        sx = np.zeros((nstars))
        sy = np.zeros((nstars))
        for m in range(nstars):
            sxy = wcs.wcs2pix(stars['RAJ2000'][m], stars['DEJ2000'][m])
            sx[m] = sxy[0]
            sy[m] = sxy[1]
       
        if starpix != 'none':
            if ncatalog == 'GSC2.3':
                starfile = np.column_stack((stars[ncatalog], sx, sy, 
                                         stars['jmag'], stars['Fmag']))
                headerf = 'ID \t posX \t posY \t Fmag \t Jmag'
            else:
                starfile = np.column_stack((stars['USNO-B1.0'], sx, sy, 
                                         stars['B2mag'], stars['R2mag']))
                headerf = 'ID \t posX \t posY \t Jmag \t Fmag'
            np.savetxt(starpix, starfile, '%s', delimiter='\t', 
                           header=headerf)
              
    # Plot objects
    plt.clf()
    imasz = imasz.split(',')     
    if imasz[0] == 'none':
        fig = plt.figure()         
    else:
        fig = plt.figure(int(imasz[2]),figsize=(float(imasz[0]), 
                         float(imasz[1])))  
    AX = fig.add_subplot(1, 1, 1)

  


    for e in range(len(sx)):
#    for e in range(6):
        circ ((sx[e]-cent[0])*scale,  (sy[e]-cent[1])*scale, 
              float(r[0])*scale, linef=r[1], linew=float(r[2]))
        # label the objects
        if label==1 and e <6:
            plt.annotate(str(e+1), xy=((sx[e]-cent[0])*scale, 
                        (sy[e]-cent[1])*scale),  color=r[1], xycoords='data', 
                         xytext=(float(r[3]),float(r[4])), 
                         textcoords='offset points', 
                         arrowprops=dict(arrowstyle="->",color=r[1]))
    
   
    figure(image, cent, delta, limt, cmap, units, scale, outima, 
           pgrid=[False,'k'], bbox='tight', AX=AX)
    plt.show()
