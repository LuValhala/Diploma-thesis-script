1.	import arcpy
2.	from arcpy.sa import *
3.	import numpy as np
4.	import math
5.	arcpy.env.workspace = r"C:/test" 
6.	dtm = "dtm" 
7.	vstupmin=FocalStatistics(dtm,NbrCircle(30000,"MAP"), "MINIMUM", "DATA")
8.	minimum = arcpy.RasterToNumPyArray(vstupmin)
9.	vstupmax=FocalStatistics(dtm,NbrCircle(30000,"MAP"), "MAXIMUM", "DATA")
10.	maximum = arcpy.RasterToNumPyArray(vstupmax)
11.	array = arcpy.RasterToNumPyArray(dtm)              
12.	velkost = array.shape                                            
13.	x=velkost[0]
14.	y=velkost[1]
15.	dsc = arcpy.Describe(dtm)
16.	SR = dsc.SpatialReference
17.	ext = dsc.Extent
18.	lower_left = arcpy.Point(ext.XMin,ext.YMin)
19.	arcpy.env.outCoordinateSystem = SR
20.	noDataValue = dsc.noDataValue
21.	a = np.zeros((x, y))
22.	for i in range(0,x):
23.	  for j in range(0,y): 
24.	    if math.fabs(maximum[i,j] - array[i,j]) != 0:
25.	      a[i,j] = float(math.fabs(array[i,j] - minimum[i,j])) / float(math.fabs(maximum[i,j] - array[i,j]))
26.	    else:
27.	      a[i,j] = -1
28.	raster = arcpy.NumPyArrayToRaster (a, lower_left, dsc.meanCellWidth, dsc.meanCellHeight,noDataValue)
29.	raster.save("RP_30")
30.	del raster
31.	del raster
