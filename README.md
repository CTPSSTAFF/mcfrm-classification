# mcfrm-classification
Tools to 'classify' MC-FRM raster data and produce polygon feature classes from the classification.

This repository contains scripts to 'classify' the cells in 2050 MC-FRM probability rasters and generate polygon features from this classification.  

These scripts currently not parameterized. That is to say, the following are currently hard-wired:
* the input File GeoDatabase and raster dataset
* the output File GeoDatabase and multi-part polygon feature class

Parameterization of these scripts will be implemented incrementally, as time and personnel are available.
The intention was to get the baseline working version of these tools under version control sooner rather than later.

Inventory:
* BOS_classification.py - Script implementing classification proposed by Judy Tayor on October 14, 2022.
