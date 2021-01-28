total_steps = 0
target_steps = 10000
while total_steps < target_steps:
    line = input()

    if line == "Going home":
        steps_home = int(input())
        total_steps += steps_home
        break

    current_steps = int(line)
    total_steps += current_steps

if total_steps < target_steps:
    print(f"{target_steps - total_steps} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!")
    print(f"{total_steps - target_steps} steps over the goal!")









