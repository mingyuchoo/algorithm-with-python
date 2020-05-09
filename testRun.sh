#! /bin/bash
 coverage erase
 coverage run -m unittest discover -p "*_test.py"
 coverage report -m

