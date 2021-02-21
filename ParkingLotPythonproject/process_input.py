#process_input.py
#!/usr/bin/env python
import fileinput
import sys

from parking_details import ParkingLot
from car import Car

parking_lot = ParkingLot()


def process(command_params):
    command_with_params = command_params.strip().split(' ')
    # print(command_with_params)
    command = command_with_params[0]

    if command == 'create_parking_lot':
        assert len(command_with_params) == 2, "create_parking_lot needs no of slots as well"
        assert command_with_params[1].isdigit() is True, "param should be 'integer type'"
        parking_lot.create_parking_lot(int(command_with_params[1]))

    elif command == 'park':
        assert len(command_with_params) == 3, "park needs registration number and color as well"
        car = Car(command_with_params[1], command_with_params[2])
        parking_lot.park(car)

    elif command == 'free':
        assert len(command_with_params) == 2, "free needs slot number as well"
        assert command_with_params[1].isdigit() is True, "slot number should be 'integer type'"

        parking_lot.free(int(command_with_params[1]))
    elif command == 'status':
        parking_lot.status()

    elif command == 'registration_numbers_for_cars_with_colour':
        assert len(command_with_params) == 2, "registration_numbers_for_cars_with_colour needs color as well"
        parking_lot.registration_numbers_for_cars_with_colour(command_with_params[1])

    elif command == 'slot_numbers_for_cars_with_colour':
        assert len(command_with_params) == 2, "slot_numbers_for_cars_with_colour needs color as well"
        parking_lot.slot_numbers_for_cars_with_colour(command_with_params[1])

    elif command == 'slot_number_for_registration_number':
        assert len(command_with_params) == 2, "slot_number_for_registration_number needs registration_number as well"
        parking_lot.slot_number_for_registration_number(command_with_params[1])

    elif command == 'exit':
        exit(0)
    else:
        raise Exception("Wrong command")


if len(sys.argv) == 1:
    while True:
        line = input()
        process(line)

else:
    for line in fileinput.input():
        process(line)