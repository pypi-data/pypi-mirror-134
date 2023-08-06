from __future__ import unicode_literals
from os.path import abspath, join, dirname
import random

full_path = lambda filename: abspath(join(dirname(__file__), filename))

listPath = [full_path('mac.txt')]

def generate(qunt=10):
    with open(listPath[0], "r") as f:
        data = f.readlines()
    random.shuffle(data)
    mac = []
    for i in range(qunt):
        data[i] = data[i].strip()
        mac.append(data[i])
    return mac
