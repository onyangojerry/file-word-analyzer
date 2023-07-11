# Jerry Onyango
# CS 51
# Assign 5


def tokenize(sentence):
    """
    checks words that make up a sentence
    :param sentence: (string) typed in sentence
    :return: (list) of words from the sentence
    """
    word_list = []  # a new list for the words without the punctuation symbols

    for words in sentence.split():  # creates a list of words from a sentence
        if words[-1] in ["!", ":", "?", ";", "."]:  # checks the last index of each word in our list of words
            words = words[:-1]  # removes the last index if it is a punctuation mark mentioned above
        word_list.append(words.lower())  # converts all letters to lower case and adds them to the new list
    return word_list


def get_sentence_length(filename):
    """

    :param filename: (string) file to be opened
    :return: (list) of (int)
    """
    sentence_lengths = []  # holds the lengths of each line in a file

    file = open(filename, "r")  # opens the file prompted

    for my_line in file:
        number = len(tokenize(my_line))  # turns a line to list, counts the number of words in the list
        sentence_lengths.append(number)  # appends the lengths of each sentence as an integer to the new list
    file.close()
    return sentence_lengths


def print_sentence_stats(filename):
    """
    checks details of a file, sentences
    :param filename: (string) file to be accessed
    :return: none
    """
    file = open(filename, "r")  # opens the file prompted
    total = 0
    for lines in file:
        total += 1
    print("Total sentences:\t", total)  # counts the total number of sentences in the file

    print("longest sentence:\t ", max(get_sentence_length(filename)))  # displays the number of longest sentence
    print("shortest sentence:\t", min(get_sentence_length(filename)))  # displays the number of the shortest sentence

    total_length = 0
    for number in get_sentence_length(filename):  # evaluates the average length of all the sentences
        total_length += number
    print("Ave. sentence length:\t ", total_length / len(get_sentence_length(filename)))  # displays as an integer
    file.close()


def add_words_to_dict(the_dict, my_word):
    """
    checks number of times word appears in a sentence
    :param the_dict: (dictionary) with key (string) and value (integer)
    :param my_word: (string) the word being searched for
    :return: (dictionary) with updated values
    """
    for words in my_word:  # iterates through the sentence
        if words in the_dict:
            the_dict[words] += 1  # updates the value of a word if found again
        else:
            the_dict[words] = 1  # leaves the value of a word as 1 if not found more than once
    # return the_dict


def get_word_counts(filename):
    """
    checks words and their frequencies
    :param filename: (string) file to be accessed
    :return: (dictionary) updated with frequencies
    """
    file = open(filename, "r")  # opens the prompted file
    my_dictionary = {}  # the dictionary to be updated
    for line in file:
        sorted_lines = tokenize(line)  # sorts the lines in a file into a list
        add_words_to_dict(my_dictionary, sorted_lines)  # updates the dictionary created

    file.close()  # closes the file
    return my_dictionary


def dict_count_max(word_frequencies):
    """

    :param word_frequencies: (dictionary)
    :return: (integer) maximum frequency
    """
    max_key = ''  # list to store the key as a string
    max_freq = -1  # sets the highest frequency

    for key in word_frequencies:  # iterating over the keys
        if word_frequencies[key] > max_freq:  # compares initial highest frequency with the new highest
            max_freq = word_frequencies[key]  # updates the new high frequency
            max_key = key  # keeps track and updates the new key with high frequency

    return max_key


def print_top_ten(filename):
    """

    :param filename: (string) file input
    :return: none
    """
    the_dict = get_word_counts(filename)  # forms a dictionary

    for i in range(10):  # prints 10 different items
        max_freq = dict_count_max(the_dict)
        print(str(i + 1) + ' : ' + str(max_freq) + "\t" + str(the_dict[max_freq]))
        the_dict.pop(max_freq)  # deletes the key with the highest frequency from the dictionary


def print_all_stats(filename):
    """
    checks all sentence stats
    :param filename: (string) the file input
    :return: none
    """
    print(print_sentence_stats(filename))
    print(print_top_ten(filename))


#  _____________________________________________________
# analysis section

# normal.txt
"""
Total sentences:	 99903
longest sentence:	  158
shortest sentence:	 1
Ave. sentence length:	  23.068286237650522
None
1 : the	168748
2 : of	88729
3 : and	68751
4 : in	62433
5 : to	50806
6 : a	45689
7 : is	24087
8 : as	22356
9 : was	21023
10 : for	18085
None
"""

# simple.txt
"""
Total sentences:	 99925
longest sentence:	  142
shortest sentence:	 1
Ave. sentence length:	  15.491488616462346
None
1 : the	108687
2 : of	50223
3 : and	40741
4 : in	40040
5 : a	35423
6 : to	31579
7 : is	29677
8 : was	17367
9 : it	14133
10 : are	13349
None
"""


# the average length of s sentence in normal.txt is greater than that of simple.txt
# article 'the' tops as the most used in both but tops in the normal.txt


def get_word_counts_two(filename1, filename2):
    """

    :param filename1: (string) first file
    :param filename2: (string) second file
    :return: (integer) number of unique words
    """

    file_a = open(filename1, "r")  # opens first the prompted file
    file_b = open(filename2, "r")  # opens second prompted file
    my_dictionary = {}  # the dictionary to be updated
    for line in file_a:
        sorted_lines = tokenize(line)  # sorts the lines in first file into a list
        add_words_to_dict(my_dictionary, sorted_lines)  # updates the dictionary created
        for line in file_b:
            sorted_lines = tokenize(line)  # sorts the lines in second file into a list
            add_words_to_dict(my_dictionary, sorted_lines)  # updates the same dictionary created

    unique_words = []  # new list to append all keys
    for key in my_dictionary:  # iterating over the keys
        if my_dictionary[key] == 1:  # checks frequencies equal to one
            unique_words.append(key)  # adds all keys to the empty list

    file_a.close()  # closes the file
    file_b.close()  # closes the file
    return len(unique_words)
