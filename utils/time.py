from datetime import datetime, timedelta
from fixture import TIME_RANGES
import random

class TimeFaker: 
    # get a random datetime object, with given values
    random_datetime = datetime(2024,1,1,0,0,0,0) # Datetime that is on Monday 
    time_range = None

    def __init__(self, time_range=None, weekday=None): 
        # the given input could be an time_range like 17:00 - 20:00 or morning,noon, evening
        # weekday could be a number, or a word like monday, thuesday ... 
        # weekday starts with 0=Monday - 6:Sunday
        if time_range: 
            self.time_range = self._set_time_range(time_range)
        
        if weekday: 
            self.weekday = weekday
        else: 
            self.weekday = random.randint(0,7)

        self.random_datetime = self._generate_random_datetime()

    def _generate_random_datetime(self): 
        random_datetime = self.random_datetime + timedelta(days=self.weekday)
        hour = random.randint(0,23)
        minute = random.randint(0,59)
        random_datetime = self.random_datetime.replace(hour=hour, minute=minute)
        if self.time_range: 
            hour = random.randint(self.time_range[0][0],self.time_range[1][0])
            minute = random.randint(self.time_range[0][1],self.time_range[1][1])
            random_datetime = self.random_datetime.replace(hour=hour, minute=minute)
        return random_datetime

    def _set_time_range(self, time_range): 
        if type(time_range) == tuple and len(time_range) == 2 and type(time_range[0]) == tuple and type(time_range[1]): 
            return time_range
            
        if type(time_range) == str: 
            return self._get_range_from_string_time_range(time_range)
        
        raise ValueError("Range Error")
    
    def _get_range_from_string_time_range(self, time_range: str): 
        if time_range in TIME_RANGES.keys(): 
            return TIME_RANGES[time_range]
        
        raise ValueError("Range not defined")
