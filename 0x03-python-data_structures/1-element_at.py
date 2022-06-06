#!/usr/bin/python3
# 1-element_at.py
# Ouattara Alphonse <ujlog01@gmail.com>

def element_at(my_list, idx):
  """retrive an element from a list"""
  if idx < 0 or idx > (len(my_list) - 1):
    return None
  return (my_list[idx])
