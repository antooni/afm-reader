import sys

from decoder import decode_afm

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise NameError('Too little arguments provided')

    file_path: str = sys.argv[1]

    d = decode_afm(file_path)

    print(d)


# name of the file is a key
# rework plot config
