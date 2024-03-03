import sys


def print_last_10_lines(data):
    lines = data.splitlines()[-10:]
    for line in lines:
        print(line)


if __name__ == "__main__":
    try:
        if len(sys.argv) == 1:  # read lines from stdin
            data = sys.stdin.read()
            print_last_10_lines(data)

        elif len(sys.argv) == 2:  # read lines from 1 file
            filename = sys.argv[1]
            with open(filename, 'r') as f:
                lines = f.read()
                print_last_10_lines(lines)

        else:  # read lines from multiple files
            extraline = True
            for i in range(1, len(sys.argv)):
                filename = sys.argv[i]
                try:
                    with open(filename, 'r') as f:
                        if i > 1 and extraline:
                            print('')
                        print(f"==> {filename} <==")
                        data = f.read()
                        print_last_10_lines(data)
                        extraline = True
                except FileNotFoundError as error:
                    print(f"{sys.argv[0]}: {error.filename}: No such file or directory")
                    extraline = False

    except FileNotFoundError as error:
        print(f"{sys.argv[0]}: {error.filename} No such file or directory")
    except KeyboardInterrupt:
        pass



