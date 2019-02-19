def count(footstep):
    steps = [1, 2]
    for i in range(footstep - 2):
        steps.append(steps[i] + steps[i + 1])
    return steps[footstep-1]

print(count(10))
