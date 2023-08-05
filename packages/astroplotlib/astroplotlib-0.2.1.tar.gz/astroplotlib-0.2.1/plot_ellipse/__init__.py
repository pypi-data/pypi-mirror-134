#!/usr/bin/env python

import sys, os
import matplotlib.pyplot as plt
from matplotlib.colors import *
import matplotlib as mpl
import numpy as np
from scipy.ndimage import filters
import pyfits                      
from pyraf import iraf 

from plot_functions import figure

def plot_graf(fig, subplot1, vect, parmx, parmy, rads, rads2, scale, units, 
              task, taskerr, cora1='b.', corp1='r.', labely=0, labelx=0, 
              sticky=0, stickx=0, hspace1=0, wspace1=0,gridc='black'):

    labels = {'SMA':'$Semi-major\,axis$', 
              'INTENS':'$Intens$', 'ELLIP':'$\\epsilon$', 
              'PA':'$Position\,Angle\,(degree)$', 'RSMA':'$R^{1/4}$',
              'MAG':'$mag$', 'TFLUX_E':'$Total\,Flux\,inside\,ellipse$',
              'TFLUX_C':'$Total\,flux\,inside\,circle$', 
              'TMAG_E':'$Total\,mag\,inside\,ellipse$',
              'TMAG_C':'$Total\,mag\,inside\,circle$', 
              'NPIX_E':'$Total\,pixels\,inside\,ellipse$', 
              'NPIX_C':'$Total\,pixels\,inside\,circle$',
              'A4':'$A4$', 'B4':'$B4$', 'MAG2':'$mag/arcsec^{2}$',
              'R_eq_E':'$R_{eq}\,of\,ellipse$',
              'R_eq_E_ARC':'$R_{eq}\,of\,ellipse$', 
              'TFLUX_T':'$Total\,flux\,inside\,R_{eq}$',
              'TMAG_T':'$Total\,mag\,inside\,R_{eq}$', 
              'NPIX_T':'$Total\,pixels\,inside\,R_{eq}$', 
              'R_eq_T':'$R_{eq}$','R_eq_T_ARC':'$R_{eq}$',
              'SMA_ARC':'Semi-major axis','SMA_LOG':'$\\log(sma)$'}
    
    # is there error bar?
    try:
        taskerr[parmy]           
        kopen='1'
    except:
        kopen='0'
    
    mpl.rcParams['grid.color']  = gridc  

    ax = fig.add_subplot(subplot1[0],subplot1[1],subplot1[2])

    if hspace1 != '0': 
        plt.subplots_adjust(hspace=float(hspace1))
    if wspace1 != '0': 
        plt.subplots_adjust(wspace=float(wspace1))

    ax.minorticks_on() 

    if parmx == 'RSMA':
        scale = scale**(0.25)

    if kopen=='1':
        ax.errorbar(vect[rads2[0]:rads2[1] + 1:rads2[2], task[parmx]]*scale, 
                    vect[rads2[0]:rads2[1] + 1:rads2[2],task[parmy]], 
                    yerr=vect[rads2[0]:rads2[1] + 1:rads2[2], 
                    task[taskerr[parmy]]], fmt=corp1, ecolor='k')
        ax.errorbar(vect[rads[0]:rads[1] + 1:rads[2], task[parmx]]*scale, 
                    vect[rads[0]:rads[1] + 1:rads[2],task[parmy]], 
                    yerr=vect[rads[0]:rads[1] + 1:rads[2], 
                    task[taskerr[parmy]]], fmt=cora1, ecolor='k')

    else:    
        ax.plot(vect[rads2[0]:rads2[1] + 1:rads2[2],task[parmx]]*scale, 
                vect[rads2[0]:rads2[1] + 1:rads2[2],task[parmy]],corp1)

        ax.plot(vect[rads[0]:rads[1] + 1:rads[2],task[parmx]]*scale, 
                vect[rads[0]:rads[1] + 1:rads[2],task[parmy]], cora1)
    
    if parmy.find('MAG') != -1 and (vect[0,task[parmy]]<vect[1,task[parmy]]):
        plt.ylim(plt.ylim()[::-1])

    ax.grid(True)
    if labely != 0: 
        plt.ylabel(r'%s'%(labels[parmy]))
    if labelx != 0: 
        plt.xlabel(r'%s $(%s)$'%(labels[parmx],units[1]))

    if sticky == 0: 
        plt.setp( ax.get_yticklabels(), visible=False)  
    if stickx == 0: 
        plt.setp( ax.get_xticklabels(), visible=False)



def ellip(image, table, rad, cora, rad2, corp, cent, delta, limt, cmap, elicon, 
          subp, parm, figs, outima, magzp, pixscale, sky, ref, units, 
          szcent=[10,1], azi_prof=['off', 2,'INDEF','INDEF'],ima_fig='on',
          plot_par='on', cent_ref = [0,0], cent_ellip=[0,0], rad_cent='no',
          rad_user='range', cbaropt=0, barinvt='no', 
          cbar=['vertical', 1.0, 0.0, '%.1f'], cbarl=None,
          nivelconts_mag='no', 
          AX1=None):  
  
    """
    Plot the ellipses (and its contours) and the parameters 
    (as like: PA, ellipticity, MAG, etc) fited with the IRAF's task ellip. 
    
    Parameters
    ----------
     
    image : Image to plot
    table : Table binary 
    rad   : range in pixels of the ellipses to plot [radmin,radmax,step]
    cent  : Center of the image in pixels  [x,y] 
    delta : Delta of the image in pixels [dx,dy] 
    limt  : Minimun and maximum image intesity to be mapped and scale of the 
            intensity (normal=0, log=1), [z1,z2,0 or 1] 
    cmap  : Color map and invertion of the color map (normal='0', 
            invertion='1'), ['colormap','0' or '1']
    elicon: Color ellipses, color countours,smoothness,0 no grid or 1 grid, 
            color ellip. centers and symbol: ('r','b','1','7','w+')
    parm  : Parameters to plot [SMA or RSMA or R_eq, MAG, PA]
    outima: Outputs [table (none), image (none), parameters (none) ]"
    magzp : Magnitud point zero 
    pixscale : Pixels scale arcsec
    units : Factor of the scale for the pixels (e.g, 0.5 (arcsec/pix) or 
            0.001(kpc/pix)) , unit scale 
    rad_user: srt,
            'range' when is given rad1, rad2 and step
            'user' the user gives a list of the indexes of the isophotes to plot  
 
    """        
    task = {'SMA':0, 'INTENS':1, 'INT_ERR':2, 'PIX_VAR':3,'RMS':4, 'ELLIP':5, 
            'ELLIP_ERR':6, 'PA':7, 'PA_ERR':8, 'X0':9, 'X0_ERR':10, 'Y0':11, 
            'Y0_ERR':12,'GRAD':13, 'GRAD_ERR':14,'GRAD_R_ERR':15,'RSMA':16, 
            'MAG':17, 'MAG_LERR':18, 'MAG_UERR':19, 'TFLUX_E':20, 'TFLUX_C':21, 
            'TMAG_E':22,'TMAG_C':23,'NPIX_E':24, 'NPIX_C':25,
            'A3':26,'A3_ERR':27, 'B3':28, 'B3_ERR':29, 'A4':30, 'A4_ERR':31, 
            'B4':32, 'B4_ERR':33, 'NDATA':34,'NFLAG':35,     
            'NITER':36, 'STOP':37, 'A_BIG':38, 'SAREA':39, 'MAG2':40, 
            'R_eq_E':41,'R_eq_E_ARC':42,'TFLUX_T':43,'TMAG_T':44, 'NPIX_T':45, 
            'R_eq_T':46,'R_eq_T_ARC':47, 'SMA_ARC':48, 'SMA_LOG':49, 
            'LOG_SMA':50} 
              
    taskerr = {'INTENS':'INT_ERR', 'ELLIP':'ELLIP_ERR', 'PA':'PA_ERR', 
               'X0':'X0_ERR','Y0':'Y0_ERR','GRAD':'GRAD_ERR','MAG':'MAG_LERR',
              'A3':'A3_ERR','B3':'B3_ERR','A4':'A4_ERR','B4':'B4_ERR'}
       
    colors = {'b':'blue', 'g':'green', 'r':'red', 'c':'cyan', 'm':'magenta', 
              'y':'yellow','k':'black','w':'white'}

    ### GRIDS
    #grid.color       :   black   # grid color
    #grid.linestyle   :   :       # dotted
    #grid.linewidth   :   0.5     # in points
    if elicon[0] != 'none' : mpl.rcParams['grid.color']  = colors[elicon[0]]
    mpl.rcParams['grid.linewidth'] =  1     # in points

##  ########### iraf script #############

    if 1==int(os.path.exists('temp.dat')): os.remove('temp.dat')
    iraf.stsdas(motd='no',_doprint=0)
 
    tabletmp="temp.tab"

    os.system("cp %s %s" %(table,tabletmp))
    area = 2.5*(np.log10(pixscale**2))
    oper1 = ("-2.5*log10((INTENS-" + str(sky) + ")/ " + str(ref)+ ") + " + 
             str(magzp) + "+" + str(area))
    iraf.tcal(tabletmp,outcol="MAG2",equals=oper1) 
    oper2 = ("-2.5*log10((INTENS-" + str(sky) + ")/ "+ str(ref)+ ") + " + 
             str(magzp))
    iraf.tcal(tabletmp,outcol="MAG",equals=oper2) 
    oper3 = ("-2.5*log10((TFLUX_E-NPIX_E*" + str(sky) + ")/" + str(ref) + ") + " 
             + str(magzp))
    iraf.tcal(tabletmp,outcol="TMAG_E",equals=oper3) 
    oper4 = ("-2.5*log10((TFLUX_C-NPIX_C*" + str(sky) + ")/" + str(ref) + ") + " 
             + str(magzp))
    iraf.tcal(tabletmp,outcol="TMAG_C",equals=oper4) 
    oper5 = "(NPIX_E/%s)**0.5"%(np.pi)
    iraf.tcal(tabletmp,outcol="R_eq_E",equals=oper5)
    oper6 = "R_eq_E*%s"%(pixscale)
    iraf.tcal(tabletmp,outcol="R_eq_E_ARC",equals=oper6)
    
    
    iraf.tdump(tabletmp, datafil='temp.dat', columns=" ", Stdout=1)
    os.system("sed -i \"s/INDEF/00.00/g\" temp.dat")

    scale  = float(units[0])

    vect=np.loadtxt('temp.dat')
        
    #remove temporaly file
    os.remove('temp.tab')
    os.remove('temp.dat')
    

    #### mag galaxy ##
    ## Load image
    ima    = pyfits.getdata(image)         
    ## Number of isophotes
    #lvec   = len(vect[:,task['INTENS']])  
    ## Vector: total flux inside an isophote nivel     
    #tflux  = np.zeros([lvec])                
    ## Vector: total pixels inside an isophote nivel     
    #ntflux = np.zeros([lvec])                

    #for e in np.arange(lvec):
    #    itflux    = np.where(ima>=vect[e,task['INTENS']])
    #    ntflux[e] = len(itflux[0])
    #    tflux[e]  = np.sum(ima[itflux])

    #print ('hola1')
    ### Adding new columns on 'vect' array ##

    ## 'TFLUX_T'
    #ntflux = np.resize(ntflux,(lvec,1))
    #tflux  = np.resize(tflux,(lvec,1))
    #vect   = np.hstack((vect,tflux)) 

    ## 'TMAG_T'                        
    #mtflux = -2.5*np.log10((tflux-ntflux*sky)/ref)+magzp
    #mtflux = np.resize(mtflux,(lvec,1))
    #vect   = np.hstack((vect,mtflux))                            
 
    ## 'NPIX_T'
    #vect   = np.hstack((vect,ntflux))     
  
    ## 'R_eq_T'
    #rtflux = (ntflux/np.pi)**0.5                                 
    #vect   = np.hstack((vect,rtflux))  

    ## 'R_eq_T_ARC'
    #arcrtflux = rtflux*pixscale
    #vect   = np.hstack((vect,arcrtflux))  

    ## 'SMA_ARC'
    #arcsma = vect[:,task['SMA']]*pixscale
    #arcsma = np.resize(arcsma,(lvec,1))
    #vect   = np.hstack((vect,arcsma))
 
    ## 'SMA_LOG'
    #logsma = np.log10(arcsma)
    #vect   = np.hstack((vect,logsma))
    
    
    if outima[0] != 'none':
        if 1==int(os.path.exists(outima[0]+'2')): os.remove(outima[0]+'2')
        np.savetxt(outima[0],vect,fmt='%1.5f  ')  
        iraf.tcreate(outima[0]+'2', 
                     cdfile='/home/joseaher/Dropbox/work/prog/parm/header', 
                     datafile=outima[0])
    else: 
        np.savetxt('temp1.dat',vect,fmt='%1.5f  ')
        if 1==int(os.path.exists(table+'2')): 
            os.remove(table+'2')
        iraf.tcreate(table+'2', 
                     cdfile='/home/joseaher/Dropbox/work/prog/parm/header', 
                     datafile='temp1.dat')
        os.remove('temp1.dat')
    
    
    ## 'SMA_LOG_SCALE_USER' (LOG_SMA)
    #vect = np.hstack((vect,(np.log10((arcsma/pixscale)*scale))))  
    
    # This option is when is given  custommed radii rather than rad_init,
    #  rad_final, step
    if rad_user == 'range':
        rad[0] = np.where(vect[:,task['SMA']]>=rad[0])[0][0]
        rad[1] = np.where(vect[:,task['SMA']]<=rad[1])[0][-1]

        len_SMA = len(vect[:,task['SMA']])
        print ("Len of SMA array:", len_SMA)
 
        if rad[1] + rad[2] < len_SMA:
            rad_array = np.arange(rad[0], rad[1] + rad[2], rad[2])
        else:
            rad_array = np.arange(rad[0], len_SMA, rad[2])

    else:
        rad_array = np.array(rad)

    rad2[0] = np.where(vect[:,task['SMA']]>=rad2[0])[0][0]
    rad2[1] = np.where(vect[:,task['SMA']]<=rad2[1])[0][-1]

    print ("Radius (position in the array) of fitted ellipses", rad_array[::-1]) 

    # Definition of arrays
    elip   = np.take(vect[:,task['ELLIP']], rad_array)
    pa     = np.take(vect[:,task['PA']], rad_array)
    radmaj = np.take(vect[:,task['SMA']], rad_array)
    X0     = np.take(vect[:,task['X0']], rad_array)
    Y0     = np.take(vect[:,task['Y0']], rad_array)
    nivelconts = np.take(vect[:,task['INTENS']], rad_array)
    if nivelconts_mag == 'yes':
        nivelconts = -2.5*np.log10((nivelconts-sky)/(ref*pixscale)) + magzp

    #nivelconts[0] = 0
   
    if AX1 is None:
        fig1 = plt.figure(1,figsize=(figs[0],figs[1]))
        AX1 = fig1.add_subplot(1, 1, 1)
        AX1.minorticks_on()

    if azi_prof[0] != 'off':
        fig3 = plt.figure(3)
        AX3 = fig3.add_subplot(1, 1, 1)
        AX3.minorticks_on()
        print('information about ellipse-contour azimuthal profile:')
        print('semi-minor axis,  semi-major axis, PA')

    i = 0
    for angle in pa:
        '''
        For initial setup of the ellipse is chosen that the semi-major axis is 
        aligned with positive 'Y' axis, while the semi-minor axis is aligned 
        with positve 'X' axis. The PA increases counterclockwise.

        The dataset of ellipse start conunterclockwise from (-y,0), after 
        follows  (0,+x), (+y,0), (-x,0) up to again (-y,0). 
        '''

        # Semi-minor axis
        semix = radmaj[i]*(1-elip[i])              
        # Semi-major axis 
        semiy = radmaj[i]

        if azi_prof[0] != 'off':
            print(np.round(semix,2), np.round(semiy,2), round(angle,2))

                          
        # array [-semiy, -semiy+step,..., semiy-step,semiy]
        y1 = np.linspace(-semiy,semiy,400) 
        # Repeat the start point to close the ellipse when it is drawn 
        semiy1 = np.array([semiy]) 
        y1 = np.concatenate((y1,semiy1))        
        # Ellipse as function of semimajor axis
        x1 = ((1-(y1**2/semiy**2))*(semix**2))**0.5 

        # Now, creating the semi-ellipse remaining: [semiy,...,0,...,-semiy] 
        # [0,...,-X,...,0]
        invy1 = y1[::-1]   
        x2 = x1*-1.0
        x = np.concatenate((x1,x2))
        y = np.concatenate((y1,invy1))
                                        
        # Ellipse PA 
        alpha = (angle/180.0)*np.pi 

        # Matrix of Transformation
        xp = x*np.cos(alpha) - y*np.sin(alpha)           
        yp = x*np.sin(alpha) + y*np.cos(alpha)

        # Ellipse center      
        x0 = X0[i]-1                     
        y0 = Y0[i]-1     
            
        # Translation of the ellipse into image coordinate system 

        # The reference center (cent_ref) has the 0,0 coordinates of the frame 
        # where will be plotted the ellipse.  The coordinates of reference
        # center have to be given in the same image coordinates systme where the 
        # ellipses were fitted.
        #
        # "cent_ellip" are the equivalent coordinates of cent_ref coordinates 
        #  in the new image coordinate system.  

        if cent_ref[0]==0 and cent_ref[1]==0:
            cent_refx = cent[0]  
            cent_refy = cent[1]
        else:
            cent_refx = cent_ref[0]
            cent_refy = cent_ref[1]

        cx = (x0 - cent_refx + cent_ellip[0])*scale
        cy = (y0 - cent_refy + cent_ellip[1])*scale
        xp = xp*scale + cx  
        yp = yp*scale + cy  

        # plot azimuthal profile of the ellipse-contour
        if azi_prof[0] != 'off':

            step = 360./len(xp)
            offset = azi_prof[1]
            k=1
            colorpa = (['k.','r.','b.','g.','k.'])  
            for  xima, yima in zip(xp,yp):
                AX3.plot(k*step, ima[int(yima+y0+1.5),int(xima+x0+1.5)] + 
                         offset*i, colorpa[i])
                ima[int(yima+y0+1.5),int(xima+x0+1.5)]=np.nan
                k+=1
            AX3.set_xlabel('Degrees')
            AX3.set_ylabel('Intensity')
        
        # Plotting ellipse center
        print (elicon[4], szcent[0], szcent[1])
        AX1.plot(cx, cy, elicon[4], markersize=szcent[0], mew=szcent[1])
        # Plotting  ellipse
        AX1.plot(xp,yp,elicon[0],markersize=2)
 
                        
        i=i+1


    ## plot of the photometric center
    if rad_cent != 'no':

        X0     = np.take(vect[:,task['X0']], rad_cent)
        Y0     = np.take(vect[:,task['Y0']], rad_cent)
        # Ellipse center      
        x0 = X0-1                     
        y0 = Y0-1        
        if cent_ref[0]==0 and cent_ref[1]==0:
            cent_refx = cent[0]  
            cent_refy = cent[1]
        else:
            cent_refx = cent_ref[0]
            cent_refy = cent_ref[1]

        cx = (x0 - cent_refx + cent_ellip[0])*scale
        cy = (y0 - cent_refy + cent_ellip[1])*scale
        xp = xp*scale + cx  
        yp = yp*scale + cy  
        
        #AX1.plot(cx, cy, elicon[1] + elicon[4][1], markersize=szcent[0]*2, mew=szcent[1])

        AX1.plot(cx, cy, elicon[5], markersize=szcent[0]*2, 
                         mew=szcent[1])

   
    ## plot the image and contours and ellipses fitted ##
    
    # off/on of grids
    if elicon[3] == '0': 
        elicon[3]='off'
    else:
        elicon[3]='on'
    
    if azi_prof[0] != 'off':
        print ("the offset between the azimuthal profile curves is:", offset)
        if azi_prof[2] == 'INDEF':    
            miny = np.min(nivelconts) - azi_prof[1]
        else:
            miny = azi_prof[2]
        if azi_prof[3] == 'INDEF':    
            maxy = np.max(nivelconts) + azi_prof[1]
        else:
            maxy = azi_prof[3]
        AX3.set_ylim(miny, maxy)

    if ima_fig == 'on':
        figure(ima, cent, delta, limt, cmap, units[1], scale, outima[1], 
               pgrid=[elicon[3], elicon[0]], bbox='tight', cont=elicon[1], 
               nivels=np.sort(nivelconts), sigmag=float(elicon[2]), 
               contc=elicon[1], AX=AX1, nameaxis=[units[1], units[2]],
               cbaropt=cbaropt, barinvt=barinvt, cbar=cbar, cbarl=cbarl)

    ## plot of the fitted parameters ##
    if plot_par == 'on': 
        fig2 = plt.figure(2, figsize=(figs[2], figs[3]))
        nsub = subp[0]*subp[1]

        for i in range(nsub):
            plot_graf(fig2, (subp[0],subp[1],i+1), vect, parm[i*8], parm[i*8+1], 
                      rads=[rad[0],rad[1],rad[2]], rads2=[rad2[0], rad2[1],
                      rad2[2]], 
                      scale=scale, units=units, task=task, taskerr=taskerr, 
                      cora1=cora, corp1=corp, labely=int(parm[i*8+2]), 
                      labelx=int(parm[i*8+3]), sticky=int(parm[i*8+4]), 
                      stickx=int(parm[i*8+5]), hspace1=parm[i*8+6], 
                      wspace1=parm[i*8+7], gridc='black')

        if outima[-1] != 'none' :
            plt.savefig(outima[2], format=outima[2].split('.')[-1], 
                        bbox_inches='tight')
