#!/bin/env python3
import random


def simulate_one_family():
    boys = 0
    girls = 0
    while boys == 0:
        child = random.choice(['boy', 'girl'])
        if child == 'boy':
            boys += 1
        else:
            girls += 1
    return boys, girls


def simulate_multiple_families(num_families):
    total_boys = 0
    total_girls = 0
    for i in range(num_families):
        if i % 1000000 == 0:
            print('loading %.2f%%' % (i / num_families * 100))
        boys, girls = simulate_one_family()
        total_boys += boys
        total_girls += girls
    boys_girls_ratio = total_boys / total_girls
    return boys_girls_ratio


if __name__ == '__main__':
    ratio = simulate_multiple_families(10 ** 9)
    print('ratio is %.8f' % ratio)
