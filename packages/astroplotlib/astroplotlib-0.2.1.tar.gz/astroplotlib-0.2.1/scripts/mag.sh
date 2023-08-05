#!/bin/bash

echo " "
echo "-the outfile the daophot (file.mag) :"
read inputfile

echo "-What is the image, aperture, outputfile  :"
read image aper outf


#l=$(cat $inputfile | wc -l)


### tipic value for MAG
#lim1=-0.1
#lim2=-0.8
#crit=3

### tipic value for Sharpness
#lim1=0.3
#lim2=0.8
#crit=4
echo "agora vai"

cat $inputfile | gawk 'BEGIN{}
                       {
                        if($1 =='$image')
                          {
                           pass=1;
                           i=0;
                           printf("jjjjjlllll");
                           printf("%g\t%g\t",$2,$3);
                           id=$4;
                          }
                        if(pass==1 && i==1)
                          {
                          printf("jjjjjj");
                          printf("%g\t%g\t",$1,$2);
                          pass=0;
                          }
                        if($1 =='$aper')
                          {
                          printf("%g\t%g\t%g\t%g\t%g\t%g\n",$2,$3,$4,$5,$6,id)    
                          } 
                        if(i==0)
                          {
                          printf("jjjjjjjjjjjjjjjjja"); 
                          i=1;
                          printf("%f",i)
                          } 
                        }'>$outf



# printf("jjjjjj");
#printf("%g\t%g\t",$1,$2);

                       
#if($1 ~ /^'$image'/)   
#printf("%g\t%g\t%g\t%g\t%g\t%g\n",$2,$3,$4,$5,$6,id)                          
#if($1 ~ /^'$aper'/)
#cat all.$inputfile | awk 'BEGIN{}
#                       {
#                        if($'$crit' < '$lim1')
#                          {
#                          printf("%g\t%g\t%g\t%g\n",$1,$2,$3,$4)
#                          }
#                        }'>lower.$inputfile                          

#cat all.$inputfile | awk 'BEGIN{}
#                       {
#                        if(($'$crit'>'$lim1') && ($'$crit'<'$lim2'))
#                          {
#                          printf("%g\t%g\t%g\t%g\n",$1,$2,$3,$4)
#                          }
#                        }'>med.$inputfile                          


#cat all.$inputfile | awk 'BEGIN{}
#                       {
#                        if($'$crit' >'$lim2')
#                          {
#                          printf("%g\t%g\t%g\t%g\n",$1,$2,$3,$4)
#                          }
#                        }'>upper.$inputfile                          
                        
#print the file that contain the input data
#echo "">> find.log
#echo "=========================================">> find.log
#echo "image name: $inputfile ">> find.log
#echo "lim1: $lim1">> find.log
#echo "lim2: $lim2">> find.log
#echo "date:" $(date)>>find.log
#echo "=========================================">> find.log 

#echo ""
#echo "-done-"
#echo ""                        


