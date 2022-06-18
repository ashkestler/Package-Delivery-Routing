import datetime
import math
import csv
from package import update_package_address, deliver_package, Package
from truck import trucks

distance_data_list = []
address_list = []
TRUCK_SPEED = 18


def load_distance_data():
    with open('./data/address_data.csv') as address_data:
        address_data_csv = csv.reader(address_data, delimiter=',')
        global address_list

        for row in address_data_csv:
            address_list.append(row[0])

    with open('./data/distance_data.csv') as distance_data:
        distance_data_csv = csv.reader(distance_data, delimiter=',')
        global distance_data_list

        for row in distance_data_csv:
            distance_data_list.append(list(row))


# get distance between two addresses in miles
# O(1) constant
def distance_between(address1, address2):
    distance = distance_data_list[address_list.index(address1)][address_list.index(address2)]
    if distance == '':
        distance = distance_data_list[address_list.index(address2)][address_list.index(address1)]

    return float(distance)


# find the closest address to current address
# O(N) linear
def get_next_location(from_address, truck_packages):
    _min = 2000
    closest_address = ''
    deliver_this = None

    for package in truck_packages:
        this_distance = distance_between(from_address, package.address)
        if this_distance < _min:
            deliver_this = None
            _min = this_distance
            closest_address = package.address

        if package.address == closest_address:
            if deliver_this is None:
                deliver_this = package
            elif isinstance(deliver_this, Package):
                temp_list = [deliver_this, package]
                deliver_this = temp_list
            elif isinstance(deliver_this, list):
                deliver_this.append(package)

    return closest_address, _min, deliver_this


# find the travel time for distance between current address and next address
# O(1) constant
def get_time_delta(miles):
    travel_time_hours = math.trunc(miles / TRUCK_SPEED)
    travel_time_mins = math.trunc((miles / TRUCK_SPEED) * 60) - (travel_time_hours * 60)
    travel_time_secs = math.trunc(((miles / TRUCK_SPEED) * 60) * 60) - (travel_time_mins * 60)
    time_delta = datetime.timedelta(hours=travel_time_hours, minutes=travel_time_mins, seconds=travel_time_secs)

    return time_delta


# find the most optimized route based on shortest distance and deliver packages on truck
# O(N^2) quadratic
def deliver_packages_on_truck(user_input_time, truck):
    update_package_address(user_input_time)
    curr_time = datetime.datetime.combine(datetime.date.today(), truck.time_left_hub)
    while truck.package_count > 0:
        next_location = get_next_location(truck.location, truck.package_list)
        truck.location = next_location[0]
        miles_to_next_location = next_location[1]
        packages_to_be_delivered = next_location[2]
        curr_time += get_time_delta(miles_to_next_location)
        truck.total_route_mileage += miles_to_next_location

        if isinstance(packages_to_be_delivered, list):
            for package in packages_to_be_delivered:
                deliver_package(user_input_time, curr_time, package, truck)
        else:
            deliver_package(user_input_time, curr_time, packages_to_be_delivered, truck)


# deploy trucks according to user input time
# O(N^2) quadratic
def deliver_packages_at_time(user_input_time):
    for truck in trucks:
        if user_input_time >= truck.time_left_hub:
            deliver_packages_on_truck(user_input_time, truck)







