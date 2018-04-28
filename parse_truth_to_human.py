import sys

def parse_to_human(gt_output_file):
  with open(gt_output_file) as f:
    lines = f.readlines()
    desired_lines = lines[0:len(lines):4]
    with open(gt_output_file + '_completesession.lab', 'w') as of:
      for line in desired_lines:
        line_splits = line.split(',')
        of.write("Activity"+line_splits[len(line_splits)-1])


def main():
  if len(sys.argv) < 2:
    print 'provide truth file.'

  gt_output_file = sys.argv[1]
  parse_to_human(gt_output_file)


if __name__ == '__main__':
  main()

