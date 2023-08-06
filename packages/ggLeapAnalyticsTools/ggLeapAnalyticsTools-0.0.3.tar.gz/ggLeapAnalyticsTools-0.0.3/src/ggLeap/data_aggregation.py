from datetime import datetime

import pandas as pd

from . import helpers
from . import DataHandler


def remove_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove dates from all datetimes in a dataframe
    """
    
    new_records = []
    for i in range(len(df)):
        current_record = df.loc[i]
        date_string = current_record["Date"]
        dt = helpers.ggLeap_str_to_datetime(date_string)
        new_dt = helpers.remove_date_datetime(dt)
        current_record["Date"] = new_dt
        new_records.append(current_record)

    return pd.DataFrame(new_records)


def remove_weeks(df: pd.DataFrame) -> pd.DataFrame:
    """ Remove all weeks from datetimes

        Change all dates in the DataFrame to the following:
        01/01/01 for a Monday
        02/01/01 for a Tuesday
        03/01/01 for a Wednesday
        04/01/01 for a Thursday
        05/01/01 for a Friday
        06/01/01 for a Saturday
        07/01/01 for a Sunday """

    new_records = []
    for i in range(len(df)):
        current_record = df.loc[i]
        date_string = current_record["Date"]
        dt = helpers.ggLeap_str_to_datetime(date_string)
        new_dt = helpers.remove_week_datetime(dt)
        current_record["Date"] = new_dt
        new_records.append(current_record)

    return pd.DataFrame(new_records)


def total_user_seconds(dh: DataHandler.DataHandler, 
                       username: str) -> int:
    """
    Iterate across all of a user's logins and logouts to calculate
    the total amount of time that they've spent logged in
    """
    pass


def total_user_seconds_between(dh: DataHandler.DataHandler, 
                               username: str,
                               start: int,
                               end: int) -> int:
    """
    Iterate across all of a user's logins and logouts to calculate
    the total amount of time that they've spent logged in between two times
    """
    pass
