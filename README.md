# craigslistHousingMiner
Welcome to **craigslistHousingMiner**, a web scraping tool that extracts information from up to *every* Craigslist Housing post around the world.<br>
**Note:** This tool should only be used for personal use and data analysis.

<p align = 'center'>
<img src="https://i.imgur.com/umJAItc.png" alt="cover_photo" >
</p>

## About the application
This project leverages asynchronous execution of processes to rapidly mine information from Craigslist Housing posts. The data is written to CSV in the following format:<br>```CraigslistHousing_{country/state}_{region/subregion}.csv```

An example of a CSV file for Dothan, Alabama would look like this:<br>
```CraigslistHousing_alabama_dothan.csv```<br><br>
Another example of a CSV file for Tokyo, Japan would look like this:<br>
```CraigslistHousing_japan_tokyo.csv```<br><br>

## Running the application
1) Clone this github repository.<br>
2) Install the required dependencies:<br>
```pip install -r requirements.txt```<br>
3) Run ```main.py```:<br>
```python main.py```<br>


The user is given two prompts:<br>
```Input a list of appropriate countries.```<br>
```If no list is provided, a global search will be conducted: ```<br><br>
Input a list of appropriate country keywords in which you would like to search. You may find the full list of country keywords <a href="https://i.imgur.com/WGARByx.png">here</a>. For example:<br>
```['united_states', 'japan', 'canada']```<br><br>

```Would you like to include geotags of your Craigslist posts [y/n]: ``` <br>
Type ```y``` if you would like to receive geographic coordinates for every craigslist post:<br>
<img src="https://i.imgur.com/rkjO94O.png" alt="geotag=True"><br><br>
**Note:** acquiring geotags will take a considerable amount of time.<br>
To mitigate this, you can omit geotags by typing ```n```:<br>
<img src="https://i.imgur.com/4Yl2zN6.png" alt="geotag=False"><br><br>

The application will exit once the process is finished; otherwise, you may have to repeatedly press ```CTRL + C``` in your operating terminal to properly exit the application.<br>

## Data
All data is stored in the ```craigslistHousingMiner/data/{date data acquired}``` directory.<br>
For example:<br>
```craigslistHousingMiner/data/2020-06-14```<br>

## Summary
**craigslistHousingMiner** is a useful tool if you are intereted in studying housing posts on Craigslist. However, there are two limitations in the tool's current state:<br>
1) The current state of the project is not a PyPI library.
2) Lack of GUI to facilitate easy selection of housing type(s), countries, regions, etc.

These features are scheduled to be implemented in the near future.<br><br>
**Fin**
