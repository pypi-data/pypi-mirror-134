import urllib

def send_query_vizier(catalog, position, conesize, constraint, 
                      filename = 'vizier.xml', text_display=True):

    """
    
    ---------------------
    
    Purpose
    
    Send a query to Vizier and retrieves a list of stars with astrometric 
    (alpha, delta, etc) or photometric (magnitudes, etc) information
    The data is saved in a specific xml file, with VOtable format
    
    The syntax to send a Vizier query is described there: 
    http://vizier.u-strasbg.fr/doc/asu-summary.htx
    
    ---------------------
    
    Inputs
    
    * catalog (string) = name of the catalog, following Vizier syntax
    
    Popular Vizier catalogs include:
    
    'II/294' - Sloan SDSS photometric catalog Release 7 (2009)
    
    '2MASS-PSC' - 2MASS point source catalog (2003)
    
    'GSC2.3' - Version 2.3.2 of the HST Guide Star Catalog (2006)
    
    'USNO-B1' - Verson B1 of the US Naval Observatory catalog (2003)
    
    'NVSS'  - NRAO VLA Sky Survey (1998)
    
    'B/DENIS/DENIS' - 2nd Deep Near Infrared Survey of southern Sky
    
    'I/259/TYC2' - Tycho-2 main catalog (2000)
    
    'I/311/HIP2' - Hipparcos main catalog, new reduction (2007) 
    Each string gives the complete filename (including path) of a 
    file that contains the lightcurve measurements.
    
    * position (string or [float,float]) = position name 
      (resolved by Sesame) or alpha/delta position (in degrees) 
      giving the center of the star field to be requested
    
    * conesize (None, float or [float,float]) = size in arcmin, 
      corresponds 
      to the radius (float) or alpha/delta box rectangular size 
      ([float,float]) defining the star field requested
    
    If equal to None (default), a radius of 5 arcmin is used
    
    * constraint (string) = list of constraints to be applied on the 
      catalogs fields to filter the retrieved stars (Vizier syntax)
    
    For instance: 'B1mag<=13'
    
    Multiple contraints are separated by comma: 'B1mag<13,B2mag<14'
    
    * filename (string) = optional parameter, default is 'vizier.xml'.
    
    Specifies the xml file in which the data from the Vizier request is 
    stored.
    
    It can be a full filename with path information, or a simple filename 
    in which case the active directory is used.
    
    * text_display (boolean) = optional argument. If equal to True 
    (default), some information is written in the console window. If equal 
    to False nothing is written.
    
    ---------------------
    
    Output = no output
    
    ---------------------
    
    """
    
    #------ (1) Preparing url for Vizier ----------------------
    
    cat = "?-source=" + catalog
    
    if isinstance(position,str):   
        obj = "&-c=" + position
    else:
    	obj = ("&-c.ra=" + str(position[0]) + "&-c.dec=" + 
                   str(position[1]))
    
    if conesize==None:
    	dis = "&-c.rm=05"
    
    elif isinstance(conesize,list):
    	dis = "&-c.bm=" + str(conesize[0]) + "/" + str(conesize[1])
    
    else:
    	dis = "&-c.rm=" + str(conesize)
    
    if len(constraint)==0:
    	cons = ""
    
    else:
    	constraint = constraint.replace(" ","")
    	constraint = constraint.replace(",","&")
    	constraint = constraint.replace("<","=%3C")
    	constraint = constraint.replace(">","=%3E")
    	constraint = constraint.replace("+","%2B")
    	constraint = constraint.replace("/","%2F")
    	constraint = constraint.replace("!","=!")
    	cons = "&" + constraint

    #serv = "http://webviz.u-strasbg.fr/viz-bin/votable/"           
    serv = "http://vizier.cfa.harvard.edu/viz-bin/votable/"
    url = (serv + cat + obj + dis + cons + "&-out.max=unlimited")
 
             
    #------ (2) Sending query to Vizier ----------------------    
    if text_display:
    	print
    	print "--- retrieving data from Vizier ---"
        print url
    
    
    fp = urllib.urlopen(url)    
    op = open(filename, "wb")
    
    
    
    while 1:    
    	s = fp.read(8192)
    	if not s:
    	    break
    	op.write(s)
        
    fp.close()
    op.close()

#----------- end of function -----------------------------


# -*- coding: iso_8859_1 -*-



import warnings

import numpy as np

from astropy.io.votable import parse_single_table, parse



def read_votable(filename, ordering = [False,''], remove_duplicates = [False, 
                 []], text_display=True):

	"""

	---------------------

	Purpose

	Read out a xml file with VOtable format, that was obtained with the 
        Vizier or SkyBoT web service

	---------------------

	Inputs

	* filename (string) = specifies the xml file from which the data must 
          be read out.

	It can be a full filename with path information, or a simple filename 
        in which case the active directory is used.

	* ordering (list) = optional parameter, default is [False, '']. If 
          ordering[0] is True, all the astronomical objects contained in the 
          data are ordered in increasing order using the field ordering[1].

	For instance, if ordering = [True, 'B1mag'] then the output data is 
        such that data['B1mag'] is in increasing order.

	* remove_duplicates (list) = optional parameter, default is [False,[]].

	If remove_duplicates[0] is True, then all astronomical objects having 
        two or more occurrences with the same fields remove_duplicates[1][i] 
        (with i=1,..,len(remove_duplicates[1])) are identified and all 
        redundant occurrences are deleted.

	For instance, remove_duplicates = [True, ['RAJ2000', 'DEJ2000']] allows 
        to make sure that we have only one object per (alpha, delta) position.

	* text_display (boolean) = optional argument. If equal to True 
          (default), some information is written in the console window. If 
          equal to False nothing is written.

	---------------------

	Output (Numpy record array) = array that contains all the data. The 
        columns get their names from both the ID and name attributes of the 
        FIELD elements in the VOTABLE file.

	See online help: 
        http://stsdas.stsci.edu/astrolib/vo/html/intro_table.html#using-vo-table

	---------------------

	"""

	#------ (1) Converting votable to Numpy array -----------------

	if text_display:
		print
		print "--- reading existing .xml catalog ---"



	warnings.simplefilter("ignore")
	votable = parse(filename, pedantic=False)
	warnings.resetwarnings() 

	#------ added 17-12-2012 to avoid error with VO.Table saying  "No 
        #        solar system object was found in the requested FOV" ------

	nbtables = 0
	for table in votable.iter_tables():
	    nbtables = 1
	    break
	if nbtables==0:
	    return []

	#------------

	result = votable.get_first_table()
	data = result.array

	#------ (2) Ordering objects -----------------

	if ordering[0]:
		data = data[np.argsort(data[ordering[1]]),:]


	#------ (3) Removing duplicates -----------------

	if remove_duplicates[0]:
            data2 = data[remove_duplicates[1][0]]
            
            for i in range(1,len(remove_duplicates[1])):
                if i==1:
                    data2 = np.vstack([data2, 
                            data[remove_duplicates[1][i]]]).transpose()
                
                else:
            	    data2 = np.vstack([data2.transpose(), 
                            data[remove_duplicates[1][i]]]).transpose()
            
            data2 = np.core.records.fromarrays(list(data2.transpose()))
            
            data2, indices = np.unique(data2, return_index=True)
            
            indices = np.sort(indices)
            
            data = data[indices]
 
	return data
