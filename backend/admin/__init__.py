from datetime import datetime
from icecream import ic
# pip install icecream
import time
from datetime import datetime


def time_format():
    return f'{datetime.now()}|> '


ic('===============================================')
ic('============ Django REST Framework ============')
ic('===============================================')
ic(time_format())