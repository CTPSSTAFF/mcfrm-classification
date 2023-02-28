# mcfrm-classification
Tools to 'classify' a  MC-FRM raster probability dataset according to various schemes, 
and to produce a multi-part polygon feature class from the classification.

### Inventory
* MBTA_classification.py - Script implementing classification used by the MBTA, and communicated to CTPS by Hannah Lyons-Galante in the spring of 2022.
* BOS_classification.py - Script implementing classification used by the City of Boston and discussed by Judy Tayor on October 14, 2022.
* CTPS_classification.py - Script implementing 7-level classification for LRTP Needs Assessment, proposed by Judy Tayor on November 2, 2022.

### CTPS Classiifcation Scheme
* probability >  0.10              - cell value = 7
* probability >= 0.05 and < 0.10   - cell value = 6
* probability >= 0.02 and < 0.05   - cell value = 5
* probability >= 0.01 and < 0.02   - cell value = 4
* probability >= 0.002 and < 0.01  - cell value = 3
* probability >= 0.001 and < 0.002 - cell value = 2
* probability <  0.001             - cell value = 1

### MBTA Classification Scheme
* probability >= 0.10              - cell value = 4
* probability >= 0.01  and < 0.10  - cell value = 3
* probability >= 0.002 and < 0.01  - cell value = 2
* probability >= 0.001 and < 0.002 - cell value = 1
* probability <= 0.001             - cell value = 0

### City of Boston Classification Scheme
* probability >= 0.05              - cell value = 4
* probability >= 0.02 and < 0.05   - cell value = 3
* probability >= 0.01 and < 0.02   - cell value = 2
* probability >= 0.002 and < 0.01  - cell value = 1
* probability >= 0.001 and < 0.001 - cell value = 0

### Script Parameterization
For all three scripts, the input raster dataset is hard-wired to the 2050 flood probability raster dataset for the 'North' towns.

#### CTPS Classifcation Script
The CTPS classification script takes two parameters:
* the 'working' File GeoDatabase
* the final output multi-part polygon feature class

## MBTA and City of Boston Classification Scripts
These scripts \(MBTA_classificaiton.py and BOS_classification.py\) are currently _not_ parameterized.
That is to say, the following are currently hard-wired in them:
* the 'working' File GeoDatabase
* the final output multi-part polygon feature class
Parameterization of these two scripts will be implemented should the need arise if time and human resources are available.
The intention was to get a baseline working version of each these tools under version control sooner rather than later.
