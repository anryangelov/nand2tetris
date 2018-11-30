import os
import sys


# C instruction parts
comp_table = {
    '0': '101010',
    '1': '111111',
    '-1': '111010',
    'D': '001100',
    'A': '110000',
    '!D': '001101',
    '!A': '110001',
    '-D': '001111',
    '-A': '110011',
    'D+1': '011111',
    'A+1': '110111',
    'D-1': '001110',
    'A-1': '110010',
    'D+A': '000010',
    'D-A': '010011',
    'A-D': '000111',
    'D&A': '000000',
    'D|A': '010101',
}

dest_table = {
    'M': '001',
    'D': '010',
    'MD': '011',
    'A': '100',
    'AM': '101',
    'AD': '110',
    'AMD': '111'
}

jump_table = {
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111',
}

predefined_symbols_table = {
    'SP': 0,
    'LCL': 1,
    'ARG': 2,
    'THIS': 3,
    'THAT': 4,
    'SCREEN': 16384,
    'KBD': 24576,
}

symbol_table = {}

address_ram = 16


def translate_c_command(command):
    dest, subcomm = command.split('=', 1) if '=' in command else (None, command)
    comp, jump = subcomm.split(';', 1) if ';' in subcomm else (subcomm, None)

    a = '0'
    if 'M' in comp:
        a = '1'
        comp = comp.replace('M', 'A')

    comp_bin = a + comp_table[comp]

    dest_bin = dest_table.get(dest, '000')
    jump_bin = jump_table.get(jump, '000')

    return '111' + comp_bin + dest_bin + jump_bin


def format_addr(addr):
    return format(int(addr), 'b').zfill(15)


def translate_symbol_command(command, symbol_table):
    if command[0].isdigit():
        address = command
    elif command[0].startswith('R') and command[1:].isdigit() and 0 <= int(command[1:]) <= 15:
        address = command[1:]
    else:
        address = predefined_symbols_table.get(command)
        if address is None:
            address = symbol_table.get(command)
            if address is None:
                return

    return format_addr(address)


def translate_a_command(command):
    variable = get_a_command(command)
    value = translate_symbol_command(variable, symbol_table)
    if value is None:
        symbol_table[variable] = address_ram
        value = format_addr(address_ram)
        global address_ram
        address_ram += 1
    return '0' + str(value)


def is_label(command):
    return command.startswith('(') and command.endswith(')')


def is_a_command(command):
    return command.startswith('@')


def get_label(command):
    return command[1:-1]


def get_a_command(command):
    return command[1:]


def get_line(descr):
    for line in descr:
        line = line.strip()
        if line.startswith('//'):
            continue
        if line:
            command = line.split(None, 1)[0]  # strip comment if any
            yield command


def assign_rom_address_to_labels(descr):
    address_rom = 0
    for command in get_line(descr):
        if is_label(command):
            label = get_label(command)
            if translate_symbol_command(label, symbol_table) is None:
                symbol_table[label] = address_rom
            address_rom -= 1
        address_rom += 1


def tranlate_after_labels_resoleved(descr):
    code = []
    for command in get_line(descr):
        if is_label(command):
            continue
        elif is_a_command(command):
            binary_line = translate_a_command(command)
        else:
            binary_line = translate_c_command(command)
        code.append(binary_line)
    return os.linesep.join(code) + os.linesep


def translate(descr):
    assign_rom_address_to_labels(descr)
    descr.seek(0)
    return tranlate_after_labels_resoleved(descr)


def main():
    filename = sys.argv[1]
    name, ext = filename.rsplit('.', 1)
    with open(filename) as f:
        code = translate(f)
    filename_write = name + '.' + 'hack'
    with open(filename_write, 'w') as f:
        f.write(code)


if __name__ ==  '__main__':
    main()
