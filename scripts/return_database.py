# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics - Johann diep 
#
# This script returns the database.

import pandas as pd


def return_database():
    database = {"Threats": ["Enemies", "Terrorists", "Men", "Women"], 
                "Number of people": ["5", "8", "3", "3"], 
                "Weapons": ["Pump Shotguns", "AK-47s", "Revolvers", "Sniper Rifles"],
                "Locations": ["Tilted Towers", "Greasy Grove", "Pleasant Park", "Flush Factory"],
                "Distance Away": ["1km", "2km", "3km", "4km"]}

    table = pd.DataFrame.from_dict(database)
    return table

def main():
    table = return_database()


if __name__ == '__main__':
    main()