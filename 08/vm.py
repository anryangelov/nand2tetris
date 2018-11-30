import sys
import os
import os.path


current_file = None  # name of the vm file
label_suffix = 0
return_index = 0


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

push_command_pointer_asm = '''
    @{pointer}  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    '''

pop_command_pointer_asm = '''
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

goto = '''
    @{name}
    0;JMP
'''

if_goto = '''
    @SP
    AM=M-1
    D=M
    @{name}
    D;JNE
'''


def def_func(name, n_vars):
    label = '\n(%s)\n' % name
    push_local_0_n_times = ''.join(
        [push_command_constant_asm.format(value=0) for _ in range(n_vars)])
    return label + push_local_0_n_times


def call_func(name, n_args):
    global return_index
    return_addr = 'return_' + name + str(return_index)
    return_index += 1
    asm_parts = []
    asm_parts.append('\n// save return address\n')
    asm_parts.append(push_command_constant_asm.format(value=return_addr))
    for pointer in ('LCL', 'ARG', 'THIS', 'THAT'):
        asm_parts.append('\n// save %s\n' % pointer)
        asm_parts.append(push_command_pointer_asm.format(pointer=pointer))
    asm_parts.append(
    '''
    // reposition ARG
    @SP
    D=M
    @{minus_value}
    D=D-A
    @ARG
    M=D
    // reposition LCL
    @SP
    D=M
    @LCL
    M=D
    '''.format(minus_value=n_args+5))
    asm_parts.append(goto.format(name=name))
    asm_parts.append('\n(%s)\n' % return_addr)
    return ''.join(asm_parts)


func_return = '''
    // R13 (temp var) = LCL
    @LCL
    D=M
    @R13
    M=D
    // R14 (temp var) = retAddr
    @5
    A=D-A
    D=M
    @R14
    M=D
    // reposition return value for caller
    @SP
    A=M-1
    D=M
    @ARG
    A=M
    M=D
    // restore the caller's SP
    @ARG
    D=M+1
    @SP
    M=D
    // restore the caller's THAT
    @R13
    AM=M-1
    D=M
    @THAT
    M=D
    // restore the caller's THIS
    @R13
    AM=M-1
    D=M
    @THIS
    M=D
    // restore the caller's ARG
    @R13
    AM=M-1
    D=M
    @ARG
    M=D
    // restore the caller's LCL
    @R13
    AM=M-1
    D=M
    @LCL
    M=D
    @R14
    A=M
    0;jump
    '''


def comparing(jump):
    def inner():
        global label_suffix
        asm_tmpl = part_eq_gt_lt_asm.format(jump=jump, suffix=label_suffix)
        label_suffix += 1
        return arithmetic_commands_asm.format(operation='-', part_eq_gt_lt_asm=asm_tmpl)
    return inner


init = '''
@256
D=A
@SP
M=D
''' + call_func('Sys.init', 0)


push_pop_commands = {
    'push': {
        'local': lambda index: push_command_asm.format(memory_segment='LCL', index=index),
        'argument': lambda index: push_command_asm.format(memory_segment='ARG', index=index),
        'this': lambda index: push_command_asm.format(memory_segment='THIS', index=index),
        'that': lambda index: push_command_asm.format(memory_segment='THAT', index=index),
        'constant': lambda index: push_command_constant_asm.format(value=index),
        'pointer': lambda index: push_command_pointer_asm.format(pointer=3+int(index)),
        'temp': lambda index: push_command_pointer_asm.format(pointer=5+int(index)),
        'static': lambda index: push_command_static_asm.format(index=index, file=current_file),
    },
    'pop': {
        'local': lambda index: pop_command_asm.format(memory_segment='LCL', index=index),
        'argument': lambda index: pop_command_asm.format(memory_segment='ARG', index=index),
        'this': lambda index: pop_command_asm.format(memory_segment='THIS', index=index),
        'that': lambda index: pop_command_asm.format(memory_segment='THAT', index=index),
        'pointer': lambda index: pop_command_pointer_asm.format(pointer=3+int(index)),
        'temp': lambda index: pop_command_pointer_asm.format(pointer=5+int(index)),
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
    'label': lambda name: '\n(%s)\n' % name,
    'goto': lambda name: goto.format(name=name),
    'if-goto': lambda name: if_goto.format(name=name)
}


subroutines_commands = {
    'call': call_func,
    'function': def_func,
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
        int_arg2 = int(arg2)
        asm_code =subroutines_commands[command_type](arg1, int_arg2)
    elif command_type == 'return':
        asm_code = func_return
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


def translate_file(current_filename, desc):
    global current_file
    current_file = current_filename
    asm_code_parts = []
    for command in get_command(desc):
        asm_code = process_vm_command(command)
        asm_code_parts.append(asm_code)
    return '\n'.join(asm_code_parts)


def main():
    dirname = sys.argv[1]
    dirname = dirname.rstrip('/')
    filename_write = os.path.join(dirname, os.path.split(dirname)[-1]) + '.asm'
    asm = []
    for basename in os.listdir(dirname):
        if basename.endswith('.vm'):
            fullpath = os.path.join(dirname, basename)
            with open(fullpath) as f:
                code = translate_file(basename, f)
                asm.append(code)
    asm_str = init + ''.join(asm)
    with open(filename_write, 'w') as f:
        f.write(asm_str)


if __name__ == '__main__':
    import fire
    fire.Fire()
