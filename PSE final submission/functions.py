#class for finding the available room based on search riteria (e.g. equipment/ timeslot)
class find_available_room: 
    def __init__(self, room_data, givenCriteria, search_choice):
        self.room_data = room_data
        self.criteria = givenCriteria
        self.choice = search_choice
    #function for returning all available rooms based on search criteria
    def search(self):
        avail_rooms = []
        for col in self.room_data:
            for key, value in col.items():
                if self.choice == "time slot":
                    available_slots = col["Time Slots"]
                    if self.criteria in available_slots:
                        room_name = col ["Name"]
                elif self.choice == "equipment":
                    room_equipment = col["Equipment"]
                    if self.criteria in room_equipment:
                        room_name = col ["Name"]
                if room_name not in avail_rooms:
                            avail_rooms.append(room_name)
        return avail_rooms

#function for returning the room specifications
def show_room_details(room_data,num):
    for col in room_data:
        for key, value in col.items():
            if value == num:
                return col

#function for booking a room
def book_room(room_data, booking_data, num, period):
    #insert booking history details
    temp_dict = {}
    temp_dict['room_name'] = num
    temp_dict['time_booked'] = period
    booking_data.append(temp_dict)
    #remove the selected timeslot from the room availability
    for col in room_data:
        for key, value in col.items():
            if value == num:
                timeslots = col["Time Slots"]
                timeslots.remove(period)

#function for checking if a particular room still has available time slots
def check_availability(room_data, num):
    for col in room_data:
        for key, value in col.items():
            if value == num:
                if len(col["Time Slots"])>0:
                    return True
                else:
                    return False

#search available based on input capacity             
def search_capacity (room_data, capacity):
    avail_rooms = []
    for col in room_data:
        for key, value in col.items():
            col_capacity = int(col["Capacity"])
            if col_capacity >= capacity:
                room_name = col ["Name"]
                if room_name not in avail_rooms:
                    avail_rooms.append(room_name)
    return avail_rooms

