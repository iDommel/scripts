#!/usr/bin/env python3
import random
import argparse

def pair_names(names_list):
    if not names_list:
        return "The list is empty. No pairs can be made."

    random.shuffle(names_list)

    paired_names = []

    for i in range(0, len(names_list)-1, 2):
        paired_names.append((names_list[i], names_list[i+1]))

    if len(names_list) % 2 == 1:
        single_person = names_list[-1]
        return paired_names, f"{single_person} does not have a pair."

    return paired_names, None



def main(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            list_of_names = [line.strip() for line in file]
    except Exception as e:
        print(f"Error reading the input file: {e}")
        return

    if not list_of_names:
        print("The list is empty. No pairs can be made.")
        return

    pairs, single_info = pair_names(list_of_names)

    try:
        with open(output_file, 'w') as file:
            for i, pair in enumerate(pairs, 1):
                file.write(f"Pair {i}: {pair[0]} -> {pair[1]}\n")
            if single_info:
                print("There is a person without a pair.")
                file.write(single_info + '\n')
    except Exception as e:
        print(f"Error writing to the output file: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pairing names from input file and writing the pairs to output file.")

    parser.add_argument('input_file', type=str, help='Path to the input file containing names')
    parser.add_argument('output_file', type=str, help='Path to the output file for saving pairs')

    args = parser.parse_args()

    main(args.input_file, args.output_file)