import time
import datetime as dt
import decimal

class decimaltime:
  """ Presents the time of day in Decimal Time 
      10 Hours/day
      100 minutes/hour
      100 seconds/minute
  """
  def time(self, archaic_seconds = 0):
    if archaic_seconds == 0:
      now = decimal.Decimal(dt.datetime.now().strftime('%s.%f'))
      midnight = decimal.Decimal(dt.date.today().strftime('%s.%f'))
      archaic_seconds_from_midnight = decimal.Decimal(now - midnight)
    else:
      archaic_seconds_from_midnight = decimal.Decimal(archaic_seconds)
    return archaic_seconds_from_midnight * decimal.Decimal('1.157')

  def time_to_string(self, decimal_seconds = 0):
    if decimal_seconds == 0:  
      seconds_from_midnight = self.time() 
    else:
      seconds_from_midnight =  decimal.Decimal(decimal_seconds)
    decimal_hour = seconds_from_midnight / 10000
    decimal_minute = (seconds_from_midnight % 10000) / 100
    decimal_second = seconds_from_midnight % 100
    time_string = "%(hour)01d:%(minute)02d:%(second)02d" % {"hour": decimal_hour, "minute": decimal_minute, "second": decimal_second}
    return time_string

def DeciTimeCaller():
  decitime = decimaltime()
  new_time = decitime.time_to_string()
  while True:
    this_time = decitime.time_to_string()
    if (this_time != new_time): 
      print this_time
      new_time = this_time
    time.sleep(.1667)

DeciTimeCaller()
