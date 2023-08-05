#!/usr/bin/env python

from __future__ import print_function
import sys
from  numpy import *
import pyfits
import matplotlib.pyplot as plt
from plot_functions import *
from task import clipping

def sky_calculation(image, nhist, regs, parphot, nbin, scale, units, 
                    barscale, parr, cent, delta, limt, cmap, cont, outima, 
                    sizeima, vclipping=['no',3,3,3,0,'-']):
     """
     The functions calculates the sky statistics  for given regions on the image

     Parameters
     ----------
      image: str,
          Image name 
      nhist: float,
          Numbers of regions')
      regs: array,
          Regions (xcoord,ycoord,width,heigth,ang)
      parphot: array,
          Phot Paramters (scale ima(1.), texp(1.), csky(0.), zp(0.))')
      nbin: float,
          numbers of bins for histogram (recommended 50)
      scale: float,
          Image scale
      units: str,
          Image unit
      barscale: array,
          Length bar (pix), text, position) or 'none' to no show "
      parr: array,
          (Position north-east, legth arrow, margen axis y) or 'none'" 
      cent: array,
          Image center (cx, cy)
      celta: array,
          Delta image (dx, dy)
      limt: array,
          z1,z2, scale (1 to log, 0 to normal) for each image')
      cmap: str,
          Color map
      cont: array,
          (0,cmin,cmax,cnumb,cor,lab) or (0,no,no,cnumb,cor,lab) or
         (1,n1,n2,...nf,cor or no(cmap),lab) or none 
     outimage: str,
         Ouput image name
     sizeima: array,
         Image size in inch (width,heigth) or 'none' by default")  

     Notes
     -----
     There are 4 option to location '1' left-bottom,  '2' right-bottom,
     '3' right-top, '4' left-top.

     Notation for the option of the contours:
         cmax: maximum nivel intesity  for the contour\n')
         cmin: minimum nivel intesity  for the contour\n')
         cnumb: Number of the contour\n')
         cor: Contour Colors ('k','r','b')\n")
     When then option 1, user choose the contour nivels (n1,n2,n3,...,nf)
     """

     ima_xy, ima_array = callf(image)
         
     for i in arange(nhist):
      
         polyrec = rect(regs[i*5],regs[i*5+1],regs[i*5+2],regs[i*5+3],
                          regs[i*5+4],plotr='no')
     
         iman='r' + str(i+1) + '.png'
         itit='\nReg. ' + str(i+1)
         print (itit)
         print ('=========')
         sk, skyv, imav = calcu(polyrec,ima_xy, ima_array)

         if vclipping[0] == 'yes':
               print ("clipping")  
               tskyv = clipping(skyv,*vclipping[1::])
               skyv  = skyv[~isnan(tskyv)]
                 
         fig = plt.figure()
         ax = fig.add_subplot(111)
         histo(ax, skyv, int(nbin), iman, itit, norm=False)
     
         skymag  = -2.5*log10((sk[-1]-sk[3]*parphot[2])/parphot[1]) + parphot[3]
         skyarea = square(parphot[0])*sk[3]
         skymag2 = (-2.5*log10((sk[-1]-sk[3]*parphot[2])/(skyarea*parphot[1])) +  
                   parphot[3])
         print ("Sky Mag: %s" %(round(skymag,2)))
         print ("Sky Mag^2: %s" %(round(skymag2,2)))
     
         if i==0 : skytot=skyv
         else : skytot=concatenate((skytot,skyv)) 
     
     print ("\nTotal Sky")
     print ("===========")
     print ("\nSky mean total: %s" %(round(mean(skytot),2)))
     print ("Sky median total: %s" %(round(median(skytot),2)))
     print ("Sky standard deviation total: %s" %(round(std(skytot),2)))
     print ("Sky area total: %s"%(len(skytot)))
     print ("Sky Min: %s"%(round(amin(skytot),2)))
     print ("Sky Max: %s"%(round(amax(skytot),2)))
     
     fig = plt.figure()
     ax = fig.add_subplot(111)
     histo(ax, skytot, int(nbin), 'skytot.png', 'ceu total', norm=False) 
     
     if sizeima[0] == 'none':
         fig = plt.figure()         
     else:
         fig = plt.figure(figsize=(float(sizeima[0]), float(sizeima[1])))  
     AX = fig.add_subplot(1, 1, 1)
     
     
     if cent[0] == 0 and cent[1] == 0: 
         cent[0] = ima_array.shape[1]*0.5 
         cent[1] = ima_array.shape[0]*0.5
     
     
     # plot of the sky regions
     for i in arange(nhist):
         r1 = regs[i*5]*scale
         r2 = regs[i*5+1]*scale 
         c1 = cent[0]*scale 
         c2 = cent[1]*scale 
         l  = regs[i*5+2]*scale 
         w  = regs[i*5+3]*scale 
         a  = regs[i*5+4]
         rect(r1-c1, r2-c2, l, w, a, linef='k-', linew=2)
         plt.text(r1-c1,r2-c2+w+w*0.5, 'Reg ' + str(i+1)) 
     
     
     if parr[0] != 'none': 
         zetas(image, delta, scale, parr[0], larrow=parr[1], ny=parr[2], AX=AX)
     
     if barscale[0] != 'none': 
         bar(delta, scale, barscale[0], barscale[1], barscale[2], AX=AX)
     
     figure(image, cent, delta, limt, cmap, units, scale, outima, AX=AX)
