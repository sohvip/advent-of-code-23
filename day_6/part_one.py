from functools import reduce

def beat_the_records():
    time = [53, 83, 72, 88]
    distance = [333, 1635, 1289, 1532]
    ways_to_win = []
    for i in range(len(time)):
        lower_limit = 0
        upper_limit = time[i]
        for j in range(time[i]+1):
            if j * (time[i] - j) > distance[i]:
                lower_limit = j
                break
        for k in range(time[i], -1, -1):
            if k * (time[i] - k) > distance[i]:
                upper_limit = k
                break
        ways_to_win.append(upper_limit - lower_limit + 1)
    return reduce(lambda a, b : a * b, ways_to_win)
