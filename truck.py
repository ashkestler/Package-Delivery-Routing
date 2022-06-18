from package import set_package_data, packages_hash_table
from datetime import time

packages_manually_placed = None
trucks = []
HUB = '4001 South 700 East'
MAX_CAPACITY = 16
set_package_data()


# Initialization  ------------------------------------------------------------------------------------------------------
# initialize truck class
class Truck:
    # O(1) constant
    def __init__(self, time_left_hub, location, total_route_mileage, package_count):
        self.time_left_hub = time_left_hub
        self.location = location
        self.total_route_mileage = total_route_mileage
        self.package_list = set()
        self.package_count = package_count
        self.id_num = None

    # adds package to truck
    # O(1) constant
    def add(self, package):
        self.package_list.add(package)
        self.package_count = len(self.package_list)

    # removes package from truck
    # O(1) constant
    def remove(self, package):
        self.package_list.remove(package)
        self.package_count = len(self.package_list)


# create truck objects
# O(1) constant
def create_new_truck(time_left_hub, location=HUB, total_route_mileage=0, package_count=0):
    new_truck = Truck(time_left_hub, location, total_route_mileage, package_count)
    trucks.append(new_truck)
    new_truck.id_num = trucks.index(new_truck) + 1


create_new_truck(time(8, 00))
create_new_truck(time(9, 5))
create_new_truck(time(11, 00))


# packages manually placed based on project requirements
def load_packages_manually(truck_id, id_list):
    global packages_manually_placed
    truck = trucks[truck_id - 1]
    if packages_manually_placed is None:
        packages_manually_placed = set()
    for id_num in id_list:
        new_package = packages_hash_table.search(id_num)
        truck.add(new_package)
        packages_manually_placed.add(id_num)


load_packages_manually(1, [13, 14, 15, 16, 19, 20])
load_packages_manually(2, [3, 6, 18, 25, 36, 38])
load_packages_manually(3, [9, 28, 32])


# sort unloaded packages by deadline
# O(N^2) quadratic
def packages_sorted_by_deadline():
    deadline_list = []
    if packages_manually_placed is not None:
        for id_num in range(1, len(packages_hash_table.table) + 1):
            if id_num not in packages_manually_placed:
                package = packages_hash_table.search(id_num)
                deadline_list.append(package)
    else:
        for id_num in range(1, len(packages_hash_table.table) + 1):
            package = packages_hash_table.search(id_num)
            deadline_list.append(package)
    deadline_list.sort(key=lambda _package: _package.deadline)
    return deadline_list


# sort unloaded packages onto trucks prioritized by deadline
# O(N^2) quadratic
def load_trucks():
    trucks_sorted_by_time = sorted(trucks, key=lambda _truck: _truck.time_left_hub)
    for package in packages_sorted_by_deadline():  # O(N^2)
        for truck in trucks_sorted_by_time:
            if truck.package_count < MAX_CAPACITY:
                truck.add(package)
                break

