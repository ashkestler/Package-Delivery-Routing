import csv
from datetime import time
from datastructures.hash_table import HashTable

# Initialization  ------------------------------------------------------------------------------------------------------
# create package hash table
# O(N) linear
packages_hash_table = HashTable(40)


class Package:
    def __init__(self, id_num, address, city, zipcode, deadline, weight, status):
        self.id_num = id_num
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.delivery_time = None

    def __str__(self):
        string_obj = self.id_num, self.address
        return str(string_obj)


# Package Functions ----------------------------------------------------------------------------------------------------
# set package data to hash table from CSV
# O(N) linear
def set_package_data():
    with open('./data/package_data.csv') as package_file:
        package_data = csv.reader(package_file, delimiter=',')

        for row in package_data:
            # time conversion
            if row[5] == '9:00 AM':
                row[5] = time(9, 00)
            elif row[5] == '10:30 AM':
                row[5] = time(10, 30)
            elif row[5] == 'EOD':
                row[5] = time(17, 00)
            # assign object attributes
            id_num = int(row[0])
            address = row[1]
            city = row[2]
            zipcode = row[4]
            deadline = row[5]
            weight = int(row[6])
            status = 'At hub'

            new_package = Package(id_num, address, city, zipcode, deadline, weight, status)
            packages_hash_table.insert(id_num, new_package)


# formatted search for all package data
# O(N) linear
def get_package_data():
    print('\nPackage Data:')
    for i in range(1, len(packages_hash_table.table) + 1):
        p = (packages_hash_table.search(i))
        print('Package ID:', p.id_num, '| Address:', p.address, '| City:', p.city, '| Zip:',
              p.zipcode, '| Deadline:', p.deadline.strftime("%H:%M"), '| Weight:', p.weight, '| Status:', p.status)


# formatted search for specific package data by ID
# O(1) constant
def get_package_data_by_id(user_input):
    p = packages_hash_table.search(user_input)
    print('\nRequested Package Data: ')
    print('Package ID:', p.id_num, '| Address:', p.address, '| City:', p.city, '| Zip:',
          p.zipcode, '| Deadline:', p.deadline.strftime("%H:%M"), '| Weight:', p.weight, '| Status:', p.status)


# updates incorrect address if user input time is after 10:20AM per project requirements
# O(1) constant
def update_package_address(user_input_time):
    if user_input_time >= time(10, 20):
        package = packages_hash_table.search(9)
        package.address = '410 S State St'
        package.city = 'Salt Lake City'
        package.zipcode = '84111'


# updates status of specified package according to user input time
# O(1) constant
def update_status(user_input_time, package):
    delivery_time = package.delivery_time.time()
    if user_input_time < delivery_time:
        package.status = 'En route'
    else:
        package.status = 'Delivered at ' + str(delivery_time)


#
def deliver_package(user_input_time, delivery_time, package, truck):
    package.delivery_time = delivery_time
    update_status(user_input_time, package)
    truck.remove(package)
