import lab03
import sys

# This function tests your lab 01 code, ensuring that it prints the correct output
def test_main(capsys):
    lab03.main() # run the student's code
    captured = capsys.readouterr()
    sys.stderr.write('actual output:\n')
    sys.stderr.write(captured.out + '\n')
    correct_output = 'There are 6 pets in the list.\nThe word lengths of each pet name are [4, 5, 16, 5, 6, 4].\nThe vowel to consonant ratios of each word are [0.5, 0.6666666666666666, 0.25, 0.5, 0.5, 1.0, 0.5, 0.3333333333333333, 0.5].\n'

    sys.stderr.write('correct output:\n')
    sys.stderr.write(correct_output + '\n')
    assert captured.out == correct_output # verify that the output is a match

