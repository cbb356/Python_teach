def count(footstep):
    if footstep == 1:
        return 1
    if footstep == 2:
        return 2
    else:
        return count(footstep - 2) + count(footstep - 1)

print(count(10))