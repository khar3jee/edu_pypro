"""
Chapter 3
Example Greeter for e-commerce sight

Goal: write up Greeter class w/ 3x methods
- _day
    - gives current day
- _part_of_day
    - gives time of day (e.g. morning)
- greet(self, store)
    - prints message similar to:
    'Hi, welcome to <store>!
     How's your <day><time of day> going?
     Here's a coupon for 20% off'
- store will be attribute to name of store
"""

from datetime import date as d

class Greeter():
    """example e-commerce greeter"""

    def __init__(self):
        """greeter attributes, store name"""
        self.store_name = 'Super Awesome Store of Things'

    def main(self):
        self.get_day()

    def get_day(self):
        current_day = d.today()
        print(d.strftime(current_day, "%A"))

greeter = Greeter()
greeter.main()
