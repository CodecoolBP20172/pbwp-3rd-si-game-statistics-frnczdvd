# REPORT FUNCTIONS
# FERENCZ DAVID
# 2017.07.08
# CODECOOL BUDAPEST
# PYTHON 3.6.1

import math

def get_most_played(file_name):
    count1 = 0
    count2 = str()
    try:
        with open(file_name) as f:
            for line in f:
                copies = float(line.split("\t")[1])
                title = line.split("\t")[0]
                if copies > count1:
                    count1 = copies
                    count2 = title
            return (count2)
    except FileNotFoundError:
        return "File not found"

def sum_sold(file_name):
    count = []
    try:
        with open(file_name) as f:
            for line in f:
                count.append(float(line.split("\t")[1]))
                result = sum(count)
            return result
    except FileNotFoundError:
        return "File not found"

def get_selling_avg(file_name):
    count = []
    try:
        with open(file_name) as f:
            for line in f:
                count.append(line.split("\t")[0])
                result = None
            return result
    except FileNotFoundError:
        return "File not found"

def count_longest_title(file_name):
    count = []
    try:
        with open(file_name) as f:
            for line in f:
                count.append(line.split("\t")[0])
                result = max(len(s) for s in count)
            return result
    except FileNotFoundError:
        return "File not found"

def get_date_avg(file_name):
    count = []
    try:
        with open(file_name) as f:
            for line in f:
                count.append(int(line.split("\t")[2]))
                result = math.ceil(sum(count) / len(count))
            return result
    except FileNotFoundError:
        return "File not found"

def get_game(file_name, title):
    count = []
    try:
        with open(file_name) as f:
            for line in f:
                count = (line.split("\t"))
                if title == count[0]:
                    count[1] = float(count[1])
                    count[2] = int(count[2])
                    count[-1] = count[-1].replace("\n", "")
                    return count
    except FileNotFoundError:
        return "File not found"
