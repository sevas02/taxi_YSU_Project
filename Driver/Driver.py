import math

from Order.Order import Order
from Driver.Car import Car
from Timer import Timer


class Driver:
    """
    Class for storing data about drivers and managing them
    """

    def __init__(self,
                 car: Car,
                 full_name: str,
                 location: str, bank: str) -> None:
        self.__car = car
        self.__full_name = full_name
        self.__location = location
        self.__bank = bank
        self.__timer = Timer()
        self.__order_id = None
        self.__duration_trip = None
        self.__start_time = None

    def pick_up(self, new_order: Order):
        """
        A function that keeps the driver busy
        """
        self.__order_id = new_order.get_id
        self.__start_time = new_order.get_start_time

    def release(self):
        """
        Driver release function
        """
        self.__order_id = None
        self.__duration_trip = None
        self.__start_time = None

    @property
    def get_location(self):
        return self.__location

    @property
    def get_duration_trip(self):
        return self.__duration_trip

    @property
    def get_full_name(self):
        return self.__full_name

    @property
    def get_category(self):
        return self.__car.get_category
    
    @property
    def get_car(self):
        return self.__car

    @property
    def get_order_id(self):
        return self.__order_id

    @property
    def get_bank(self):
        return self.__bank

    def set_location(self, location: str):
        self.__location = location

    def set_duration_trip(self, dist_to_client, order_duration):
        self.__duration_trip = math.ceil(dist_to_client / 8.61 + order_duration)

    @property
    def is_finished(self) -> bool:
        if self.__timer.get_time - self.__start_time > self.__duration_trip:
            return True
        return False

    def print_info(self):
        self.__car.print_info()
        print("Driver: ", self.__full_name, self.__location, self.__bank, sep=' | ')
