# CL_Mining
Welcome to **CL_Mining**, a web scraping tool that extracts information from *every* Craigslist Housing post from around the world.<br>
**Note:** This tool should only be used for personal use and data analysis.

<p align = 'center'>
<img src="https://i.imgur.com/umJAItc.png" alt="cover_photo" >
</p>

### How to use:
1) Clone the github repository onto your computer.<br>
2) Install the required Python libraries through pip:<br>
```pip install -r requirements.txt```<br>
3) If you are satisfied of downloading all housing information (i.e. apartments/housing, rooms offered, office space, etc.) from every Craigslist location in the globe, simply run this file in your terminal:<br>
```python multiprocessing_cl.py```<br>

The ```multiprocessing_cl.py``` script will leverage (no. CPU cores on your computer - 2) CPU cores to extract craigslist housing information. The files are stored in a CSV format with the following syntax:<br>
CraigslistHousing_{state/country}_{region/district}.csv<br>

An example of a .csv file for Dothan, Alabama would look like this:<br>
CraigslistHousing_alabama_dothan.csv<br><br>
The user is given an option upon starting the multiprocessing script:<br>
```Would you like to search for geotagged results?[y/n]: ```<br>
Type ```y``` if you would like to receive geographic coordinates for every craigslist post:<br>
<img src="https://i.imgur.com/yguE95V.png" alt="geotag=True"><br><br>
Note: acquiring geotag results will take a considerable amount of time.<br>
To mitigate this, you may turn off geotagging option by typing ```n```:<br>
<img src="https://i.imgur.com/zQooOAE.png" alt="geotag=False"><br><br>

Your computer may sound like a jet airplane. Don't worry, it's not bad for your computer to use <a href=https://www.quora.com/Will-enabling-all-your-CPU-cores-be-harmful-or-damage-the-processor>multiple CPU cores</a>. The protocol will exit once the process is finished; otherwise, press ```CTRL + C``` in your operating terminal to exit the protocol.<br>

### Data
All data is stored as a .csv file in the ./Data/{date_data_acquired} directory.<br>
For example:<br>
./Data/2019-11-15<br>

### Summary
The **CL_Mining** tool is useful if you are intereted in studying housing posts on Craigslist. However, there are two limitations in the tool's current state:<br>
1) Only sources information from Craigslist Housing
2) Lack of GUI to facilitate facile selection of housing type(s), countries, etc.

These features are scheduled to be implemented in the near future!<br><br>
**Fin**

