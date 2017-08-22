#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import json
import os
from os.path import join


class ProcessData(object):
    def __init__(self, base_dir='./', out_dir='../../processed',
                 out_file='out.csv'):
        """Extract tweet texts from all JSON files in raw data directory
        """
        self.base_dir = base_dir
        self.out_dir = out_dir
        self.out_file_abs = join(out_dir, out_file)

    def get_csv_names(self):
        """Get a generator with all file paths in underlying directories
        """
        print(self.base_dir)
        for dir_path, dir_names, file_names in os.walk(self.base_dir):
            for file_name in file_names:
                if file_name.lower().endswith('.json'):
                    yield join(dir_path, file_name)

    def _write_to_csv(self, data, keys=['text']):
        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)
        with open(self.out_file_abs, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
            for tweet in data:
                print('Data')
                print(tweet)
                csv_writer.writerow([tweet[key] for key in keys])

    def process_data(self):
        """Extract text from JSONs and write it to csv file
        """
        print('Process')
        for file_name in self.get_csv_names():
            print('Filename '+file_name)
            with open(file_name, 'r') as file:
                data = json.load(file)
                self._write_to_csv(data)

    def __call__(self):
        self.process_data()


if __name__ == "__main__":
    data_dir = '../../data/'
    base_dir = join(data_dir, 'raw')
    out_dir = join(data_dir, 'processed/trump')
    ProcessData(base_dir, out_dir, 'trump_tweets.csv')()
