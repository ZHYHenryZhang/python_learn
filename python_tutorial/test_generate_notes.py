""" tests for generate_notes.py

Author: Henry Zhang
Date:August 07, 2019
"""

'''
TDD
1. specifications
input: a python file
output: a markdown file, with all the lines with a NOTE in comment.

2. write a simple testcase
print("This line is important") # NOTE
'''
# module
import generate_notes as gn

# parameters


# classes


# functions
def test_generate_notes():
  filename = 'generate_notes_testcase.py'
  notes = gn.generate_notes(filename)
  assert notes[0] == '# NOTE: this is a testcase for generate_notes.py\n'
  assert notes[1] == 'print("This line is important") # NOTE'

def test_format_notes():
  notes = ['# NOTE: this is a testcase for generate_notes.py\n',
            '    print("This line is important") # NOTE']
  notes_formatted = gn.format_notes(notes)
  assert notes_formatted[0] == '# NOTE: this is a testcase for generate_notes.py\n'
  assert notes_formatted[1] == 'print("This line is important") # NOTE'

def test_generate_filename_out():
  filename = 'python_tutorial.py'
  filename_out = gn.generate_filename_out(filename)
  assert filename_out == 'python_tutorial_notes.md'

# main
def main():
  test_generate_notes()
  test_format_notes()
  test_generate_filename_out()

if __name__ == "__main__":
  main()