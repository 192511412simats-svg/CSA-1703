from collections import deque

def water_jug():
    capacity = (4, 3)
    start = (0, 0)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        # Goal: 2 gallons in 4-gallon jug
        if state[0] == 2:
            return path

        a, b = state
        states = []

        # Fill 4-gallon jug
        states.append((4, b))

        # Fill 3-gallon jug
        states.append((a, 3))

        # Empty 4-gallon jug
        states.append((0, b))

        # Empty 3-gallon jug
        states.append((a, 0))

        # Pour 4-gallon jug into 3-gallon jug
        amount = min(a, 3 - b)
        states.append((a - amount, b + amount))

        # Pour 3-gallon jug into 4-gallon jug
        amount = min(b, 4 - a)
        states.append((a + amount, b - amount))

        for new_state in states:
            if new_state not in visited:
                queue.append((new_state, path))

    return None


solution = water_jug()

print("Solution:")
for state in solution:
    print(state)
