# Diploma-thesis-script
For more information about the script and the methodology feel free to contact me anytime at lubos.valco@gmail.com. For more information about the theory, contact my tutor at: Department of physical geography and geoecology at University of Comenius in Bratislava, Slovakia - prof. RNDr. Jozef Minár, CSc., or by email: jozef.minar@uniba.sk

THEORY:
The continuosly expanding(dynamic) window is trying to capture the true nature of the topographic characteristic in each point. Needed because sometimes the characteristic should be calculated in 2km window, but sometimes 4km is needed. therefore the window should calculate for each point differently, according to condition.
For better explanation see Pike, R., J., Acevedo, W., 1989. Topographic grain automated from Digital elevation models. In: Proceedings 9th International Symposium on Computer Assisted Cartography. s. 128–137.

PYTHON IMPLEMENTATION:
Working environment is ArcGIS 10.2.. Imported layer is transformed into 2D array, then values of various configurations of chosen calculation are stored in memory**** . After that comparision chooses the correct value and saves it into zero array, which is then exported as output layer.
Script is published the way it was created when publishing the thesis. NOTE that right now (8/2017) i would make it completely differently as it absolutely inefficient in the amount of RAM it needs to use****. Problem was that i didnt know about few functions in the beginning of the creative process. [ NbrCircle(x,y) returns the value of calculated characteristic in given radius - can be used to save all the RAM and also speed up the process a bit ]

ABSTRACT OF THE THESIS:
VALČO, Ľuboš: Data preparation for the physically based morphostructural segmentation of the Western Carpathians. [Master thesis]. Comenius University in Bratislava. Faculty of Natural Sciences. Department of Physical Geography and Geoecology. Tutor: prof. RNDr. Jozef Minár, CSc. Bratislava: Faculty of Natural Sciences CU, 2017. 63 pp.

This master thesis is creating new methods for physicaly based morphostructural topographic segmentation. It is also testing the newly created automatized methods as well as calibrating the values of input parameters that influence the calculation in the model specially focusing on classification of the morphostructures. Creation of the new method focused mainly on calculationg the main wave lenght. Other calculated characteristics were also local relief (diference between the highest and the lowest point in the area), amount of endogenic and exogenic energy and others. Calculated characteristics by new methods were tested on the area of the Western Capathians. New methods are almost completely automated using scripts written in Python 2.7. The process of development is described in details but in an understandable way. Thesis can be therefore interesting also for begginers in creating the new automated methods. Results are presented with map outputs. Analysis of the results and comparision of the outputs with other published scientific papers are in the ending of the thesis.

Keywords: topographic segmentation , morphostructures, Western Capathians, topographic energy, spatial analysis,
