"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    word_dict = {}
    word_list = s.split(" ")
    max_count = 1
    max_word_list = []
    top_n = []
    
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
            max_count = max(max_count, word_dict[word])
        else:
            word_dict[word] = 1

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    for word in word_dict:
        max_word_list.append((word, word_dict[word]))

    max_word_list.sort(key=lambda item: item[0]) # Sort alphabetically first
    max_word_list.sort(key=lambda item: item[1],reverse=True) # Sort numerically last

    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    n = min(n, len(max_word_list))
    top_n = max_word_list[0:n]

    return top_n

def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()