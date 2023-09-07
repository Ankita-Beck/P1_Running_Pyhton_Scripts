import arcpy

arcpy.env.workspace = r"D:\Programming_for_GIS_3\P1_Running_Pyhton_Scripts\Practical_1_ProProject\Practical_1_ProProject\01_Running_Python_Scripts.gdb"

# Convert to feature class
input_feature_class = "Wilson_Zoning"
output_feature_class = " Wilson_Zoning_point"

arcpy.management.FeatureToPoint(input_feature_class,output_feature_class,"CENTROID")

print("Process completed")