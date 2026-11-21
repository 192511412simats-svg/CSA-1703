room = ['D', 'D']
pos = 0

print("Initial State:", room)

while 'D' in room:
    if room[pos] == 'D':
        room[pos] = 'C'
        print("Cleaned room", pos + 1)
    else:
        pos = 1 - pos
        print("Moved to room", pos + 1)

print("Final State:", room)
