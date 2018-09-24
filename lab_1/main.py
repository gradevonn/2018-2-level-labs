def calculate_frequencies(info):
    words = info.split(' ')
    frequencies_dictionary = {}
    for count, k in enumerate(words):
        if words[count] in frequencies_dictionary:
            frequencies_dictionary[words[count]] += 1
        else:
            frequencies_dictionary[words[count]] = 1
    return frequencies_dictionary


pass


def filter_stop_words(frequencies_dict, stopwords):
    frequencies = {key: frequencies_dict[key] for key in frequencies_dict if key not in stopwords}
    sorted_words = sorted(frequencies, key=frequencies.get)
    sorted_words.reverse()
    return sorted_words


pass


def get_top_n(sorted_words, top_n):
    out = ''
    for i in range(top_n):
        out += sorted_words[i]
        out += '\n'
    return out


pass
m_file = open("data.txt")
final_file = open("report.txt", 'w')
n = input(int)
text = m_file.read(n)
freq_dict = calculate_frequencies(text)
print (freq_dict)
stop_words = input(tuple)
sort = filter_stop_words(freq_dict, stop_words)
print (sort)
N = input(int)
output = get_top_n(sort, N)
print (output)
final_file.write(output)
m_file.close()
final_file.close()
