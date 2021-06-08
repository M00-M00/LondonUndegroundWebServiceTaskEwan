import csv 
import pandas as pd
from app import db
from app.models import station, line

df = pd.read_csv("london_stations.csv")

def split_lines(all_lines):
    lines = all_lines.split(" ")
    return lines


def split_lines(all_lines):
    lines = all_lines.replace(",", "")
    lines = lines.replace("Hammersmith & City", "Hammersmith&City")
    lines = lines.split(" ")
    print (lines)
    return lines

def get_lines(df):
    all_lines = df.LINES.unique()
    all_lines_single = [str(line).split(" ")[0] for line in all_lines]  
    unique_lines = list(dict.fromkeys(all_lines_single))
    unique_lines2 = [l.split(",")[0] for l in unique_lines]
    ul3 = list(dict.fromkeys(unique_lines2))
    ul3.remove("nan")
    ul3.remove("Hammersmith")
    ul3.append("Hammersmith&City")
    unique_lines = ul3
    return unique_lines

unique_lines = get_lines(df)


def list_of_stations(df):
    df_filter_network  =  df.loc[df['NETWORK'] == 'London Underground']
    #turns lineS str to a list of str 
    df_filter_network["LIST_LINES"] = [split_lines(x) for x in df_filter_network["LINES"]]
    london_undergound_list  = [london_undergound_dict[x] for x in london_undergound_dict]
    return london_undergound_list



def update_db():
    london_undergound_list = list_of_stations(df)
    unique_lines = get_lines(df)
    line.update_db(unique_lines)
    station.update_db(london_undergound_list)
