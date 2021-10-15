import pandas as pd
import requests
from bs4 import BeautifulSoup

ROOT_URL = 'https://itsmarta.com/'
EXT = '.aspx'
BUS_ROUTES_URL = 'https://www.itsmarta.com/bus-routes.aspx'
TRAIN_LINES_URL = 'https://www.itsmarta.com/railline-schedules.aspx'
TRAIN_STATIONS_URL = 'https://itsmarta.com/train-stations-and-schedules.aspx'

def main():
    
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
        if valid_choices():
            valid_input = True
            
        #if user enters invalid input
        else:
            print("Invalid input. Please try again.")

def valid_choices(station: str, bus_stop: str) -> bool:
    #todo check if station exists first by either using station list OR requesting webiste
    soup = get_soup(TRAIN_STATIONS_URL)

    #get the div that holds all the station names and url elements 
    container = soup.find('div', class_='stations__items isotope')

    #create dict for stations where station name is key and url is the value
    stations_dict = {}

    #loop through all the train stations in the container div
    for station_element in container.findAll('a', href=True):
        #populate dictionary with station information
        stations_dict[station_element.text] = station_element['href']


    #todo if station DOES exist, check saved dataframes for the desired stop
    #todo if saved dataframes not found, parse and save dataframes that have the desired stop
    #? only save dfs for the desired stops??


def get_soup(url: str) -> BeautifulSoup:
    html = requests.get(url)

    #check for a response error
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
        df.drop(df.columns[0], axis=1) #inplace=true

    #drop all columns that have NaN values
    #df.dropna(axis=1, inplace=True)
    return


#parse a table for any MARTA page with a table    
def parse_table(url: str) -> pd.core.frame.DataFrame:
    return

if __name__ == "__main__":
    main()