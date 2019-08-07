''' extract lines marked with NOTE from a python file 

Author: Henry Zhang
Date:August 07, 2019
'''

# module
import sys

# parameters


# classes


# functions
def generate_notes(filename):
  notes = []
  with open(filename, 'r') as f:
    for line in f:
      strings = line.split()
      if 'NOTE:' in strings or 'NOTE' in strings or 'BUG:' in strings:
        notes.append(line)
  return notes

def format_notes(notes):
  notes_formatted = []
  for line in notes:
    for i in range(len(line)):
      if line[i] != ' ':
        break
    notes_formatted.append(line[i:])
  return notes_formatted

def write_notes(notes, filename):
  with open(filename, 'w+') as f:
    f.writelines(notes)

def generate_filename_out(filename):
  for i in range(len(filename)):
    if filename[-i-1] == '.':
      break
  filename_out = filename[:-i-1] + '_notes.md'
  return filename_out

# main
def main():
  filename = sys.argv[1]
  notes = generate_notes(filename)
  notes_formatted = format_notes(notes)
  filename_out = generate_filename_out(filename)
  write_notes(notes_formatted, filename_out)

if __name__ == "__main__":
  main()