import pytest
import src.exercise

def test_capture_stdout(capsys):
    
    # Execute the student program, and capture the output (print statements):
    src.exercise.main()
    out, err = capsys.readouterr()
    
    # Split the output
    output = out.strip().split('\n')
    
    # Compare the actual output to the expected output:
    assert output[1] == '96'
    assert output[2] == '25'
