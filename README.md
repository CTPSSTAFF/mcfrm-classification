# mcfrm-classification
Tools to 'classify' a  MC-FRM raster probability dataset and produce a multi-part polygon feature class from the classification.
 
These scripts currently _not_ parameterized. That is to say, the following are currently hard-wired:
* the input raster dataset
* the 'working' File GeoDatabase
* the final output multi-part polygon feature class

Parameterization of these scripts will be implemented incrementally, as time and human resources are available.
The intention was to get a baseline working version of each these tools under version control sooner rather than later.

Inventory:
* MBTA_classification.py - Script implementing classification used by the MBTA, and communicated to CTPS by Hannah Lyons-Galante in the spring of 2022.
* BOS_classification.py - Script implementing classification used by the City of Boston and discussed by Judy Tayor on October 14, 2022.
* CTPS_classification_script.py - Script implementing 7-level classification for LRTP Needs Assessment, proposed by Judy Tayor on November 2, 2022.