#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      yogi
#
# Created:     22/02/2021
# Copyright:   (c) yogi 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
import os
from arcpy import env

def main():

    # Create brand new geodatabase
    arcpy.CreateFileGDB_management(r"D:\arcpy\tutorial_geosai", "geosai.gdb")

    # List all features in a folder
    arcpy.env.workspace = r"D:\arcpy\tutorial_geosai\data"
    feature_classes = arcpy.ListFeatureClasses() # return a list of shapefile

    # Copy all features to gdb
    for fc in feature_classes:
        arcpy.CopyFeatures_management(
            fc, os.path.join(r"D:\arcpy\tutorial_geosai\geosai.gdb", os.path.splitext(fc)[0])
        )

    # Union features in gdb
    arcpy.env.workspace = r"D:\arcpy\tutorial_geosai\geosai.gdb"
    arcpy.Union_analysis (["adm_kab", "adm_kec"], "adm_union")

    # Create a new folder
    arcpy.CreateFolder_management(r"D:\arcpy\tutorial_geosai", "data_output")

    # Copy adm_union to folder
    arcpy.CopyFeatures_management(r"D:\arcpy\tutorial_geosai\geosai.gdb\adm_union", r"D:\arcpy\tutorial_geosai\data_output\adm_union")

    # Print Done
    print("Done")

if __name__ == '__main__':
    main()
