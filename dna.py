import csv
import sys


def main():

    # TODO: Check for command-line usage

    if (len(sys.argv) != 3):
        print("The usage: python dna.py filename filename")

    # TODO: Read database file into a variable

    databases = []
    with open(sys.argv[1], "r") as database:
        reader = csv.DictReader(database)
        for name in reader:
            databases.append(name)

    # TODO: Read DNA sequence file into a variable

    sequences = ""
    with open(sys.argv[2], "r") as line:
        sequences = str(line.read())

    # TODO: Find longest match of each STR in DNA sequence

    subsequences = {
        "AGATC": 0,
        "TTTTTTCT": 0,
        "AATG": 0,
        "TCTAG": 0,
        "GATA": 0,
        "TATC": 0,
        "GAAA": 0,
        "TCTG": 0
    }

    for strs in subsequences:
        subsequences[strs] = longest_match(sequences, strs)

    print(match_profiles(databases, subsequences))


def match_profiles(databases, subsequences):
    # TODO: Check database for matching profiles

    name = None
    for dicts in databases:
        check = False
        count = 0
        for i in dicts:
            if i == "name":
                continue
            for strs in subsequences:
                if (i == strs) and (int(dicts[i]) == subsequences[strs]):
                    count += 1
                    break
                else:
                    if (count != 0):
                        continue
                    else:
                        check = True
                        count = 0
            if check:
                break

        if (count == 3 or count == 8):
            name = dicts["name"]
        elif count < 8:
            continue

    if name == None:
        return "No match"
    else:
        return name


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()