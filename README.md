# CL_Mining
A repository for an autonomous Craigslist Housing miner that extracts *all* housing information from every location in the world.<br>
**This tool should be used for data analysis and personal use.** 

<p align = 'center'>
<img src="https://i.imgur.com/umJAItc.png" alt="cover_photo" >
</p>

### How to use:
1) Clone the github repository onto your computer.<br>
2) Install the required Python libraries through pip:<br>
```pip install -r requirements.txt```<br>
3) If you are satisfied of downloading all housing information (i.e. apartments/housing, rooms offered, office space, etc.) from every Craigslist location in the globe, simply run this file in your terminal:<br>
```python multiprocessing_cl.py```<br>

### How to view data:
The ```multiprocessing_cl.py``` script will leverage (your CPU cores - 2) cores to work concurrently and extract craigslist housing information. The files are stored in a CSV format, with the following syntax:<br>
CraigslistHousing_{state/country}_{region/district}.csv<br>

An example of a file for Dothan, Alabama would look like this:<br>
CraigslistHousing_alabama_dothan.csv<br><br>
The user is presented with an option upon booting the multiprocessing script:<br>
```Would you like to search for geotagged results?[y/n]: ```<br>
Type ```y``` if you would like to receive geographic coordinates for every craigslist post:<br>
<img src="https://i.imgur.com/yguE95V.png" alt="geotag=True"><br><br>
Note: acquiring geotag results will take a considerable amount of time.<br>
To mitigate this, you may turn off geotagging option by typing ```n```:<br>
<img src="https://i.imgur.com/zQooOAE.png" alt="geotag=False"><br><br>

Your computer may sound like a jet airplane. Don't worry, it's not bad for your computer to use <a href=https://www.quora.com/Will-enabling-all-your-CPU-cores-be-harmful-or-damage-the-processor>multiple cores to perform a task</a>. The protocol will exit once the process is finished; otherwise, press ```CTRL + C``` in your operating terminal to exit the protocol.<br><br>

### Data
All data is stored as a .csv file in the ./Data directory of the repository.<br>

### Summary
This repository is useful if you are intereted in studying housing listings on Craigslist. However, there are two limitations in the repository's current state:<br>
1) Script only sources information from Craigslist Housing
2) Lack of GUI to facilitate facile selection of housing type(s), countries, etc.

