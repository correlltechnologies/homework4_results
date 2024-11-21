#!/usr/bin/env python
import sys

filename = sys.argv[1]
# Read the rosbag file


found_tags = {}
source = open(filename, mode='r')   

while True:
    line = source.readline()
    if not line: break
    if line.find("detections=[]", 140) != -1: continue
    if line.find("detections=[", 140) == -1: continue
    index = line.find(", id=", 200)
    num = line[index + 5]
    if line[index + 6] != ",":
        num += line[index + 6]
    num = int(num)
    if num in found_tags:
       found_tags[num] += 1
    else:
       found_tags[num] = 1

source.close()

print("Found tags: ", end="")
for tag in found_tags.keys():
  print(tag, end=", ")
print("\n")

print("Counts:")
for tag, count in found_tags.items():
  print(f'{tag}: {count}')