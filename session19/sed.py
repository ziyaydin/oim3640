def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.

    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    with open (source) as f_read, open(dest, 'w') as f_write:
        for line in f_read:
            line = line.replace(pattern, replace)
            f_write.write(line)

def main():
    pattern = "man"
    replace = "woman"
    source = "data/dylan.txt"
    dest = "data/dylan2.txt"
    sed(pattern, replace, source, dest)


if __name__ == "__main__":
    main()
