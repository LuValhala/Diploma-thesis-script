1.	import arcpy
2.	from arcpy.sa import *
3.	import numpy as np
4.	import math
5.	arcpy.env.workspace = r"C:/test" 
6.	FS = "MEAN"                                            
7.	dtm = "od_udolnice" 
8.	er1=0 #pocitadla pre chyby
9.	er2=0
10.	er3=0
11.	er4=0
12.	er5=0
13.	err=0
14.	def Stupa(i, j, ka, pk): 
15.	  if ka < len(zoz)-1: 
16.	    if ka >= len(zoz)-pk-1: 
17.	      try:
18.	        if pk == 0:
19.	          a[i,j] = zoz[ka][i,j]
20.	          e[i,j] = zoznvelk[ka] #+1
21.	          global er2
22.	          er2 =+ 1
23.	          return
24.	        if math.fabs(zoz[ka+pk][i,j] * 0.05) >= math.fabs(zoz[ka+pk][i,j] - zoz[ka][i,j]):
25.	          a[i,j] = zoz[ka][i,j]
26.	          e[i,j] = zoznvelk[ka] #+1
27.	          return
28.	        else:
29.	          Stupa(i, j, ka+1, pk-1) 
30.	          return
31.	      except:
32.	        global er1
33.	        er1 =+ 1
34.	    else:  
35.	      try:
36.	        if math.fabs(zoz[ka][i,j]* 0.05) < zoz[ka+pk][i,j] - zoz[ka][i,j]: 
37.	          Stupa(i, j, ka+1, pk)
38.	          return
39.	        else:
40.	          a[i,j] = zoz[ka][i,j]
41.	          e[i,j] = zoznvelk[ka] #+1
42.	          return
43.	      except:
44.	        global er3
45.	        er3 =+ 1
46.	  else: 
47.	    try:
48.	      a[i,j] = zoz[ka][i,j]
49.	      e[i,j] = zoznvelk[ka] #+1
50.	      return
51.	    except:
52.	      global er4
53.	      er4 =+ 1 
54.	def Klesa(i, j, ka, pk):
55.	  if ka < len(zoz)-1: 
56.	    if ka >= len(zoz)-pk-1:
57.	      try:
58.	        if pk == 0:
59.	          a[i,j] = zoz[ka][i,j]
60.	          e[i,j] = zoznvelk[ka] #+2         
61.	 global er2
62.	          er2 =+ 1
63.	          return
64.	        if math.fabs(zoz[ka+pk][i,j] * 0.05) >= math.fabs(zoz[ka+pk][i,j] - zoz[ka][i,j]):
65.	          a[i,j] = zoz[ka][i,j]
66.	          e[i,j] = zoznvelk[ka] #+2
67.	          return
68.	        else:
69.	          Klesa(i, j, ka+1, pk-1) 
70.	          return
71.	      except:
72.	        global er1
73.	        er1 =+ 1
74.	    else:  
75.	      try:
76.	        if math.fabs(zoz[ka][i,j]* 0.05) > zoz[ka][i,j] - zoz[ka+pk][i,j]:
77.	            Klesa(i, j, ka+1, pk)
78.	            return
79.	          else:
80.	            a[i,j] = zoz[ka][i,j]
81.	            e[i,j] = zoznvelk[ka] #+2
82.	            return
83.	      except:
84.	        global er3
85.	        er3 =+ 1
86.	  else:
87.	    try:
88.	      a[i,j] = zoz[ka][i,j]
89.	      e[i,j] = zoznvelk[ka] #+2
90.	      return
91.	    except:
92.	      global er4
93.	      er4 =+ 1      
94.	def Pocitaj(i, j, ka, pk):
95.	  if ka < len(zoz)-1: 
96.	    if ka >= len(zoz)-pk-1: 
97.	      try:
98.	        if math.fabs(zoz[ka+pk][i,j] * 0.05) >= math.fabs(zoz[ka+pk][i,j] - zoz[ka][i,j]):
99.	          a[i,j] = zoz[ka][i,j]
100.	          e[i,j] = zoznvelk[ka] #+3
101.	          return
102.	        else:
103.	          Pocitaj(i, j,ka+1,pk-1) 
104.	          return
105.	      except:
106.	        global er1
107.	        er1 =+ 1
108.	    else:   #stupa alebo klesa?
109.	      try:        
110.	        if math.fabs(zoz[ka+pk][i,j] * 0.05) >= math.fabs(zoz[ka+pk][i,j] - zoz[ka][i,j]):
111.	          if zoz[ka][i,j] < zoz[ka+pk][i,j]:
112.	            Stupa(i, j, ka, pk)
113.	            return
114.	          if zoz[ka][i,j] > zoz[ka+pk][i,j]:
115.	            Klesa(i, j, ka, pk)
116.	            return          else:
117.	            global err 
118.	            err = +1
119.	        else: 
120.	          Pocitaj(i, j, ka+1, pk)
121.	          return
122.	      except:
123.	        global er3
124.	        er3 =+ 1
125.	  else: 
126.	    try:
127.	      a[i,j] = zoz[ka][i,j]
128.	      e[i,j] = zoznvelk[ka] #+3   
129.	      return
130.	    except:
131.	      global er4
132.	      er4 =+ 1
133.	array = arcpy.RasterToNumPyArray(dtm)              
134.	velkost = array.shape                                            
135.	x=velkost[0]
136.	y=velkost[1]
137.	dsc = arcpy.Describe(dtm)
138.	SR = dsc.SpatialReference
139.	ext = dsc.Extent
140.	lower_left = arcpy.Point(ext.XMin,ext.YMin)
141.	arcpy.env.outCoordinateSystem = SR
142.	noDataValue = dsc.noDataValue
143.	c=FocalStatistics(dtm,NbrCircle(500,"MAP"),FS,"DATA")   
144.	d0=arcpy.RasterToNumPyArray(c)
145.	c=FocalStatistics(dtm,NbrCircle(625,"MAP"),FS,"DATA")   
146.	d1=arcpy.RasterToNumPyArray(c)
147.	c=FocalStatistics(dtm,NbrCircle(750,"MAP"),FS,"DATA")
148.	d2=arcpy.RasterToNumPyArray(c)   
149.	c=FocalStatistics(dtm,NbrCircle(875,"MAP"),FS,"DATA")   
150.	d3=arcpy.RasterToNumPyArray(c)
151.	c=FocalStatistics(dtm,NbrCircle(1000,"MAP"),FS,"DATA")
152.	d4=arcpy.RasterToNumPyArray(c)      
153.	c=FocalStatistics(dtm,NbrCircle(1125,"MAP"),FS,"DATA")   
154.	d5=arcpy.RasterToNumPyArray(c)
155.	c=FocalStatistics(dtm,NbrCircle(1250,"MAP"),FS,"DATA")   
156.	d6=arcpy.RasterToNumPyArray(c)      
157.	c=FocalStatistics(dtm,NbrCircle(1375,"MAP"),FS,"DATA")   
158.	d7 = arcpy.RasterToNumPyArray(c)     
159.	c=FocalStatistics(dtm,NbrCircle(1500,"MAP"),FS,"DATA")
160.	d8 = arcpy.RasterToNumPyArray(c)
161.	c=FocalStatistics(dtm,NbrCircle(1625,"MAP"),FS,"DATA")
162.	d9 = arcpy.RasterToNumPyArray(c)
163.	c=FocalStatistics(dtm,NbrCircle(1750,"MAP"),FS,"DATA")
164.	d10 = arcpy.RasterToNumPyArray(c)
165.	c=FocalStatistics(dtm,NbrCircle(1875,"MAP"),FS,"DATA")
166.	d11 = arcpy.RasterToNumPyArray(c)        
167.	c=FocalStatistics(dtm,NbrCircle(2000,"MAP"),FS,"DATA")
168.	d12 = arcpy.RasterToNumPyArray(c)
169.	c=FocalStatistics(dtm,NbrCircle(2125,"MAP"),FS,"DATA")   
170.	d13 = arcpy.RasterToNumPyArray(c)
171.	c=FocalStatistics(dtm,NbrCircle(2250,"MAP"),FS,"DATA")   
172.	d14 = arcpy.RasterToNumPyArray(c)      
173.	c=FocalStatistics(dtm,NbrCircle(2375,"MAP"),FS,"DATA")   
174.	d15 = arcpy.RasterToNumPyArray(c)     
175.	c=FocalStatistics(dtm,NbrCircle(2500,"MAP"),FS,"DATA")
176.	d16 = arcpy.RasterToNumPyArray(c)
177.	c=FocalStatistics(dtm,NbrCircle(2625,"MAP"),FS,"DATA")
178.	d17 = arcpy.RasterToNumPyArray(c)
179.	c=FocalStatistics(dtm,NbrCircle(2750,"MAP"),FS,"DATA")
180.	d18 = arcpy.RasterToNumPyArray(c)
181.	c=FocalStatistics(dtm,NbrCircle(2875,"MAP"),FS,"DATA")
182.	d19 = arcpy.RasterToNumPyArray(c)        
183.	c=FocalStatistics(dtm,NbrCircle(3000,"MAP"),FS,"DATA")
184.	d20 = arcpy.RasterToNumPyArray(c)
185.	del c
186.	zoz = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20]
187.	zoznvelk = [pee for pee in range(1000, 6250, 250)] 
188.	a = np.zeros((x, y))
189.	e = np.zeros((x, y))  
190.	for i in range(0,x):
191.	  for j in range(0,y):
192.	    Pocitaj(i, j, 0, 2) 
193.	print "chyby:",er1,er2,er3,er4,er5, err,
194.	raster = arcpy.NumPyArrayToRaster (a, lower_left, dsc.meanCellWidth, dsc.meanCellHeight,noDataValue)
195.	raster.save("priem_vy_odU")
196.	
197.	raster2=arcpy.NumPyArrayToRaster(e, lower_left, dsc.meanCellWidth, dsc.meanCellHeight,noDataValue) 
198.	raster2.save("Velk_oKna")
199.	del raster
200.	del raster2
 
