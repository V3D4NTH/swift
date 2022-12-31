#  date: 31. 12. 2022
#  author: Daniel Schnurpfeil
#
from copy import copy

from src.pl0_code_generator.instructions import Inst, Op


def ret_stck_str(stack: list) -> str:
    ret_val = ""
    for index, i in enumerate(stack):
        ret_val += str(index) + "\t" + str(i) + "\n"
    return ret_val


def run_pl0_code(generated_code: list) -> str:
    if len(generated_code) > 130:
        return "code is too long"
    static_base = 0
    stack_pointer = -1
    instruction_pointer = 0
    stack = []

    while instruction_pointer < len(generated_code):
        if generated_code[instruction_pointer][0] == Inst.lit.value:
            stack_pointer += 1
            if stack_pointer >= len(stack):
                stack.append(generated_code[instruction_pointer][2])
            else:
                stack[stack_pointer] = generated_code[instruction_pointer][2]

        elif generated_code[instruction_pointer][0] == Inst.opr.value:

            if int(generated_code[instruction_pointer][2]) == Op.neg.value:
                stack[stack_pointer] = -stack[stack_pointer]

            elif int(generated_code[instruction_pointer][2]) == Op.add.value:
                stack[stack_pointer - 1] = stack[stack_pointer - 1] + stack[stack_pointer]
                stack_pointer -= 1
            elif int(generated_code[instruction_pointer][2]) == Op.sub.value:
                stack[stack_pointer - 1] = stack[stack_pointer - 1] - stack[stack_pointer]
                stack_pointer -= 1

            elif int(generated_code[instruction_pointer][2]) == Op.mul.value:
                stack[stack_pointer - 1] = stack[stack_pointer - 1] * stack[stack_pointer]
                stack_pointer -= 1

            elif int(generated_code[instruction_pointer][2]) == Op.div.value:
                stack[stack_pointer - 1] = stack[stack_pointer - 1] / stack[stack_pointer]
                stack_pointer -= 1

            elif int(generated_code[instruction_pointer][2]) == Op.mod.value:
                stack[stack_pointer - 1] = stack[stack_pointer - 1] % stack[stack_pointer]
                stack_pointer -= 1

            elif int(generated_code[instruction_pointer][2]) == Op.eq.value:
                if stack[stack_pointer - 1] == stack[stack_pointer]:
                    stack[stack_pointer - 1] = 1
                else:
                    stack[stack_pointer - 1] = 0
                stack_pointer -= 1

            elif int(generated_code[instruction_pointer][2]) == Op.ne.value:
                if stack[stack_pointer - 1] != stack[stack_pointer]:
                    stack[stack_pointer - 1] = 1
                else:
                    stack[stack_pointer - 1] = 0
                stack_pointer -= 1

            elif int(generated_code[instruction_pointer][2]) == Op.lt.value:
                if stack[stack_pointer - 1] < stack[stack_pointer]:
                    stack[stack_pointer - 1] = 1
                else:
                    stack[stack_pointer - 1] = 0
                stack_pointer -= 1

            elif int(generated_code[instruction_pointer][2]) == Op.ge.value:
                if stack[stack_pointer - 1] >= stack[stack_pointer]:
                    stack[stack_pointer - 1] = 1
                else:
                    stack[stack_pointer - 1] = 0
                stack_pointer -= 1

            elif int(generated_code[instruction_pointer][2]) == Op.le.value:
                if stack[stack_pointer - 1] <= stack[stack_pointer]:
                    stack[stack_pointer - 1] = 1
                else:
                    stack[stack_pointer - 1] = 0
                stack_pointer -= 1

            elif int(generated_code[instruction_pointer][2]) == Op.gt.value:
                if stack[stack_pointer - 1] > stack[stack_pointer]:
                    stack[stack_pointer - 1] = 1
                else:
                    stack[stack_pointer - 1] = 0
                stack_pointer -= 1

        elif generated_code[instruction_pointer][0] == Inst.lod.value:
            stack_pointer += 1
            if stack_pointer - len(stack) > -1:
                stack.append(0)
            stack[stack_pointer] = stack[generated_code[instruction_pointer][2] + static_base]

        elif generated_code[instruction_pointer][0] == Inst.sto.value:
            stack[generated_code[instruction_pointer][2] + static_base] = stack[stack_pointer]
            stack_pointer -= 1

        elif generated_code[instruction_pointer][0] == Inst.cal.value:
            stack.append(stack_pointer)
            stack.append(0)
            stack.append(copy(instruction_pointer))
            instruction_pointer = generated_code[instruction_pointer][2] - 1
            static_base = stack_pointer + 1

        elif generated_code[instruction_pointer][0] == Inst.int.value:
            stack_pointer += generated_code[instruction_pointer][2]
            if stack_pointer - len(stack) > -1:
                for _ in range(stack_pointer - len(stack) + 1):
                    stack.append(0)

        elif generated_code[instruction_pointer][0] == Inst.ret.value:
            if static_base == 0:
                break
            instruction_pointer = stack[static_base + 2]
            stack_pointer = static_base - 1
            static_base = 0

        elif generated_code[instruction_pointer][0] == Inst.jmc.value:
            if stack[stack_pointer] == 0:
                instruction_pointer = generated_code[instruction_pointer][2] - 1

        elif generated_code[instruction_pointer][0] == Inst.jmp.value:
            instruction_pointer = generated_code[instruction_pointer][2] - 1

        if instruction_pointer < 0 or instruction_pointer > len(generated_code) or \
                stack_pointer < 0 or stack_pointer > len(stack):
            raise IndexError("ERR in executing generated code...")

        instruction_pointer += 1
    return ret_stck_str(stack)
