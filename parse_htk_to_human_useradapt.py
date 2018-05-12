import sys
import math

last = None

def parse_to_human(htk_output_file, num_sessions):
  global last

  with open(htk_output_file, 'r') as f:
    line = f.readline() # ignore first line (this line should read #!MLF!# )
    while line:
      last = float(-1000)/50
      line = f.readline()   # read file name
      if line.startswith("\""):
        file_name = line.lstrip("\"")[:-2] + "-" + str(num_sessions)
        print file_name
        with open(file_name, 'w') as of:
          line = f.readline()
          while line:
            if line.startswith("."):
              break
            write_in_ms(of, line)

            line = f.readline()


def write_in_ms(of, line):
  global last

  interval = float(1000)/50

  line_splits = line.split(" ")
  start = long(line_splits[0])/10000 # convert 100 ns to milliseconds
  end = long(line_splits[1])/10000  # convert 100 ns to milliseconds


  while last < end:
    last = last+interval
    of.write(str(long(round(last)))+" "+line_splits[2]+"\n")

def main():
  if len(sys.argv) < 3:
    print 'provide htk label file and num sessions'
    exit(1)

  htk_output_file = sys.argv[1]
  num_sessions = sys.argv[2]
  parse_to_human(htk_output_file, num_sessions)

if __name__ == '__main__':
  main()

