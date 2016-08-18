
# format will be { 'last name': [['person 1 Degree', 'person 2 Title', 'person 3 email]']
# format of second dict will be {(first name, last name): [Degree, Title, Email]
import csv, re

def read_csv(file):
    """Read the CSV file and return the list"""
    with open(file, 'rb') as csvfile:
        aggregate_list = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            aggregate_list.append(row)
    return aggregate_list

def replace_char(list_of_chars,replacement_char,target,key):
    """Remove list of characters from a target dictionary's items within a certain key"""
    for char in list_of_chars:
        for i in range(len(target)):
            target[i][key] = target[i][key].replace(char,replacement_char)
    return target

def remove_first_space_degree(list):
    """Cleans up titles by removing first space if existant"""
    for i in range(len(list)):
        if list[i][' degree'][0] == ' ':
            list[i][' degree'] = list[i][' degree'][1:]
    return list

def add_first_last_name(target_list):
    """Add first and last names to dictionary or abbreviation if no first name"""
    for i in range(len(target_list)):
        target_list[i]['first_name'] = re.split('\s+',target_list[i]['name'])[0]
        target_list[i]['last_name'] = re.split('\s+', target_list[i]['name'])[-1]
    return target_list

def get_unique_last_names(target):
    """Get unique set of last names for creating the first dictionary"""
    list_of_last_names = []
    for each in target:
        list_of_last_names.append(each['last_name'])
    unique_last_names = sorted(set(list_of_last_names))
    return unique_last_names


def create_empty_last_name_list(list):
    """Creates empty last name dictionary to be filled"""
    newdict ={}
    for each in list:
        newdict[each] = []
    return newdict

def create_last_name_ordered_dict(name_dict,source_list):
    """Create dictionary per question 6"""
    for key,value in name_dict.iteritems():
        for i in range(len(source_list)):
            if source_list[i]['last_name'] == key:
                name_dict[key].append([source_list[i][' degree'],
                                       source_list[i][' title'],
                                       source_list[i][' email']])
    return name_dict

def create_2nd_dict(source_list):
    """Create dictionary per question 7 """
    new_dict = {}
    for i in range(len(source_list)):
        new_dict[(source_list[i]['first_name'], source_list[i]['last_name'])] = [source_list[i][' degree'],
                                                                       source_list[i][' title'],
                                                                       source_list[i][' email']]
    return new_dict

def print_ordered_dict(dict):
    ordered_list = []
    for key,value in dict.iteritems():
        ordered_list.append([key, value])
    ordered_list = sorted(ordered_list,key = lambda x: x[0][1])
    for each in ordered_list:
        print str(each[0])+":"+str(each[1])


# Q6 Create a dictionary in a last-name ordered format ---------------------------------------------------

aggregate_list = read_csv('faculty.csv')

# Simplify title
new_list = replace_char(['of Biostatistics','is Biostatistics'],'',aggregate_list,' title')
new_list = add_first_last_name(new_list)
new_list = remove_first_space_degree(new_list)
last_names = get_unique_last_names(new_list)
empty_names_dict = create_empty_last_name_list(last_names)
new_dict = create_last_name_ordered_dict(empty_names_dict,new_list)
alt_list = create_2nd_dict(new_list)


# Prints the first three key and value paris of the dictionary
print "\nThe first dictionary's first three key value paris are as follows"
for i in range(0,3):
    print str(new_dict.keys()[i])+":"+str(new_dict.values()[i])
# --------------------------------------------------------------------------------------------------------

# Q7 Create a dictionary in a first_last_name ordered format-----------------------------------------------
print "\nThe alternative dictionary's first three key value paris are as follows"
for i in range(0,3):
    print str(alt_list.keys()[i])+":"+str(alt_list.values()[i])

# Q8 Print an ordered dictionary (by last name -----------------------------------------------------------
print "\nBelow is a print of the key value pairs for a dictionary ordered by last name"
print_ordered_dict(alt_list)



