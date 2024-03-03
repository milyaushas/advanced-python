import sys

if __name__ == "__main__":
    try:
        if len(sys.argv) == 1:  # read lines from 'stdin'
            i = 1
            while True:
                print(f'     {i}  {input()}')
                i += 1

        elif len(sys.argv) == 2:  # enumerate lines from given file
            filename = sys.argv[1]
            with open(filename, 'r') as f:
                lines = f.readlines()
                i = 1
                for line in lines:
                    if line.strip() == '':
                        print('')
                    else:
                        print(f'     {i}  {line}'.rstrip())
                        i += 1
        else:
            print('Invalid number of arguments')

    except FileNotFoundError:
        print(f'{sys.argv[0]}: {sys.argv[1]}: No such file or directory')
    except KeyboardInterrupt:
        pass
