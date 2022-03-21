"""
1st Functionality: View the detail of any specified room (e.g. 2.005), including capacity, equipment, location, availability, etc.,

2nd functionality: book the room if there are available timeslots (Assumption: Booking for only on a particular day)

3rd functionality: Search available room based on given criteria, including time slots, equipment and capacity
"""
#The ast module helps Python applications to process trees of the Python abstract syntax grammar. 
#Docs.python.org. 2021. ast — Abstract Syntax Trees — Python 3.7.12 documentation. [online] Available at: <https://docs.python.org/3.7/library/ast.html> [Accessed 26 December 2021].
import ast
#import all the functions from function.py
from functions import *

#read in all the text from room.txt
f = open("room.txt", "r")
data = f.read()
#tranform all the text into the dictionary through using function from ast module
room_data = ast.literal_eval(data)
#initialize storage for storing booking data
booking_data = []
#set the booking status as true
booking_status = True

#Start the booking process
while booking_status == True:
    try:
        #prompt the user for selecting search criteria
        search_choice = input("Please select search option: (room number/ time slot/ capacity/ equipment)") 
        #when the user input room number   
        if search_choice == "room number":   
            try:
                room_number = input("Please enter the room number you want to search: ")  
            #store the room specifications into a variable
                details = show_room_details(room_data, room_number)
                #print out the details in key and value pairs
                for k, v in details.items():
                    print(k ,":", v)
            #exception handling
            except AttributeError:
                print("There is no room with this number. please reselect the search option.")
        #when the user's input is time slot
        elif search_choice == "time slot":     
            time_slot = input("Please enter the timeslot you want to book a room(e.g. 10:00-11:00):  ") 
            #create an instance of the object
            search_timeslot1 = find_available_room(room_data, time_slot, search_choice)
            #store all the available rooms which has the specified time slot 
            rooms = search_timeslot1.search()
            print(rooms)
            room_number = input("Please enter the room number you want to book: ")
        #when the user's input is capacity
        elif search_choice == "capacity":
            #prompt the user to input the capacity needed
            capacity = int(input ("Please enter the maximum capacity needed (1-292): "))
            #store all the available rooms which has the specified capacity
            rooms = search_capacity(room_data, capacity)
            print(rooms)
            room_number = input("Please enter the room number you want to book: ")
        
        #when the user's input is equipment
        elif search_choice == "equipment":
            #prompt the user to input the equipment to be included for the room
            equipment = input ("Please enter equipment required for the room: ")
            search_equipment1 = find_available_room(room_data, equipment, search_choice)
            rooms = search_equipment1.search()
            print(rooms)
            room_number = input("Please enter the room number you want to book: ")
        
        #check the availability of the selected room
        availability = check_availability(room_data, room_number)
        #when the room is available
        if availability == True:
            booking = " "
            while (booking != 'y' and booking != 'n'):
                #ask the user whether or not to book this room
                booking = input("Would you like to book this room: (y/n): ")
            #whenthe user input y as yes
            if booking == "y":
                #ask the user to type in the booking time slot 
                period = input("Please enter the timeslot you want to book (e.g. 10:00-11:00): ")   
                #insert the booking data into the database 
                book_room(room_data, booking_data, room_number, period)
            elif booking == "n":
                booking_status = True
            #ask the user whether he/she wants to book another room
            next_booking = " "
            while (next_booking != 'T' and next_booking != 'F'):
                next_booking = input("Please indicate if you want to book another room (T/F): ")
            #continue the booking if users input T as True
            if next_booking == "T":
                booking_status = True
            else:
                booking_status = False
        #ask the user to select another room when all the timeslots are booked
        elif availability == False:
            print("This room is currently unavailable, please select another room")
        
    except NameError:
        print("input is invalid") 
         
#print out all the booking data stored in dictionary
print("All Booking Records")
for i in range (len(booking_data)):
    print ("Booking ID: ", i+1 )
    for k, v in booking_data[i].items():
        print(k, ":", v)

