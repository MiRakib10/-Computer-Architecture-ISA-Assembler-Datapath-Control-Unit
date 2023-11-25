# func  dec-bin

def deciToBin(n):
    return bin(int(n, 10)).replace("0b", "").rjust(3, '0')

# fun bin-hex

def binToHexa(n):
    return hex(int(n, 2))[2:]  # [2:] omits 0x from left


def main(assembly):
    # opcodes
    opcode_type_1 = {  # op + register1 + rgister2 
        "add": "0000",
        "sub": "0001",
        "nor": "0111",
        "nand": "0110",
        "slt": "1011",

    }

    opcode_type_2 = {  # op + register + im
        "beq": "1010",
        "addi": "0010",
        "subi": "0011",
        "sll": "0100",
        "srl": "0101",
        "lw": "1000",
        "sw": "1001",
        "slti": "1100",

    }

    opcode_type_3 = {  # op + register

        "j": "1101",
    }
    # registor dec val
    registers = {
        "$zero": "000",
        "$s0": "001",
        "$s1": "010",
        "$s2": "011",
        "$t0": "100",
        "$t1": "101",
        "$t2": "110",
        "$t3": "111",
    }


    command = list(assembly.lower().split(" ")) #check instruction

    # formate space
    try:
        if len(command) == 3:
            instruction = command[0]
            reg = [command[1].replace(',', ''), command[2]]

        else:
            instruction = command[0]
            reg = command[1].split(",")
    except Exception as e:
        return "Invalid Instructions"


    # type 1 decoder
    if instruction in opcode_type_1.keys():
        try:
            hexa_opCode = (opcode_type_1[instruction])
            hexa_rs = (registers[reg[0]])
            hexa_rd = (registers[reg[1]])
            return binToHexa(hexa_opCode+hexa_rs+hexa_rd)

        except Exception as e:
            return "Invalid Instructions"



    # type 2 decoder
    elif instruction in opcode_type_2.keys():
        try:
            if int(reg[1], 10) <= 7:  # immediate can not be greater then 7 cause register hase only 3 bit
                hexa_opCode = (opcode_type_2[instruction])
                hexa_rs = (registers[reg[0]])
                immediate_bin = deciToBin(reg[1])

                return binToHexa(hexa_opCode + hexa_rs + immediate_bin)

            else:
                return "Invalid number range:-3 to 7"

        except Exception as e:
            return "Invalid Instructions"



    # type 3 decoder
    elif instruction in opcode_type_3.keys():
        try:
            if int(reg[0]) > 0:
                hexa_opCode = (opcode_type_3[instruction])
                immediate_bin = deciToBin(reg[0])
                hexa_immediate = (bin(int(reg[0]))[2:].zfill(6)[:4]) + (
                    bin(int(reg[0]))[2:].zfill(6)[4:])
                return binToHexa(hexa_opCode + hexa_immediate)
            else:
                hexa_opCode = (opcode_type_3[instruction])
                hexa_immediate = (bin(int(reg[0]) % (1 << 6))[2:-4]) +(
                    bin(int(reg[0]) % (1 << 6))[-4:])
                return binToHexa(hexa_opCode + hexa_immediate)


        except Exception as e:
            return "Invalid Instructions"


    else:
        return "Opcode are not match"


# File reading and writing section
input_file = input("Enter the name of Input or Assembly text File: ")
output_file = input("Enter the name of Output or Hexa text File: ")

hex_list = []

try:
    # reading the Input txt file
    file1 = open(input_file, 'r')
    Lines = file1.readlines()
    for line in Lines:
        hex_list.append(main(line.strip()))

    # writing the file
    with open(output_file, 'w') as f:
        for code in hex_list:
            f.write(code)
            f.write('\n')

except Exception as e:
    print(e)
