import sys


def get_statistics(data):
    n_lines = len(data.splitlines())
    n_words = len(data.split())
    n_bytes = len(data.encode('utf-8'))
    return n_lines, n_words, n_bytes


if __name__ == "__main__":
    try:
        if len(sys.argv) == 1:
            data = sys.stdin.read()
            n_lines, n_words, n_bytes = get_statistics(data)
            print(f"      {n_lines}       {n_words}      {n_bytes}")

        elif len(sys.argv) == 2:
            filename = sys.argv[1]
            with open(filename, 'r') as f:
                data = f.read()
                n_lines, n_words, n_bytes = get_statistics(data)
                print(f"      {n_lines}       {n_words}      {n_bytes} {filename}")

        else:
            total_lines, total_words, total_bytes = 0, 0, 0

            for i in range(1, len(sys.argv)):
                filename = sys.argv[i]
                try:
                    with open(filename, 'r') as f:
                        data = f.read()
                        n_lines, n_words, n_bytes = get_statistics(data)
                        print(f"      {n_lines}      {n_words}      {n_bytes} {filename}")
                        total_lines += n_lines
                        total_words += n_words
                        total_bytes += n_bytes
                except FileNotFoundError as error:
                    print(f"{sys.argv[0]}: {error.filename} No such file or directory")

            print(f"      {total_lines}      {total_words}     {total_bytes} total")

    except FileNotFoundError as error:
        print(f"{sys.argv[0]}: {error.filename} No such file or directory")
    except KeyboardInterrupt:
        pass
