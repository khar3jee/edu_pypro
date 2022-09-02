"""
Chapter 3
Example Greeter for e-commerce sight

Goal: refactor get_day and get_time_of_day into
functions outside of Greeter class
"""

from datetime import date as d, datetime as dt

class Greeter():
    """example e-commerce greeter"""

    def __init__(self):
        """greeter attributes, store name"""
        self.store_name = 'Super Awesome Store of Things'
        self.coupon = '20%'

    def greet(self):
        """
        Calls _get_day, _time_of_day and 
        prints greeting
        """
        day = get_day()
        time = get_time_of_day()
        print(f"Hi, welcome to {self.store_name}!\
        \nHow's your {day} {time} going?\nHere's a coupon for {self.coupon} off")

def get_day():
    """
    Gets date from datetime.date and
    returns current day of the week (e.g. Monday)
    """
    current_day = d.today()
    return d.strftime(current_day, "%A")

def get_time_of_day():
    """
    Gets time from some nether-hole of datetime
    and returns time of day as string (e.g. morning)
    """
    current_time = dt.now()
    if current_time.hour < 12:
        return 'morning'
    elif 12 <= current_time < 17:
        return 'afternoon'
    else:
        return 'evening'

greeter = Greeter()
greeter.greet()
