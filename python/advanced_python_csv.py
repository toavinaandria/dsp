import csv, re

def read_csv(file):
    """Read the CSV file and return the list"""
    with open(file, 'rb') as csvfile:
        aggregate_list = []
        reader = csv.reader(csvfile)
        for row in reader:
            aggregate_list.append(row)
    return aggregate_list

def remove_header(list):
    """Remove header from the list"""
    list.pop(0)
    return list

def get_list_items(list, column, separator=''):
    """Return a list of all items from a list within a certain column, separating items by the separator variable"""
    new_list = []
    for item in list:
        new_list.append(item[column])
    # Get individual titles that are separated by blank spaces
    for i in range(len(new_list)):
        new_list[i] = re.split(separator,new_list[i])
    # Remove blank spaces and flatten the list
    return [item for sublist in new_list for item in sublist if item != '']

def list_of_list(list):
    return [[x] for x in list]

def write_csv(target_file,source):
    with open(target_file, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for each in source:
            writer.writerow(each)

# procedure
list = read_csv('faculty.csv')
email_list = list_of_list(remove_header(get_list_items(list,3)))
write_csv('emails.csv',email_list)






