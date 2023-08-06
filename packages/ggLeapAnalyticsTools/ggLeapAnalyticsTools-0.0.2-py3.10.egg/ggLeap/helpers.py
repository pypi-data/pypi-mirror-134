import pandas as pd

from datetime import datetime, date

def remove_date_datetime(dt: date) -> date:
    """ Remove a date from a datetime. """
    dt = dt.replace(year=1, month=1, day=1)
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
    cleaned_csv = clean_csv(path)
    return cleaned_csv

def clean_csv(path: str) -> pd.DataFrame:
    f = open(path, 'r')
    data = f.readlines()

    new_df_vals = []
    for datum in data:
        values = datum.split(',')

        if 'RemovedOffer' in values:
            # merge "Offer name: XXXXXX" and "Reason: XXXXX"
            index = values.find('RemovedOffer')
            offer_name = values[index + 1]
            reason = values[index + 2]

            new_val = offer_name + "; " + reason

            values.remove(index + 2)
            values.remove(index + 1)
            values.insert(index + 1, new_val)

        new_df_vals.append(values)

    return pd.DataFrame(new_df_vals)
