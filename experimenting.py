import datetime
import xml.etree.ElementTree as ET
import gzip
import zipfile as zf
import os
import itertools as it
import pandas as pd


def get_xes_events_data(file):
        """
        reads and parse all the events information from a xes file
        """
        temp_data = list()
        tree = ET.parse(file)
        root = tree.getroot()
        # if self.ns_include:
        #     ns = {'xes': root.tag.split('}')[0].strip('{')}
        #     tags = dict(trace='xes:trace',
        #                 string='xes:string',
        #                 event='xes:event',
        #                 date='xes:date')
        # else:
        #     ns = {'xes': ''}
        #     tags = dict(trace='trace',
        #                 string='string',
        #                 event='event',
        #                 date='date')
        # traces = root.findall(tags['trace'], ns)
        # i = 0
        # sup.print_performed_task('Reading log traces ')
        # for trace in traces:
        #     temp_trace = list()
        #     caseid = ''
        #     for string in trace.findall(tags['string'], ns):
        #         if string.attrib['key'] == 'concept:name':
        #             caseid = string.attrib['value']
        #     for event in trace.findall(tags['event'], ns):
        #         task = ''
        #         user = ''
        #         event_type = ''
        #         for string in event.findall(tags['string'], ns):
        #             if string.attrib['key'] == 'concept:name':
        #                 task = string.attrib['value']
        #             if string.attrib['key'] == 'org:resource':
        #                 user = string.attrib['value']
        #             if string.attrib['key'] == 'lifecycle:transition':
        #                 event_type = string.attrib['value'].lower()
        #         timestamp = ''
        #         for date in event.findall(tags['date'], ns):
        #             if date.attrib['key'] == 'time:timestamp':
        #                 timestamp = date.attrib['value']
        #                 try:
        #                     timestamp = datetime.datetime.strptime(
        #                         timestamp[:-6], self.timeformat)
        #                 except ValueError:
        #                     timestamp = datetime.datetime.strptime(
        #                         timestamp, self.timeformat)
        #         # By default remove Start and End events
        #         # but will be added to standardize
        #         if task not in ['0', '-1', 'Start', 'End', 'start', 'end']:
        #             if ((not self.one_timestamp) or
        #                 (self.one_timestamp and event_type == 'complete')):
        #                 temp_trace.append(dict(caseid=caseid,
        #                                        task=task,
        #                                        event_type=event_type,
        #                                        user=user,
        #                                        timestamp=timestamp))
        #     if temp_trace:
        #         temp_trace = self.append_xes_start_end(temp_trace)
        #     temp_data.extend(temp_trace)
        #     i += 1
        # self.raw_data = temp_data
        # self.data = self.reorder_xes(temp_data)
        # sup.print_done_task()



# log = lr.LogReader('input_files/BPI_Challenge_2012.xes')
# log_df = pd.DataFrame(log.data)
# print(log_df)

get_xes_events_data('input_files/BPI_Challenge_2012.xes')