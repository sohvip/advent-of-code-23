def win_the_race():
    time = 53837288
    distance = 333163512891532
    lower_limit = 0
    upper_limit = time
    for i in range(time+1):
        if i * (time - i) > distance:
            lower_limit = i
            break
    for j in range(time, -1, -1):
        if j * (time - j) > distance:
            upper_limit = j
            break
    return upper_limit - lower_limit + 1
