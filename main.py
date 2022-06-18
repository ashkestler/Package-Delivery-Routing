# Name: Ashley Kestler  Student ID: 001484567

import datetime
from package import get_package_data, get_package_data_by_id
from truck import trucks, load_trucks
from schedule import load_distance_data, deliver_packages_at_time


# Initialization -------------------------------------------------------------------------------------------------------
# O(N^2) quadratic
def user_interface_init():
    load_distance_data()
    load_trucks()


# User Interface -------------------------------------------------------------------------------------------------------
# O(N^2) quadratic
def user_interface():
    print('Enter a time after 08:00 (in 24H time, i.e. 09:00 or 0900) to check package status or X to quit')
    user_input_time = input()
    if user_input_time == 'X':
        quit()
    try:
        if int(user_input_time[:2]) not in range(8, 24) or int(user_input_time[-2:]) not in range(0, 60):
            print('You have entered an invalid time. Please try again.')
            user_interface()
        else:
            h = int(user_input_time[:2])
            m = int(user_input_time[-2:])
            _time = datetime.time(h, m)
    except ValueError:
        print('You formatted the time incorrectly. Please try again.')
        user_interface()

    # deploy trucks according to user input time
    deliver_packages_at_time(_time)

    # Options menu
    # O(1) constant
    def options_menu():
        print('Choose an Option:')
        print('1: View All Package Data')
        print('2: Search for Package by ID')
        print('3: View Total Mileage for All Trucks')
        user_input = input('Enter a number 1-3: ')

        if user_input == '1':
            get_package_data()
            quit()
        elif user_input == '2':
            print('\nEnter the ID of the package you want to view:')
            package_id = int(input())
            get_package_data_by_id(package_id)
            quit()
        elif user_input == '3':
            total_mileage = 0
            print('\n')
            for truck in trucks:
                print('Truck #' + str(truck.id_num) + ' traveled', truck.total_route_mileage, 'miles.')
                total_mileage += truck.total_route_mileage
            print('The total mileage traveled by all trucks is', total_mileage, 'miles.')
            quit()

    options_menu()


# Main Function Calls --------------------------------------------------------------------------------------------------
user_interface_init()
user_interface()

