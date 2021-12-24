#!/usr/bin/env python3

import csv
import requests
import json

def read_csv(file_name):
  with open(file_name, newline="") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    return [[size, int(freq)] for size, freq in reader]

def process_entries(entries):
  total_obs = sum([freq for _, freq in  entries])
  return [readable_str(size, freq, total_obs) for size, freq in entries]

def percentage(n, total):
  return (n / total) * 100

def readable_str(size, freq, total_obs):
  freq_pcnt = f"{percentage(freq, total_obs):.2f}"
  return f"Company size: {size}, Frequency: {freq} ({freq_pcnt}%)"

def show_results(results):
  for result in results:
    print(result)

data = read_csv("company-size.csv")
viewable_data = process_entries(data)
show_results(viewable_data)

