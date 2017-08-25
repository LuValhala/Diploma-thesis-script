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
63.	a = a – 1
64.	for i in range(0,x):
65.	  for j in range(0,y):
66.	    if a[i,j] == -1:
67.	      if math.fabs(d2[i,j]* 0.05) >= math.fabs(d2[i,j] – d0[i,j]):
68.	        a[i,j] = d0[i,j]
69.	        e[i,j] = 1000    
70.	      if a[i,j] == -1:
71.	        if math.fabs(d3[i,j]* 0.05) >= math.fabs(d3[i,j] – d1[i,j]):
72.	          a[i,j] = d1[i,j]
73.	          e[i,j] = 1250
74.	        if a[i,j] == -1:
75.	          if math.fabs(d4[i,j]* 0.05) >= math.fabs(d4[i,j] – d2[i,j]):
76.	            a[i,j] = d2[i,j]
77.	            e[i,j] = 1500
78.	          if a[i,j] == -1:
79.	            if math.fabs(d5[i,j]* 0.05) >= math.fabs(d5[i,j] – d3[i,j]):
80.	              a[i,j] = d3[i,j]
81.	              e[i,j] = 1750
82.	            if a[i,j] == -1:
83.	              if math.fabs(d6[i,j]* 0.05) >= math.fabs(d6[i,j] – d4[i,j]):
84.	                a[i,j] = d4[i,j]
85.	                e[i,j] = 2000
86.	              if a[i,j] == -1:
87.	                if math.fabs(d7[i,j]* 0.05) >= math.fabs(d7[i,j] – d5[i,j]):
88.	                  a[i,j] = d5[i,j]
89.	                  e[i,j] = 2250
90.	                if a[i,j] == -1:
91.	                  if math.fabs(d8[i,j]* 0.05) >= math.fabs(d8[i,j] – d6[i,j]):
92.	                    a[i,j] = d6[i,j]
93.	                    e[i,j] = 2500
94.	                  if a[i,j] == -1:
95.	                    if math.fabs(d9[i,j]* 0.05) >= math.fabs(d9[i,j] – d7[i,j]):
96.	                      a[i,j] = d7[i,j]
97.	                      e[i,j] = 2750              
98.	                    if a[i,j] == -1:
99.	                      if math.fabs(d10[i,j]* 0.05) >= math.fabs(d10[i,j] – d8[i,j]):
100.	                        a[i,j] = d8[i,j]
101.	                        e[i,j] = 3000            
102.	                      if a[i,j] == -1:
103.	                        if math.fabs(d11[i,j]* 0.05) >= math.fabs(d11[i,j] – d9[i,j]):
104.	                          a[i,j] = d9[i,j]
105.	                          e[i,j] = 3250       
106.	                        if a[i,j] == -1:
107.	                          if math.fabs(d12[i,j]* 0.05) >= math.fabs(d12[i,j] – d10[i,j]):
108.	                            a[i,j] = d10[i,j]
109.	                            e[i,j] = 3500        
110.	                          if a[i,j] == -1:     
111.	                            if math.fabs(d13[i,j]* 0.05) >= math.fabs(d13[i,j] - d11[i,j]):
112.	                              a[i,j] = d11[i,j]
113.	                              e[i,j] = 3750
114.	                            if a[i,j] == -1:
115.	                              if math.fabs(d14[i,j]* 0.05) >= math.fabs(d14[i,j] - d12[i,j]):
116.	                                a[i,j] = d12[i,j]
117.	                                e[i,j] = 4000
118.	                              if a[i,j] == -1:
119.	                                if math.fabs(d15[i,j]* 0.05) >= math.fabs(d15[i,j] - d13[i,j]):
120.	                                  a[i,j] = d13[i,j]
121.	                                  e[i,j] = 4250
122.	                                if a[i,j] == -1:
123.	                                  if math.fabs(d16[i,j]* 0.05) >= math.fabs(d16[i,j] - d14[i,j]):
124.	                                    a[i,j] = d14[i,j]
125.	                                    e[i,j] = 4500              
126.	                                  if a[i,j] == -1:
127.	                                    if math.fabs(d17[i,j]* 0.05) >= math.fabs(d17[i,j] - d15[i,j]):
128.	                                      a[i,j] = d15[i,j]
129.	                                      e[i,j] = 4750            
130.	                                    if a[i,j] == -1:
131.	                                      if math.fabs(d18[i,j]* 0.05) >= math.fabs(d18[i,j] - d16[i,j]):
132.	                                        a[i,j] = d16[i,j]
133.	                                        e[i,j] = 5000       
134.	                                      if a[i,j] == -1:
135.	                                        if math.fabs(d19[i,j]* 0.05) >= math.fabs(d19[i,j] - d17[i,j]):
136.	                                          a[i,j] = d17[i,j]
137.	                                          e[i,j] = 5250
138.	                                        if a[i,j] == -1:
139.	                                          if math.fabs(d20[i,j]* 0.05) >= math.fabs(d20[i,j] - d18[i,j]):
140.	                                            a[i,j] = d18[i,j]
141.	                                            e[i,j] = 5500      
142.	                                          if a[i,j] == -1:
143.	                                            if math.fabs(d20[i,j]* 0.05) >= math.fabs(d20[i,j] – d19[i,j]):
144.	                                               a[i,j] = d19[i,j]
145.	                                               e[i,j] = 5750      
146.	                                             if a[i,j] == -1:
147.	                                              a[i,j] = d20[i,j]
148.	                                              e[i,j] = 6000
149.	raster = arcpy.NumPyArrayToRaster (a, lower_left, dsc.meanCellWidth, dsc.meanCellHeight,noDataValue) 
150.	raster.save("amplituda")
151.	raster2 = arcpy.NumPyArrayToRaster(e, lower_left, dsc.meanCellWidth, dsc.meanCellHeight,noDataValue)
152.	raster2.save("velkost_okna")
153.	del raster
154.	del raster2
