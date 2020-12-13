with open('8.in') as f:
    program = f.readlines()

acc = 0
pc = 0
S = set()
while pc < len(program):
    op, b = program[pc].split(' ')
    b = int(b)
    if pc in S:
        print(acc)
        exit()
    S.add(pc)
    if op == 'acc':
        acc += b
        pc += 1
        continue
    elif op == 'nop':
        pc += 1
        continue
    elif op == 'jmp':
        pc += b
        continue
