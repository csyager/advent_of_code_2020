with open('input.txt') as f:
    input_file = f.readlines()
input_file = [x.rstrip() for x in input_file]

program = []

for elem in input_file:
    elem_list = elem.split()
    command = elem_list[0]
    value = elem_list[1]
    program.append([command, value, False])

command_history = []

def test_program(program, update_history:bool):
    loop_detected = False
    loop_detected = False
    current_command = 0
    acc = 0
    while not loop_detected:
        try:
            elem = program[current_command]
            command = elem[0]
            value = elem[1]
            already_visited = elem[2]
            if already_visited:
                loop_detected = True
                print("loop detected!")
                print(acc)
                return 0
            if command == 'nop':
                elem[2] = True
                if update_history:
                    command_history.append(current_command)
                current_command += 1
            elif command == 'jmp':
                elem[2] = True
                if update_history:
                    command_history.append(current_command)
                current_command += int(value)
            else:
                elem[2] = True
                if update_history:
                    command_history.append(current_command)
                acc += int(value)
                current_command += 1
        except IndexError as e:
            print("Program terminated successfully!")
            print(acc)
            return 1

test_program(program, True)

# reset program for simulation
for e in program:
    e[2] = False


for command_num in command_history:
    elem = program[command_num]
    command = elem[0]
    if command == 'acc':
        pass
    elif command == 'nop':
        program[command_num][0] = 'jmp'
        ret = test_program(program, False)
        if ret == 0:
            # test program failed
            for e in program:
                e[2] = False
            program[command_num][0] = 'nop'
            acc = 0
        else:
            print(acc)
    elif command == 'jmp':
        program[command_num][0] = 'nop'
        ret = test_program(program, False)
        if ret == 0:
            for e in program:
                e[2] = False
            program[command_num][0] = 'jmp'
            acc = 0
        else:
            print(acc)
    
