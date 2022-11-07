# Script to perform 7-way classification on input MC-FRM raster dataset,
# and produce a multipart polygon feature class with "gridcode" attribute with values 1 to 7.
#
# Classification scheme:
#    * probability >  0.10              - cell value = 7
#    * probability >= 0.05 and < 0.10   - cell value = 6
#    * probability >= 0.02 and < 0.05   - cell value = 5
#    * probability >= 0.01 and < 0.02   - cell value = 4
#    * probability >= 0.002 and < 0.01  - cell value = 3
#    * probability >= 0.001 and < 0.002 - cell value = 2
#    * probability <  0.001             - cell value = 1
#
# Parameters: 1 - input_raster_ds_path
#             2 - working_gdb
#             3 - final_output_fc
# 
# Author: Ben Krepp,  11/07/2022

import arcpy

# input_raster_ds_path = "//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/Present/North/Probability/Present_Probability_North.gdb/raster_ds_Present_North_probability"
# working_gdb = "//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/Present/North/Probability/CTPS_CLASSIFICATION.gdb"
# final_output_fc = working_gdb + '/CTPS_probability_score_present'


# Read input parameters
input_raster_ds_path = arcpy.GetParameterAsText(0)
working_gdb = arcpy.GetParameterAsText(1)
final_output_fc = arcpy.GetParameterAsText(2)

# Sanity check: Echo input parameters
arcpy.AddMessage('Input raster dataset: ' + input_raster_ds_path)
arcpy.AddMessage('Working GDB: ' + working_gdb)
arcpy.AddMessage('Final output feature class: ' + final_output_fc)


# Load input raster
input_raster_layer_name = "input_raster"
arcpy.MakeRasterLayer_management(in_raster=input_raster_ds_path, out_rasterlayer=input_raster_layer_name, where_clause="", band_index="1;1")
arcpy.AddMessage('Loaded raster.')
	
#####################
# *** Classification 7 raster: probability > 10%
arcpy.AddMessage('Beginning classification level 7 processing.')

classified_raster = working_gdb + "/p_gt_10_pct"
arcpy.gp.RasterCalculator_sa('Con("input_raster" > 0.10, 7, -1)', classified_raster)  
arcpy.AddMessage('Classified raster.')

# Multipart polygon feature class: features classified as 7 or -1
polygon_fc_temp = working_gdb + "/p_gt_10_pct_fc_temp"
arcpy.RasterToPolygon_conversion(in_raster=classified_raster, out_polygon_features=polygon_fc_temp, 
                                 simplify="SIMPLIFY", raster_field="Value", create_multipart_features="MULTIPLE_OUTER_PART", max_vertices_per_feature="")                                  
arcpy.AddMessage('Completed raster to polygon conversion.')                                 

# Feature class with classification 7 features only 
polygon_fc = working_gdb + "/p_gt_10_pct_fc"
arcpy.Select_analysis(in_features=polygon_fc_temp, out_feature_class=polygon_fc, where_clause="gridcode <> -1")
arcpy.AddMessage('Completed filtering polygon features.')

#####################
# *** Classification 6 raster: probability 5 to 10%
arcpy.AddMessage('Beginning classification level 6 processing.')

classified_raster = working_gdb + "/p_5_10_pct"
arcpy.gp.RasterCalculator_sa('Con(  ("input_raster"  >= 0.05 )  &  ("input_raster"  <  0.10 ), 6, -1)', classified_raster)  
arcpy.AddMessage('Classified raster.')

# Multipart polygon feature class: features classified as 6 or -1
polygon_fc_temp = working_gdb + "/p_5_10_pct_fc_temp"
arcpy.RasterToPolygon_conversion(in_raster=classified_raster, out_polygon_features=polygon_fc_temp, 
                                 simplify="SIMPLIFY", raster_field="Value", create_multipart_features="MULTIPLE_OUTER_PART", max_vertices_per_feature="")                                  
arcpy.AddMessage('Completed raster to polygon conversion.')                                 

# Feature class with classification 6 features only 
polygon_fc = working_gdb + "/p_5_10_pct_fc"
arcpy.Select_analysis(in_features=polygon_fc_temp, out_feature_class=polygon_fc, where_clause="gridcode <> -1")
arcpy.AddMessage('Completed filtering polygon features.')

#####################
# *** Classification 5 raster: probability 2 to 5%
arcpy.AddMessage('Beginning classification level 5 processing.')

classified_raster = working_gdb + "/p_2_5_pct"
arcpy.gp.RasterCalculator_sa('Con(  ("input_raster"  >= 0.02 )  &  ("input_raster"  <  0.05 ), 5, -1)', classified_raster)  
arcpy.AddMessage('Classified raster.')

# Multipart polygon feature class: features classified as 5 or -1
polygon_fc_temp = working_gdb + "/p_2_5_pct_fc_temp"
arcpy.RasterToPolygon_conversion(in_raster=classified_raster, out_polygon_features=polygon_fc_temp, 
                                 simplify="SIMPLIFY", raster_field="Value", create_multipart_features="MULTIPLE_OUTER_PART", max_vertices_per_feature="")                                  
arcpy.AddMessage('Completed raster to polygon conversion.')                                 

# Feature class with classification 5 features only 
polygon_fc = working_gdb + "/p_2_5_pct_fc"
arcpy.Select_analysis(in_features=polygon_fc_temp, out_feature_class=polygon_fc, where_clause="gridcode <> -1")
arcpy.AddMessage('Completed filtering polygon features.')

#####################
# *** Classification 4 raster: probability 1 to 2%
arcpy.AddMessage('Beginning classification level 4 processing.')

classified_raster = working_gdb + "/p_1_2_pct"
arcpy.gp.RasterCalculator_sa('Con(  ("input_raster"  >= 0.01 )  &  ("input_raster"  <  0.02 ), 4, -1)', classified_raster)  
arcpy.AddMessage('Classified raster.')

# Multipart polygon feature class: features classified as 4 or -1
polygon_fc_temp = working_gdb + "/p_1_2_pct_fc_temp"
arcpy.RasterToPolygon_conversion(in_raster=classified_raster, out_polygon_features=polygon_fc_temp, 
                                 simplify="SIMPLIFY", raster_field="Value", create_multipart_features="MULTIPLE_OUTER_PART", max_vertices_per_feature="")                                  
arcpy.AddMessage('Completed raster to polygon conversion.')                                 

# Feature class with classification 4 features only 
polygon_fc = working_gdb + "/p_1_2_pct_fc"
arcpy.Select_analysis(in_features=polygon_fc_temp, out_feature_class=polygon_fc, where_clause="gridcode <> -1")
arcpy.AddMessage('Completed filtering polygon features.')

#####################
# *** Classification 3 raster: probability 0.2 to 1%
arcpy.AddMessage('Beginning classification level 3 processing.')

classified_raster = working_gdb + "/p_0d2_1_pct"
arcpy.gp.RasterCalculator_sa('Con(  ("input_raster"  >= 0.002 ) &  ("input_raster"  <  0.01 ), 3, -1)', classified_raster)  
arcpy.AddMessage('Classified raster.')

# Multipart polygon feature class: features classified as 3 or -1
polygon_fc_temp = working_gdb + "/p_0d2_1_pct_fc_temp"
arcpy.RasterToPolygon_conversion(in_raster=classified_raster, out_polygon_features=polygon_fc_temp, 
                                 simplify="SIMPLIFY", raster_field="Value", create_multipart_features="MULTIPLE_OUTER_PART", max_vertices_per_feature="")                                  
arcpy.AddMessage('Completed raster to polygon conversion.')                                 

# Feature class with classification 3 features only 
polygon_fc = working_gdb + "/p_0d2_1_pct_fc"
arcpy.Select_analysis(in_features=polygon_fc_temp, out_feature_class=polygon_fc, where_clause="gridcode <> -1")
arcpy.AddMessage('Completed filtering polygon features.')

#####################
# *** Classification 2 raster: probability 0.1 to 0.2%
arcpy.AddMessage('Beginning classification level 2 processing.')

classified_raster = working_gdb + "/p_0d1_0d2_pct"
arcpy.gp.RasterCalculator_sa('Con(  ("input_raster"  >= 0.001 ) &  ("input_raster"  <  0.002 ), 2, -1)', classified_raster)  
arcpy.AddMessage('Classified raster.')

# Multipart polygon feature class: features classified as 2 or -1
polygon_fc_temp = working_gdb + "/p_0d1_0d2_pct_fc_temp"
arcpy.RasterToPolygon_conversion(in_raster=classified_raster, out_polygon_features=polygon_fc_temp, 
                                 simplify="SIMPLIFY", raster_field="Value", create_multipart_features="MULTIPLE_OUTER_PART", max_vertices_per_feature="")                                  
arcpy.AddMessage('Completed raster to polygon conversion.')                                 

# Feature class with classification 2 features only 
polygon_fc = working_gdb + "/p_0d1_0d2_pct_fc"
arcpy.Select_analysis(in_features=polygon_fc_temp, out_feature_class=polygon_fc, where_clause="gridcode <> -1")
arcpy.AddMessage('Completed filtering polygon features.')

#####################
# *** Classification 1 raster: probability < 0.1%
arcpy.AddMessage('Beginning classification level 1 processing.')

classified_raster = working_gdb + "/p_lt_0d1_pct"
arcpy.gp.RasterCalculator_sa('Con("input_raster"  < 0.001, 1, -1)', classified_raster)  
arcpy.AddMessage('Classified raster.')

# Multipart polygon feature class: features classified as 1 or -1
polygon_fc_temp = working_gdb + "/p_lt_0d1_pct_fc_temp"
arcpy.RasterToPolygon_conversion(in_raster=classified_raster, out_polygon_features=polygon_fc_temp, 
                                 simplify="SIMPLIFY", raster_field="Value", create_multipart_features="MULTIPLE_OUTER_PART", max_vertices_per_feature="")                                  
arcpy.AddMessage('Completed raster to polygon conversion.')                                 

# Feature class with classification 1 features only 
polygon_fc = working_gdb + "/p_lt_0d1_pct_fc"
arcpy.Select_analysis(in_features=polygon_fc_temp, out_feature_class=polygon_fc, where_clause="gridcode <> -1")
arcpy.AddMessage('Completed filtering polygon features.')

# Merge indivdual multipart polygone feature classes into a single final output feature class
arcpy.AddMessage('Generating final output feature class.') 
# First, assemble list of input feature classes:
inputs_list = [ working_gdb + '/p_gt_10_pct_fc',
                working_gdb + '/p_5_10_pct_fc',
                working_gdb + '/p_2_5_pct_fc',
                working_gdb + '/p_1_2_pct_fc',
                working_gdb + '/p_0d2_1_pct_fc',  
                working_gdb + '/p_0d1_0d2_pct_fc',
                working_gdb + '/p_lt_0d1_pct_fc' ]
# Perform the merge
arcpy.Merge_management(inputs=inputs_list, output=final_output_fc)

# Drop un-needed "id" field
arcpy.DeleteField_management(final_output_fc, ["id"])
# Rename "gridcode" field to "score"
arcpy.AlterField_management(final_output_fc, "gridcode", "score")
arcpy.AddMessage('Processing complete.') 
