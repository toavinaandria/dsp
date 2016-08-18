# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

def read_csv(file):
    aggregate_list = []
    with open(file, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            aggregate_list.append(row)
    return aggregate_list

def remove_csv_header(list):
    list.pop(0)
    return list

def list_goal_diff(list):
    new_list = []
    for each in list:
        new_list.append([each[0],abs(int(each[5])-int(each[6]))])
        new_list.sort(key = lambda x:x[1])
    return new_list


def procedure(file):
    return list_goal_diff(remove_csv_header(read_csv(file)))

print 'The team with the smallest difference in for and against goals is '+procedure('football.csv')[0][0]
