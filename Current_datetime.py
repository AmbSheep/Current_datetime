#!/usr/bin/env python3
import datetime
import pytz


def Current_datetime():
    """
    Function to check the current date and time in Moscow, Chicago and UTC.
    :return: current date and time of the timezones in string format with it's names
    """
    Moscow_timezone = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    Chicago_timezone = datetime.datetime.now(pytz.timezone('America/Chicago'))
    UTC_timezone = datetime.datetime.now(pytz.timezone('Etc/UTC'))
    Moscow = str(Moscow_timezone.replace(tzinfo=None, microsecond=0))
    Chicago = str(Chicago_timezone.replace(tzinfo=None, microsecond=0))
    UTC = str(UTC_timezone.replace(tzinfo=None, microsecond=0))
    return 'Moscow: ' + Moscow, 'Chicago: ' + Chicago, 'UTC: ' + UTC


if __name__ == "__main__":
    for string in Current_datetime():
        print(string)
