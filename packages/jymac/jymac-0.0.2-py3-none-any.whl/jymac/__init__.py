import random
def generate(qunt):
    with open("mac.txt", "r") as f:
        data = f.readlines()
    random.shuffle(data)
    mac = []
    for i in range(qunt):
        data[i] = data[i].strip()
        mac.append(data[i])
    return mac