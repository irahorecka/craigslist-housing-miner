# CL_Mining
A repository to create an autonomous Craigslist Housing miner to extract all housing information from every location in the world. This tool should be used for data analysis and personal use. 

### How to use:
1) Clone the github repository onto your computer.<br>
2) Install the required Python libraries through pip:<br>
```pip install -r requirements.txt```<br>
3) If you are satisfied of downloading all housing information (i.e. apartments/housing, rooms offered, office space, etc.) from every Craigslist location in the globe, simply run this file in your terminal:<br>
```python multiprocessing_cl.py```<br>

### How to view data:
The ```multiprocessing_cl.py``` script will leverage all of your CPU cores to work concurrently in writing craigslist housing information onto your computer. The files are stored in a CSV format, with the following syntax:<br>
CraigslistHousing_{state/country}_{region/district}.csv<br>

An example of a file for Dothan, Alabama would look like this:<br>
CraigslistHousing_alabama_dothan.csv<br><br>
The user is presented with an option upon booting the multiprocessing script:<br>
```Would you like to search for geotagged results?[y/n]: ```<br>
Type ```y``` if you would like to receive geographic coordinates for every craigslist post.<br>

