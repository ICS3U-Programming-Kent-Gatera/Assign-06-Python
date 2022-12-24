#!/usr/bin/env python3
# Created by: Kent Gatera
# Created on: Nov 18
# This program searches for a user query within a list and displays its position.


def find_occurrences(list_package, search_query):
    index_occurrences = []
    # Getting the size of the list.
    array_size = len(list_package)
    for counter in range(0, array_size):
        if (
            # Stripping/ trimming all of the empty spaces
            # Putting it all in the same case for comparison.
            search_query.strip().lower()
            == list_package[counter].strip().lower()
        ):  # " kent".strip() == "kent ".strip()
            index_occurrences.append(counter)
    return index_occurrences


def find_total_occurrences(list_occurrences):
    # Getting the list of occurrences and finding out how big it is.
    total = len(list_occurrences)
    if total > 0:
        return total
    # If the list is lesser than 1 then return -1.
    else:
        return -1


def get_list_from_user_using_split():
    list_from_user = []
    list_input_from_user = input(
        "Enter a comma-separated list (or nothing to stop): "
    )  # abc, asdas,
    if list_input_from_user:
        return list_input_from_user.split(
            ","
        )  # .split() separates and turns anything after "," into an element
    # i.e input: "abc, asdas, " -> ["abc", " asdas", ""]
    else:
        return list_from_user


def main():
    # Adding a bunch user input.
    # list_from_user = get_list_from_user()
    list_from_user = get_list_from_user_using_split()

    if len(list_from_user) == 0:
        print("The list is empty. Bye")
    else:
        # Search query as user input.
        string_to_search = input("Enter the string to search for: ")
        # Finding out where the occurrences happened.
        position_indices = find_occurrences(list_from_user, string_to_search)
        # Finding out how many occurrences happened.
        num_times = find_total_occurrences(position_indices)

        if num_times > 0:
            # Displaying the position of the occurrence.
            print(f"'{string_to_search}' appeared at", end=": ")
            num_times = len(position_indices)
            for i in range(0, num_times):
                if i == 0 and i < num_times - 1:  # first but not last
                    print(f"{position_indices[i]}", end="")
                elif i > 0 and i < num_times - 1:  # middle but not last
                    print(f", {position_indices[i]}", end="")
                else:
                    if i == 0 and i == num_times - 1:  # first and last
                        print(f"{position_indices[i]}", end=". ")
                    else:  # not first but is last
                        print(f", and {position_indices[i]}", end=". ")

            print(f"So, {num_times} times.")
        else:
            # In case the number of occurrences is less than 0 (-1).
            print("(-1) Query not found")


# Calling main to execute the program.
if __name__ == "__main__":
    main()
