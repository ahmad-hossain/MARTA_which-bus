import pandas as pd
import requests
from bs4 import BeautifulSoup

ROOT_URL = 'https://itsmarta.com/'
EXT = '.aspx'
BUS_ROUTES_URL = 'https://www.itsmarta.com/bus-routes.aspx'
TRAIN_LINES_URL = 'https://www.itsmarta.com/railline-schedules.aspx'
TRAIN_STATIONS_URL = 'https://itsmarta.com/train-stations-and-schedules.aspx'

def main():
    #prompt the user to enter the station they are leaving from
    #as well as the destination bus stop
    make_choices()

#todo in future, let train and bus be chosen at same time
def make_choices():

    valid_input = False

    #Loop until valid input is entered
    while not valid_input:

        #get station name and bus stop
        print('This script allows you to find which buses at a certain station are going to your desired bus stop.')
        station_choice = input('Enter the TRAIN STATION: ')
        bus_stop_choice = input('Enter the desired BUS STOP: ')

        #todo check if station and bus are valid
        if valid_choices(station_choice, bus_stop_choice):
            valid_input = True
            
        #if user enters invalid input
        else:
            print("Invalid input. Please try again.")

#checks if the inputs are a valid train station and bus stop
def valid_choices(station: str, bus_stop: str) -> bool:
    
    #get dictionary of stations and their page urls
    stations_dict = get_stations()
    
    #if user entered station not in stations_dict keys
    if station.lower() not in stations_dict:
        return False
    #user entered station does exist, so check if user can reach desired bus stop from the station
    else:
    #todo check saved dataframes for the desired stop. dfs will be saved as csv in a folder that has the rail station and bus stop name

    #todo if saved dataframes not found, parse and save dataframes that have the desired stop

    #todo check the schedule for every bus at the station and see if bus_stop is a destination. If it is, save it
    #check if any key in get_buses() starts 
        return
    
def get_stations() -> dict[str, str]:
    soup = get_soup(TRAIN_STATIONS_URL)

    #get the div that holds all the station names and url elements 
    stations_container = soup.find('div', class_='stations__items isotope')

    #create dict for stations where station name is key and url is the value.
    stations_dict = {}

    #loop through all the train stations in the container div. All stations are in an <a> element with the text as the station name
    #and the href as the relative path to the station page
    for station_element in stations_container.findAll('a', href=True):
        
        #populate dictionary with station information. Key is lowercase. Example: {'airport': 'Airport.aspx'}
        stations_dict[station_element.text.lower()] = station_element['href']
    
    return stations_dict

def get_buses() -> dict[str, str]:
    return

def get_soup(url: str) -> BeautifulSoup:
    html = requests.get(url)

    #raise exception if there's a response error
    try:
        html.raise_for_status()
    except:
        print(f"Error reaching {url}")
    
    return BeautifulSoup(html.text, 'html.parser')

#parse table for a MARTA bus page
def parse_bus_table(df: pd.core.DataFrame) -> pd.core.frame.DataFrame:
    #When parsing bus table, the 1st col is all NaN values.
    #Check if first col has NaN values
    if df.iloc[:,0].isnull().values.any():
        df = df.drop(df.columns[0], axis=1)

    #alternative method:
    #drop all columns that have NaN values
    #df.dropna(axis=1, inplace=True)
    return

if __name__ == "__main__":
    main()