import re, csv, collections

# Question 1 - List and count of degrees -------------------------------------------------------------------------------

# Useful functions ---------------------------------------------------------------------------------------------------
list = []

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

# Step 2 - Get a list of all titles

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


def remove_char_from_list(list_of_chars,replacement_char,target):
    """Cleans a list by removing certain characters from a target list"""
    for char in list_of_chars:
        for i in range(len(target)):
            target[i] = target[i].replace(char,replacement_char)
    return target


def return_unique_counts(list):
    """Returns a counter for unique items"""
    for key, value in collections.Counter(list).iteritems():
        print key, value

def get_domains_from_emails(email_list, domain_column):
    domain_list = []
    for i in range(len(email_list)):
        email_list[i] = re.split('@', email_list[i])
        domain_list = [x[domain_column] for x in email_list]
    return domain_list

# Procedure for Question 1 --------------------------------------------------------------------------------------------
list = remove_header(read_csv('faculty.csv'))
degree_list = get_list_items(list, 1, '\s')
degree_list = remove_char_from_list(['.', ' '],'',degree_list)

print "The list and counts of unique degrees is as follows:"
return_unique_counts(degree_list)

# Question 2 - List of different titles and frequencies ----------------------------------------------------------------

title_list = get_list_items(list,2)
# Clean up mistake in one of the titeles
title_list = remove_char_from_list(['is '],'of ',title_list)

print "\nThe list and counts of unique titles is as follows:"
return_unique_counts(title_list)

# Question 3 - Search for email addresses and put them in a list -------------------------------------------------------

# Note - This could also be achieved by parsing each line for the @sign
print "\nThe list of emails is as follows"
email_list = get_list_items(list,3)
for each in email_list:
    print each

# Question 4 - Find how many different email domains there are --------------------------------------------------------

print "\nThe list of unique domains is as follows:"
return_unique_counts(get_domains_from_emails(email_list,1,))

