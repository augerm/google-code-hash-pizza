def write_output(self, output_file, lines):
    with open(output_file, 'w') as f:
        for line in lines:
            f.write("%s\n" % line)
