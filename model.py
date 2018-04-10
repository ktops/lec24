#model.py
import csv

BB_FILE_NAME = 'umbball.csv'

bb_seasons = []

def init_bball(csv_file_name=BB_FILE_NAME):
    global bb_seasons
    with open(csv_file_name) as f:
        csvReader = csv.reader(f)
        next(csvReader, None)
        next(csvReader, None)
        global bb_seasons
        bb_seasons = []

        for row in csvReader:
            row[3] = int(row[3])
            row[4] = int(row[4])
            row[5] = float(row[5])
            bb_seasons.append(row)

def get_bball_seasons(sortby='year', sortorder='desc'):
    if sortby == 'year':
        sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    sorted_list = sorted(bb_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list
