# mcfrm-classification
Tools to 'classify' a  MC-FRM raster probability dataset according to various schemes, 
and to produce a multi-part polygon feature class from the classification.

Inventory:
* MBTA_classification.py - Script implementing classification used by the MBTA, and communicated to CTPS by Hannah Lyons-Galante in the spring of 2022.
* BOS_classification.py - Script implementing classification used by the City of Boston and discussed by Judy Tayor on October 14, 2022.
* CTPS_classification.py - Script implementing 7-level classification for LRTP Needs Assessment, proposed by Judy Tayor on November 2, 2022.
 
Two of these scripts \(MBTA_classificaiton.py and BOS_classification.py\) are currently _not_ parameterized.
That is to say, the following are currently hard-wired in them:
* the input raster dataset
* the 'working' File GeoDatabase
* the final output multi-part polygon feature class

Parameterization of these two scripts will be implemented should the need arise if time and human resources are available.
The intention was to get a baseline working version of each these tools under version control sooner rather than later.
