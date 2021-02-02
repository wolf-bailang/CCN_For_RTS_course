from __future__ import print_function

import time
import Table
from PIT import PIT_search_data





def Drop_data(inface, data):
    print('2')

def Create_data(inface, route_ID, interest):
    '''
        Interest_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, start_time, life_time], ...], ... }
        interest = [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]
        Data_table = {'route_ID': [[interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time], ...], ... }
        data = [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, life_time]
        PS = {'route_ID': [content_name, ...], ... }
        FIB =｛'route_ID'： ['route_ID', ...], ... ｝
        fib = ['route_ID', ...]
    '''
    interest_ID = interest[route_ID][0]
    consumer_ID = interest[route_ID][1]
    content_name = interest[route_ID][-3]
    hop = 1
    start_time = interest[route_ID][-2]
    cost_time = time.time()  # s

    data = dict([[route_ID, [interest_ID, consumer_ID, route_ID, content_name, hop, start_time, cost_time]]])
    # print(data_temp)
    return data

def Send_data(inface, route_ID, interest):
    data_temp = Create_data(inface, route_ID, interest)
    data.update(data_temp)
    # print(data)

def On_data(inface, data):
    if PIT_search_data(inface, data):
        # CS_cache_data(inface, data)
        print('2')
    else:
        # fib_data(inface, data)
        Drop_data(inface, data)
        print('2')

if __name__ == '__main__':
    data = {'r1': ['i0', 'c0', 'r0', 'r1/1', 10., 100.]}
    interest = {'r0': ['i0', 'c0', 'r0', 'r1/1', 10., 100.]}
    inface = 'r0'
    route_ID = 'r0'
    # On_data(inface, data)
    Create_data(inface, route_ID, interest)
    print('data')


