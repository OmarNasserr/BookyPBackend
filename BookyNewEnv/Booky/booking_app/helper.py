from .models import Booking
from playground_app.models import Playground

from rest_framework.response import Response
from rest_framework import status
import datetime


class BookingAppHelper():

    # this function is given the playground_id, date, and total hours_available from
    # playground.start_time to playground.end_time to be
    # booked, then it compares the total hours available with the already booked hours in the
    # booking table and only return the available hours that yet to be booked
    def get_playground_available_booking_hours(playground_id, date, hours_available):
        
        FMT = '%H:%M:%S'
        playground_booked_times = Booking.objects.filter( #return all the bookings for specific playground
            playground_id=playground_id,                  #on a specific date
            date=date
        )
        
        to_be_removed=[]    #we add booked hours to this list to be removed later, as if we removed
                            #directly from the main list some iterating problems were raised in indexing
        
        if playground_booked_times.exists():            #if no bookings were found, return the hours_available list
            for hour in hours_available:                #which is basically the all time slots from 
                for booking in playground_booked_times: #playground.open_time to playground.close_time
                    
                    if  datetime.datetime.strptime(
                        booking.start_time, FMT
                    ).time() > hour or  datetime.datetime.strptime(
                        booking.end_time, FMT
                    ).time() <= hour :
                        
                                    #this condition treats bookings as a timeline, therefore it checks if an
                        pass        #hour lies between a start and end of a booking.
                                    #for an hour to be removed from the list (which means it's already booked)
                    else: 
                                                        #it has to be greater than already existing booking.start_time
                        to_be_removed.append(hour)      #and less than already existing booking.end_time
                                                        #if and hour satisfies the two conditions then it means
        else:                                           #that this hour lies between already existing 
            return hours_available                      #booking.start_time and booking.end_time or it's 
                                                        #the booking.start_time itself
                                #timeline   <---booking.start_time-----------hour-----------booking.start_time--->
                                
        for remove in to_be_removed:
            try:                                      
                hours_available.remove(remove)   
            except:
                pass
          
        return hours_available


    #this function is given the booking start time and end time
    #and returns the hours to be booked
    def get_hours_to_be_booked(b_start_time, b_end_time):
        to_be_booked_hours=[]
        while b_start_time < b_end_time:
                to_be_booked_hours.append(b_start_time)

                b_start_time = b_start_time.replace(hour=b_start_time.hour + 1)
        
        return to_be_booked_hours