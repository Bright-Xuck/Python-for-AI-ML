###pands is a python libary fro worling with data sets
##It has functions for analyzing, cleaning, exploring, and manipulating data.

import pandas as pd

mydataset = {
    'car': ["volvo", "toyaota", "Wagon"],
    'passing': [1, 4, 6]
}

test = pd.DataFrame(mydataset)
print(test)

##pd.Series for putting data into coulums