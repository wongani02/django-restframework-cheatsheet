import xhtml2pdf
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
# def reg_no_validator(value):
#
#     if len(value) <14:
#         print('does not match reg number')
#
#
#
#
# reg_no_validator('wongani')
l1 = ['1', '2']
from django.contrib.sessions.backends.db import SessionStore

class SelectedSeats:

     def __init__(self, seats=[]):
         self.seats = seats

     def getSeats(self):
         for item in self.seats:
             print(str(item))


seat_numbers = SelectedSeats(seats=l1)
seat_numbers.getSeats()