#!/usr/bin/env python3

import csv
import requests
import json

from collections import Counter

def read_ip_addrs(file_name):
  with open(file_name, newline="") as csv_file:
    reader = csv.reader(csv_file, delimiter=" ")
    ip_addrs = []
    for ip in reader:
      ip_addrs.extend(ip)
    return ip_addrs

def get(ip_addr):
  endpoint = f"https://ipinfo.io/{ip_addr}/json"
  resp = requests.get(endpoint, verify=True)

  status_code = resp.status_code
  
  if status_code != 200:
    return f"Error, status code: {status_code}"
  data = resp.json()
  return data["country"]

def frequencies(country_list):
  total_count = len(country_list)
  print(f"Total count: {total_count}")
  freqs = Counter(country_list)
  for country, freq in freqs.items():
    freq_pcnt = (freq / total_count) * 100
    print(f"Country: {country}, Frequency: {freq} ({freq_pcnt}%)")

ip_addrs = read_ip_addrs("ip_addrs.csv")
print("Addresses read successfuly. Working...")
countries = [get(ip) for ip in ip_addrs]
frequencies(countries)

