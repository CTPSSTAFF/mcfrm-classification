# mcfrm_classification_october_2022.py
#
# Given the MC-FRM 2050 probability data for the 'north' towns already combined into a single raster dataset,
# generate a polygon feature class from it, having classified the raster probability cells as follows:
#    * probability >= 0.05              - cell value = 4
#    * probability >= 0.02 and < 0.05   - cell value = 3
#    * probability >= 0.01 and < 0.02   - cell value = 2
#    * probability >= 0.002 and < 0.01  - cell value = 1
#    * probability >= 0.001 and < 0.001 - cell value = 0
#
# This script is a transcript of the steps executed manually on October 17, 2022 to produce the requested feature class.
# It has not been "genericized" or "parameterized", but doing this should be relativel straightforward and mostly entail
# defining a parameter for the name of the geodatabase in which the intermediate and final data product is created.
#
# -- B. Krepp, 18 October 2022

import arcpy

# Load 2050 probability raster for the 'north' towns
arcpy.MakeRasterLayer_management(in_raster="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/2050_North_Probability.gdb/raster_ds_2050_North_Probability", 
    out_rasterlayer="2050 Probability - north towns (raster data)", 
    where_clause="", envelope="221641.516430974 834092.936153378 281989.516430974 960748.936153378", band_index="")

# Create >= 5% inundation probability raster
# Cells with value >= 0.05 are into cells with value = 4, others into cells with value = -1
arcpy.gp.RasterCalculator_sa('Con("2050 Probability - north towns (raster data)" > 0.05, 4, -1)', 
    "//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_ge_5_pct")
	
# Create 2 to 5% inundation probability raster
# Cells with value between 0.02 and 0.05 are mapped into cells with value = 3, others into cells with value = -1
arcpy.gp.RasterCalculator_sa('Con(  ( "2050 Probability - north towns (raster data)" >= 0.02 )  &  
                                    ( "2050 Probability - north towns (raster data)" < 0.05 ), 3, -1)', 
	"//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_2_5_pct")
    
# Create 1 to 2% inundation probability raster
# Cells with value between 0.01 and 0.02 are mapped into cells with value = 2, others into cells with value = -1
arcpy.gp.RasterCalculator_sa('Con(  ( "2050 Probability - north towns (raster data)" >= 0.01 )  &  
                                    ( "2050 Probability - north towns (raster data)" < 0.02 ), 2, -1)', 
    "//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_1_2_pct")
    
# Create 0.2 to 1% inundation probability raster
# Cells with value between 0.002 and 0.01 are mapped into cells with value = 1, others into cells with value = -1
arcpy.gp.RasterCalculator_sa('Con(  ( "2050 Probability - north towns (raster data)" >= 0.002 )  &  
                                    ( "2050 Probability - north towns (raster data)" < 0.01 ), 1, -1)', 
    "//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_0d2_1_pct")
    
# Create 0.1 to 0.2% inundation probability raster
# Cells with value between 0.001 and 0.002 are mapped into cells with value = 0, others into cells with value = -1
arcpy.gp.RasterCalculator_sa('Con(  ( "2050 Probability - north towns (raster data)" >= 0.001 )  &  
                                    ( "2050 Probability - north towns (raster data)" < 0.002 ), 0, -1)', 
    "//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_0d1_0d2_pct")
    
# Create multi-part polygon feature clases from each of the 'classified' probability rasters;
# the features with gridcode == 0 will be filtered out subseqently
#
# >= 5% probability
arcpy.RasterToPolygon_conversion(in_raster="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_ge_5_pct", 
    out_polygon_features="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_ge_5_pct_temp_fc", 
    simplify="SIMPLIFY", raster_field="Value", create_multipart_features="MULTIPLE_OUTER_PART", max_vertices_per_feature="")    

# 2 to 5% probability
arcpy.RasterToPolygon_conversion(in_raster="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_2_5_pct", 
    out_polygon_features="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_2_5_pct_temp_fc", 
    simplify="SIMPLIFY", raster_field="Value", create_multipart_features="MULTIPLE_OUTER_PART", max_vertices_per_feature="")
    
# 1 to 2% probability
arcpy.RasterToPolygon_conversion(in_raster="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_1_2_pct", 
    out_polygon_features="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_1_2_pct_temp_fc", 
    simplify="SIMPLIFY", raster_field="Value", create_multipart_features="MULTIPLE_OUTER_PART", max_vertices_per_feature="")

# 0.2 to 1% probability
arcpy.RasterToPolygon_conversion(in_raster="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_0d2_1_pct", 
    out_polygon_features="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_0d2_1_pct_temp_fc", 
    simplify="SIMPLIFY", raster_field="Value", create_multipart_features="MULTIPLE_OUTER_PART", max_vertices_per_feature="")

# 0.1 to 0.2% probability
arcpy.RasterToPolygon_conversion(in_raster="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_0d1_0d2_pct", 
    out_polygon_features="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_0d1_0d2_pct_temp_fc", 
    simplify="SIMPLIFY", raster_field="Value", create_multipart_features="MULTIPLE_OUTER_PART", max_vertices_per_feature="")

# Extract features with non-zero gridcode values to indvidual feature classes
#
# >= 5% probability (gridcode == 4)
arcpy.Select_analysis(in_features="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_ge_5_pct_temp_fc", 
    out_feature_class="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_ge_5_pct_fc", 
    where_clause="gridcode = 4")

# 2 to 5% probability (gridcode == 3)
arcpy.Select_analysis(in_features="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_2_5_pct_temp_fc", 
    out_feature_class="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_2_5_pct_fc", 
    where_clause="gridcode = 3")
    
# 1 to 2% probability (gridcode == 2)
arcpy.Select_analysis(in_features="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_0d2_1_pct_temp_fc", 
    out_feature_class="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_0d2_1_pct_fc", 
    where_clause="gridcode = 2")
    
# 0.2 to 1% probability (gridcode == 1)
arcpy.Select_analysis(in_features="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_0d2_1_pct_temp_fc", 
    out_feature_class="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_0d2_1_pct_fc", 
    where_clause="gridcode = 1")
    
# 0.1 to 0.2% probability (gridcode == 0)
arcpy.Select_analysis(in_features="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_0d1_0d2_pct_temp_fc", 
    out_feature_class="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_0d1_0d2_pct_fc", 
    where_clause="gridcode = 0")

# Merge the individual polygon feature classes into a single feature class, the final product
arcpy.Merge_management(inputs="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_ge_5_pct_fc;//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_2_5_pct_fc;//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_1_2_pct_fc;//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_0d2_1_pct_fc;//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/p_0d1_0d2_pct_fc",
    output="//lilliput/groups/Certification_Activities/Resiliency/data/mcfrm/LEVEL_1/2050/North/Probability/RECLASSIFICATION_OCT2020.gdb/probability_score_2050_oct2022_fc", 
    field_mappings='Id "Id" true true false 4 Long 0 0 ,First,#,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_ge_5_pct_fc,Id,-1,-1,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_2_5_pct_fc,Id,-1,-1,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_1_2_pct_fc,Id,-1,-1,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_0d2_1_pct_fc,Id,-1,-1,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_0d1_0d2_pct_fc,Id,-1,-1;gridcode "gridcode" true true false 4 Long 0 0 ,First,#,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_ge_5_pct_fc,gridcode,-1,-1,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_2_5_pct_fc,gridcode,-1,-1,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_1_2_pct_fc,gridcode,-1,-1,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_0d2_1_pct_fc,gridcode,-1,-1,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_0d1_0d2_pct_fc,gridcode,-1,-1;Shape_Length "Shape_Length" false true true 8 Double 0 0 ,First,#,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_ge_5_pct_fc,Shape_Length,-1,-1,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_2_5_pct_fc,Shape_Length,-1,-1,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_1_2_pct_fc,Shape_Length,-1,-1,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_0d2_1_pct_fc,Shape_Length,-1,-1,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_0d1_0d2_pct_fc,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0 ,First,#,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_ge_5_pct_fc,Shape_Area,-1,-1,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_2_5_pct_fc,Shape_Area,-1,-1,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_1_2_pct_fc,Shape_Area,-1,-1,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_0d2_1_pct_fc,Shape_Area,-1,-1,\\lilliput\groups\Certification_Activities\Resiliency\data\mcfrm\LEVEL_1\2050\North\Probability\RECLASSIFICATION_OCT2020.gdb\p_0d1_0d2_pct_fc,Shape_Area,-1,-1')