import pandas as pd

from datetime import datetime, date

def remove_date_datetime(dt: date) -> date:
    """ Remove a date from a datetime. """
    dt = dt.replace(year=1, month=1, day=1)
    return dt


def remove_week_datetime(dt: date) -> date:
    """ Change dates to the following:
        01/01/01 for a Monday
        02/01/01 for a Tuesday
        03/01/01 for a Wednesday
        04/01/01 for a Thursday
        05/01/01 for a Friday
        06/01/01 for a Saturday
        07/01/01 for a Sunday """

    day = dt.today().weekday()
    dt = dt.replace(year=1, month=1, day=(day + 1))
    return dt


def ggLeap_str_to_datetime(string: str) -> date:
    date = datetime.strptime(string,
                             '%m/%d/%Y %I:%M:%S %p')
    return date


def read_csv(path: str) -> pd.DataFrame:
    """ Function to replace pandas.read_csv() because
    ggLeap data is screwy to start with so this function
    cleans the data and then loads it into a pandas
    dataframe """

    cleaning_functions = [fix_RemoveOffers]

    f = open(path, 'r')
    raw_rows = f.readlines()
    raw_rows = [row.split(',') for row in raw_rows]
    columns = raw_rows.pop(0)

    for f in cleaning_functions:
        raw_rows = f(raw_rows)

    cleaned_df = pd.DataFrame(raw_rows)
    cleaned_df.columns = columns
    return cleaned_df


def fix_RemoveOffers(raw_rows: list) -> list:
    """ If ggLeap returns records which have a 'RemoveOffer' action, then another 
    of the columns will have a comma in it meaning that reading it as a CSV doesn't work
    properly. This function fixes that """

    new_df_vals = []
    for row in raw_rows:
        if 'RemovedOffer' in row:
            index = row.index('RemovedOffer')
            offer_name = row[index + 1]
            reason = row[index + 2]

            new_val = offer_name + "; " + reason

            row.pop(index + 2)
            row.pop(index + 1)
            row.insert(index + 1, new_val)

        new_df_vals.append(row)

    return new_df_vals
