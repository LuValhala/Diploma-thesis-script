1.	import arcpy
2.	from arcpy.sa import * 
3.	import numpy
4.	import math
5.	arcpy.env.workspace = r"C:/test"
6.	dtm = „dtm“
7.	array = arcpy.RasterToNumPyArray(dtm)  
8.	velkost = array.shape                                            
9.	x=velkost[0]
10.	y=velkost[1]
11.	dsc = arcpy.Describe(dtm)
12.	SR = dsc.SpatialReference
13.	ext = dsc.Extent
14.	lower_left = arcpy.Point(ext.XMin,ext.YMin)
15.	arcpy.env.outCoordinateSystem = SR
16.	noDataValue = dsc.noDataValue
17.	FS = "RANGE" 
18.	c = FocalStatistics(dtm,NbrCircle(500,"MAP"),FS,"DATA")   
19.	d0 = arcpy.RasterToNumPyArray(c)
20.	c = FocalStatistics(dtm,NbrCircle(625,"MAP"),FS,"DATA")   
21.	d1 = arcpy.RasterToNumPyArray(c)
22.	c = FocalStatistics(dtm,NbrCircle(750,"MAP"),FS,"DATA")
23.	d2 = arcpy.RasterToNumPyArray(c)   
24.	c = FocalStatistics(dtm,NbrCircle(875,"MAP"),FS,"DATA")   
25.	d3 = arcpy.RasterToNumPyArray(c)
26.	c = FocalStatistics(dtm,NbrCircle(1000,"MAP"),FS,"DATA")
27.	d4 = arcpy.RasterToNumPyArray(c)      
28.	c = FocalStatistics(dtm,NbrCircle(1125,"MAP"),FS,"DATA")   
29.	d5 = arcpy.RasterToNumPyArray(c)
30.	c = FocalStatistics(dtm,NbrCircle(1250,"MAP"),FS,"DATA")   
31.	d6 = arcpy.RasterToNumPyArray(c)      
32.	c = FocalStatistics(dtm,NbrCircle(1375,"MAP"),FS,"DATA")   
33.	d7 = arcpy.RasterToNumPyArray(c)     
34.	c = FocalStatistics(dtm,NbrCircle(1500,"MAP"),FS,"DATA")
35.	d8 = arcpy.RasterToNumPyArray(c)
36.	c = FocalStatistics(dtm,NbrCircle(1625,"MAP"),FS,"DATA")
37.	d9 = arcpy.RasterToNumPyArray(c)
38.	c = FocalStatistics(dtm,NbrCircle(1750,"MAP"),FS,"DATA")
39.	d10 = arcpy.RasterToNumPyArray(c)
40.	c = FocalStatistics(dtm,NbrCircle(1875,"MAP"),FS,"DATA")
41.	d11 = arcpy.RasterToNumPyArray(c)        
42.	c = FocalStatistics(dtm,NbrCircle(2000,"MAP"),FS,"DATA")
43.	d12 = arcpy.RasterToNumPyArray(c)
44.	c = FocalStatistics(dtm,NbrCircle(2125,"MAP"),FS,"DATA")   
45.	d13 = arcpy.RasterToNumPyArray(c)
46.	c = FocalStatistics(dtm,NbrCircle(2250,"MAP"),FS,"DATA")   
47.	d14 = arcpy.RasterToNumPyArray(c)      
48.	c = FocalStatistics(dtm,NbrCircle(2375,"MAP"),FS,"DATA")   
49.	d15 = arcpy.RasterToNumPyArray(c)     
50.	c = FocalStatistics(dtm,NbrCircle(2500,"MAP"),FS,"DATA")
51.	d16 = arcpy.RasterToNumPyArray(c)
52.	c = FocalStatistics(dtm,NbrCircle(2625,"MAP"),FS,"DATA")
53.	d17 = arcpy.RasterToNumPyArray(c)
54.	c = FocalStatistics(dtm,NbrCircle(2750,"MAP"),FS,"DATA")
55.	d18 = arcpy.RasterToNumPyArray(c)
56.	c = FocalStatistics(dtm,NbrCircle(2875,"MAP"),FS,"DATA")
57.	d19 = arcpy.RasterToNumPyArray(c)        
58.	c = FocalStatistics(dtm,NbrCircle(3000,"MAP"),FS,"DATA")
59.	d20 = arcpy.RasterToNumPyArray(c)
60.	del c
61.	a = numpy.zeros((x, y))
62.	e = numpy.zeros((x, y))
63.	zoz = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20]
64.	zoznvelk = [kruhy for kruhy in range(1000, 6250, 250)]
65.	udolnice_VO = "velkost_okna" #raster s hodnotami dĺžky vlny
66.	VO = arcpy.RasterToNumPyArray(udolnice_VO)
67.	for i in range(0,x):
68.	  for j in range(0,y): 
69.	    velkost_kruhu = VO[i,j]
70.	    a[i,j] = zoz[zoznvelk.index(velkost_kruhu)][i,j]
71.	raster = arcpy.NumPyArrayToRaster (a, lower_left, dsc.meanCellWidth, dsc.meanCellHeight,noDataValue) 
72.	raster.save("amplituda")
73.	del raster
