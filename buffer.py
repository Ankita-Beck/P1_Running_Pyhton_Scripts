# Importing arcpy package
import arcpy

arcpy.env.workspace = r"D:\Programming_for_GIS_3\P1_Running_Pyhton_Scripts\Practical_1_ProProject\Practical_1_ProProject\01_Running_Python_Scripts.gdb"

# Perform buffer operations
arcpy.analysis.Buffer("Wilson_Schools","Wilson_School_Buffer","500 meters")

print("Process Completed")