def most_common_character(str1):
    # Initialize variables to help keep track of changing items

    str_counter = 0
    letter_list = []
    multiple_letter_list = []
    count_list = []
    max_items = []
    highest_letter_count = 0

    # Convert string to list 
    # Append letters with multiples to new list
    # Append the number of times each multiple letter occurs i.e > 1

    for i in str1:
        str_counter = str1.count(i)
        letter_list.append(i)

        if str_counter > 1:
            multiple_letter_list.append(i)
            count_list.append(str_counter)
            count_list.sort()

    # Check to see if count_list is empty. Perhaps a try/except function will be better here.

    if len(count_list) > 1:
        highest_letter_count = max(count_list)
    else:
        return "There are no duplicates here!"

    # Get the highest number in the list and find it's corresponding index/value
    # if the highest number occurs twice or more, then get the first of its kind from the list

    for m in multiple_letter_list:
        if multiple_letter_list.count(m) == highest_letter_count:
            max_items.append(m)
    
    return max_items[0]




if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))

    third_string = "abc"
    print(most_common_character(third_string))

    empty_string = ""
    print(most_common_character(empty_string))