#!/usr/bin/env python3
# FILE: hamming.py
# WRITER: Roy Levy
# DESCRIPTION: This file get an user input of hamming code and check if it has errors it write the parity bit
#              with the error.
# Eamples
# example of user code with no error: 10101010000
# example of user code with 1 error: 00101010000, error in the index 1

import math

OPEN_MSG = "Insert humming code:\n"
USER_INPUT_MSG = "user input of hamming code was: \t"
ERROR_MSG_PART1 = "In index: "
ERROR_MSG_PART2 = " expected parity bit was: "
ERROR_MSG_PART3 = " but founded: "
CODE_LENGTH_INVALID = "code length must not be a pow of 2"
ERRORS_FOUNDED = "Total errors founded: "
NO_ERRORS = "The code have no errors.\n\t Good job!"
FORMAT_BINARY_PART1 = '0'
FORMAT_BINARY_PART2 = 'b'
TO_PRINT = True
DEFAULT_PARITY_VALUE = -1
MASK = 1
EVEN = 2


def print_parity_errors(parity_key):
    """
    This function print the parity that has an error with it, and the expected value
    :param parity_key: the parity index
    :return: none
    """
    print(ERROR_MSG_PART1 + str(EVEN ** parity_key) + ERROR_MSG_PART2 +
          str(parity_bit_needed[parity_key]) + ERROR_MSG_PART3 + user_hamming[EVEN ** parity_key - 1])


def compare_parity_bits(to_print=False):
    """
    This function compare parity bits of the user input and the calculated parity bits values
    :param to_print: to print the Errors location?
    :return: the number of errors that were founded
    """
    errors_counter = 0
    for key in parity_bit_needed.keys():
        if parity_bit_needed[key] != int(user_hamming[EVEN ** key - 1]):
            errors_counter += 1
            if to_print:
                print_parity_errors(key)
    return errors_counter


def find_significant_bit(max_parity, number, bit):
    """
    This function find a significant bit by using shift to right and then mask it with 1,
    so for example: for number 6(=110) bit 1 will give us: 0 bit 2 and 3 will give us: 1
    :param max_parity: how many bits should be in the binary number it effected by the user input
                       (it add 0 to the start if needed)
    :param number: the number in decimal to check
    :param bit: what bit in binary to get (bit number counted from right to left, 1 is lsb, max_parity is msb)
    :return: the value of the significant bit we wanted
    """
    return format((number >> (len(format(number, FORMAT_BINARY_PART1 + str(max_parity) + FORMAT_BINARY_PART2)) - bit))
                  & MASK, FORMAT_BINARY_PART2)


def calc_parity_bits():
    """
    This function calc the parity bits values
    :return: True if the inserted code is valid
    """
    paritys_sum_evens = list()
    for key in parity_bit_needed.keys():
        sum_evens = 0
        for i in range(1, len(user_hamming) + 1):
            if i not in parity_bits_indexes:
                if int(find_significant_bit(int(math.log2(parity_bits_indexes[-1]) + 1), i, key + 1)):
                    sum_evens += int(user_hamming[i - 1])
        paritys_sum_evens.append(sum_evens % EVEN)
    for key in parity_bit_needed.keys():
        parity_bit_needed[key] = paritys_sum_evens.pop()


def init_hamming_code():
    """
    This function get the user input of hamming code and create the parity indexes for it.
     , parity_indexes
    :return: user_input - the binary number of the hamming code that the user inserted
             parity_needed - dictionary and its key- the parity pow index, value- how many even indexes with the digit
             that this pow index represent.
             parity_indexes- list of all the indexes of pow(2, parity_needed keys)
    """
    user_input = input(OPEN_MSG)
    parity_needed = {x: DEFAULT_PARITY_VALUE for x in range(0, int(math.ceil(math.log2(len(user_input) + 1))))}
    parity_indexes = [EVEN ** x for x in parity_needed.keys()]
    return user_input, parity_needed, parity_indexes


def check_hamming_code():
    """
    This function check the hamming code, if it has errors it write the parity bit with the error.
    :return: none
    """
    if len(user_hamming) != parity_bits_indexes[-1]:
        calc_parity_bits()
        print(USER_INPUT_MSG, user_hamming)
        if compare_parity_bits():
            print(ERRORS_FOUNDED + str(compare_parity_bits(TO_PRINT)))
        else:
            print(NO_ERRORS)
    else:
        print(CODE_LENGTH_INVALID)


user_hamming, parity_bit_needed, parity_bits_indexes = init_hamming_code()
check_hamming_code()
