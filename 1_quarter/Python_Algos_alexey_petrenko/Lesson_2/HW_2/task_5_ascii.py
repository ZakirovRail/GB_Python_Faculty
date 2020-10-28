START = 32
STOP = 127
STEP = 10

for i in range(START, STOP + 1):
    print(f'\t{i}-{chr(i)}', end='')
    if i % STEP ==1:
        print()
