from os.path import isfile

def get_most_common_char(path):
    if isfile(path):
        file_content = list(open(path, 'r').read())
        symbols = filter(lambda x: x != ' ', set(file_content))

        counter = {}
        for symbol in symbols:
            counter[symbol] = file_content.count(symbol)

        sorted_counter = sorted(list(counter.items()), key=lambda x: x[1])
        return sorted_counter[-1][0]

if __name__ == '__main__':
    file_path = ''
    print(get_most_common_char(file_path))
