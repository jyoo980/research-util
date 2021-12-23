#!/usr/bin/env python3

def read_file(file_name):
  with open(file_name, "r") as file:
    langs = file.readlines()
    return [lang.strip("\n") for lang in langs if lang != "Other\n"]

def counts(langs):
  freq = {}
  for lang in langs:
    key = "C/C++" if lang == "C" or lang == "C++" else lang
    if key not in freq:
      freq[key] = 1
    else:
      freq[key] += 1
  return freq

def compute_frequency_pcnt(lang_freqs):
  total_obs = sum(lang_freqs.values())
  return [[lang, (freq / total_obs) * 100] for lang, freq in lang_freqs.items()]

def show_results(items):
  sorted_items = sorted(items, key=lambda item: item[1], reverse=True)
  for lang, freq in sorted_items:
    print(f"Language: {lang}, Frequency: {freq:.2f}%")

langs = read_file("langs.txt")
freqs = counts(langs)
freq_pcnts = compute_frequency_pcnt(freqs)
show_results(freq_pcnts)
