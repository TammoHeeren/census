__author__ = 'theeren'
__copyright__ = ""
__credits__ = [""]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = ""
__email__ = "tammo.heeren@gmail.com"
__status__ = "Development"

import logging
import requests
from datetime import datetime

logger = logging.getLogger(__name__)


class Idb1YearVariables:
    age = 'AGE'
    area_km2 = 'AREA_KM2'
    fips = 'FIPS'
    name = 'NAME'
    pop = 'POP'
    sex = 'SEX'
    time = 'time'
    year = 'YR'

    def __init__(self):
        pass


class Idb1Year:
    base_url = 'http://api.census.gov/data/timeseries/idb/1year'
    __variables = [
        Idb1YearVariables.name,
        Idb1YearVariables.age,
        Idb1YearVariables.pop
    ]

    def __init__(self, variables=None):
        if variables is not None:
            self.__variables = variables

    @property
    def variables(self):
        return self.__variables

    def get_data(self, year=datetime.now().year):
        params = {
            'get': ','.join(self.variables),
            'YR': year
        }
        response = requests.get(self.base_url, params=params)
        return response.json()