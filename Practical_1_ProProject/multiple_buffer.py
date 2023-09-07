import arcpy

arcpy.env.workspace = r"D:\Programming_for_GIS_3\P1_Running_Pyhton_Scripts\Practical_1_ProProject\Practical_1_ProProject\01_Running_Python_Scripts.gdb"

# Buffer feature selection
input_feature_class = "Wilson_Schools"
output_feature_class = "Wilson_School_MultipleBuffer"

# Buffer distance
buffer_distance = [1000,1200,1400]

arcpy.analysis.MultipleRingBuffer(input_feature_class,output_feature_class,buffer_distance,"Feet","","NONE")

print("process completed")