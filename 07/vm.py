import sys
import os.path


current_file = None  # name of the vm file
label_suffix = 0


push_command_static_asm = '''
    @{file}.{index}
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    '''

pop_command_static_asm = '''
    @SP
    A=M-1
    D=M
    @{file}.{index}
    M=D
    @SP
    M=M-1
    '''

push_command_constant_asm = '''
    @{value}
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    '''

push_command_pointer_temp_asm = '''
    @{pointer}  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    '''

pop_command_pointer_temp_asm = '''
    @SP
    A=M-1
    D=M
    
    @{pointer}
    M=D
    
    @SP
    M=M-1
    '''

push_command_asm = '''
    @{index}
    D=A
    @{memory_segment}
    A=D+M  // pointer to value
    D=M  // real value
    
    @SP
    A=M
    M=D  // copy value in stack
    
    @SP
    M=M+1 // move stack pointer
    '''

pop_command_asm = '''
    @{index}
    D=A
    @{memory_segment}
    D=D+M  // pointer to value
    
    @R13
    M=D

    @SP
    A=M-1  // address (pointer) of value
    D=M  // real value

    @R13
    A=M  // register D contain new address
    M=D

    @SP
    M=M-1
'''

arithmetic_commands_asm = '''
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M{operation}D

    {part_eq_gt_lt_asm}

    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    '''

part_eq_gt_lt_asm = '''
    @TRUE{suffix}
    D;{jump}
    D=0
    @FALSE{suffix}
    0;JMP
(TRUE{suffix})
    D=-1
(FALSE{suffix})
'''


unary_arithmetic_commands_asm = '''
    @SP
    A=M-1  // address of the operand
    D={operation}M  // the value
    M=D
'''


label = '''
label {name}
'''


goto = '''
@{name}
0;JMP
'''

if_goto = '''
@SP
A=M-1
D=M
@{name}
D;JNQ
'''

infinite_loop = '''
(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP
'''


init = '''
@256
D=A
@SP
M=D
'''


def comparing(jump):
    def inner():
        global label_suffix
        asm_tmpl = part_eq_gt_lt_asm.format(jump=jump, suffix=label_suffix)
        label_suffix += 1
        return arithmetic_commands_asm.format(operation='-', part_eq_gt_lt_asm=asm_tmpl)
    return inner


push_pop_commands = {
    'push': {
        'local': lambda index: push_command_asm.format(memory_segment='LCL', index=index),
        'argument': lambda index: push_command_asm.format(memory_segment='ARG', index=index),
        'this': lambda index: push_command_asm.format(memory_segment='THIS', index=index),
        'that': lambda index: push_command_asm.format(memory_segment='THAT', index=index),
        'constant': lambda index: push_command_constant_asm.format(value=index),
        'pointer': lambda index: push_command_pointer_temp_asm.format(pointer=3+int(index)),
        'temp': lambda index: push_command_pointer_temp_asm.format(pointer=5+int(index)),
        'static': lambda index: push_command_static_asm.format(index=index, file=current_file),
    },
    'pop': {
        'local': lambda index: pop_command_asm.format(memory_segment='LCL', index=index),
        'argument': lambda index: pop_command_asm.format(memory_segment='ARG', index=index),
        'this': lambda index: pop_command_asm.format(memory_segment='THIS', index=index),
        'that': lambda index: pop_command_asm.format(memory_segment='THAT', index=index),
        'pointer': lambda index: pop_command_pointer_temp_asm.format(pointer=3+int(index)),
        'temp': lambda index: pop_command_pointer_temp_asm.format(pointer=5+int(index)),
        'static': lambda index: pop_command_static_asm.format(index=index, file=current_file),
    }
}

arithmetic_commands = {
    'add': lambda: arithmetic_commands_asm.format(operation='+', part_eq_gt_lt_asm=''),
    'sub': lambda: arithmetic_commands_asm.format(operation='-', part_eq_gt_lt_asm=''),
    'and': lambda: arithmetic_commands_asm.format(operation='&', part_eq_gt_lt_asm=''),
    'or': lambda: arithmetic_commands_asm.format(operation='|', part_eq_gt_lt_asm=''),
    'eq': comparing('JEQ'),
    'gt': comparing('JGT'),
    'lt': comparing('JLT'),
    'neg': lambda: unary_arithmetic_commands_asm.format(operation='-'),
    'not': lambda: unary_arithmetic_commands_asm.format(operation='!'),
}


program_flow_commands = {
    'label': lambda name: label.format(name=name),
    'goto': lambda name: goto.format(name=name),
    'if-goto': lambda name: if_goto.format(name=name)
}


subroutines_commands = {
}


def process_vm_command(command_row):
    parts = command_row.split()
    parts = parts + [None] * (3 - len(parts))  # padding None if needed
    command_type, arg1, arg2 = parts
    if command_type in push_pop_commands:
        asm_code = push_pop_commands[command_type][arg1](arg2)
    elif command_type in arithmetic_commands:
        asm_code = arithmetic_commands[command_type]()
    elif command_type in program_flow_commands:
        asm_code = program_flow_commands[command_type](arg1)
    elif command_type in subroutines_commands:
        pass
    else:
        raise ValueError('Unknow command %s' % command_type)

    return '// ' + command_row + asm_code


def get_command(descr):
    for line in descr:
        line = line.strip()
        if line.startswith('//'):
            continue
        if line:
            command = line.split('//', 1)[0]  # strip comment if any
            yield command


def build_asm_code_for_vm_file(current_filename, desc):
    global current_file
    current_file = current_filename
    asm_code_parts = []
    for command in get_command(desc):
        asm_code = process_vm_command(command)
        asm_code_parts.append(asm_code)
    return init + '\n'.join(asm_code_parts) + infinite_loop


def translate(current_filename, descr):
    result = build_asm_code_for_vm_file(current_filename, descr)
    # descr.seek(0)
    return result


def main():
    filename = sys.argv[1]
    current_filename, ext = filename.rsplit('.', 1)
    if ext != 'vm':
        raise ValueError('extention of file is not vm')
    with open(filename) as f:
        code = translate(os.path.basename(current_filename), f)
    filename_write = current_filename + '.' + 'asm'
    with open(filename_write, 'w') as f:
        f.write(code)


if __name__ == '__main__':
    main()
