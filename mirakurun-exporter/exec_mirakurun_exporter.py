#!/usr/bin/python

import requests_unixsocket
import requests
import socket
import time

from prometheus_client import start_http_server, Summary, Gauge

status_interval = 300 # initiate Mirakurun Status every 300 seconds

status_memory_usage = Gauge('mirakurun_memory_usage_bytes', 'Mirakurun Memory Usage', ['label'])
status_programs_db = Gauge('mirakurun_programs_db_events', 'Mirakurun Programs DB', ['label'])
status_stream_count= Gauge('mirakurun_stream_count', 'Mirakurun Stream Count', ['label'])
status_error_count = Gauge('mirakurun_error_count', 'Mirakurun Error Count', ['label'])
status_timer_accuracy = Gauge('mirakurun_timer_accuracy', 'Mirakurun Timer Accuracy', ['label'])

def process_request(t):

    session = requests_unixsocket.Session()
    res = session.get('http+unix://%2Fvar%2Frun%2Fmirakurun%2Fmirakurun.sock/api/status')
    res_dict = res.json()

    status_memory_usage.labels('rss').set(res_dict['process']['memoryUsage']['rss'])
    status_memory_usage.labels('heapTotal').set(res_dict['process']['memoryUsage']['heapTotal'])
    status_memory_usage.labels('heapUsed').set(res_dict['process']['memoryUsage']['heapUsed'])

    status_programs_db.labels('storedEvents').set(res_dict['epg']['storedEvents'])

    status_stream_count.labels('decoder').set(res_dict['streamCount']['decoder'])
    status_stream_count.labels('tsFilter').set(res_dict['streamCount']['tsFilter'])
    status_stream_count.labels('tunerDevice').set(res_dict['streamCount']['tunerDevice'])

    status_error_count.labels('uncaughtException').set(res_dict['errorCount']['uncaughtException'])
    status_error_count.labels('bufferOverflow').set(res_dict['errorCount']['bufferOverflow'])
    status_error_count.labels('tunerDeviceRespawn').set(res_dict['errorCount']['tunerDeviceRespawn'])

    status_timer_accuracy.labels('m1avg').set(res_dict['timerAccuracy']['m1']['avg'])
    status_timer_accuracy.labels('m5avg').set(res_dict['timerAccuracy']['m5']['avg'])
    status_timer_accuracy.labels('m15avg').set(res_dict['timerAccuracy']['m15']['avg'])

    print('process.memoryUsage.rss: %s' % (res_dict['process']['memoryUsage']['rss']))
    print('process.memoryUsage.heapTotal: %s' % (res_dict['process']['memoryUsage']['heapTotal']))
    print('process.memoryUsage.heapUsed: %s' % (res_dict['process']['memoryUsage']['heapUsed']))

    print('epg.storedEvents: %s' % (res_dict['epg']['storedEvents']))

    print('res.streamCount.decoder: %s' % (res_dict['streamCount']['decoder']))
    print('res.streamCount.tsFilter: %s' % (res_dict['streamCount']['tsFilter']))
    print('res.streamCount.tunerDevice: %s' % (res_dict['streamCount']['tunerDevice']))

    print('errorCount.uncaughtException: %s' % (res_dict['errorCount']['uncaughtException']))
    print('errorCount.bufferOverflow: %s' % (res_dict['errorCount']['bufferOverflow']))
    print('errorCount.tunerDeviceRespawn: %s' % (res_dict['errorCount']['tunerDeviceRespawn']))

    print('timerAccuracy.m1.avg: %s' % (res_dict['timerAccuracy']['m1']['avg']))
    print('timerAccuracy.m5.avg: %s' % (res_dict['timerAccuracy']['m5']['avg']))
    print('timerAccuracy.m15.avg: %s' % (res_dict['timerAccuracy']['m15']['avg']))

    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(9684) 
    # Generate some requests.
    while True:
        try:
            process_request(status_interval)
        except TypeError:
            print('TypeError returned from mirakurun-exporter server')
        except requests.exceptions.ConnectionError:
            print('requests.exceptions.ConnectionError returned from mirakurun-exporter server')
            time.sleep(status_interval)
