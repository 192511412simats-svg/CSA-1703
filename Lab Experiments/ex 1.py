from collections import deque

goal = "123456780"

moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def solve(start):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        blank = state.index("0")

        for pos in moves[blank]:
            new_state = list(state)
            new_state[blank], new_state[pos] = \
                new_state[pos], new_state[blank]

            new_state = "".join(new_state)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [state]))

    return None


print("Enter the puzzle:")
start = ""

for i in range(3):
    start += input().replace(" ", "")

solution = solve(start)

if solution:
    print("\nSolution:")
    for state in solution:
        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])
        print()
else:
    print("No solution found")
