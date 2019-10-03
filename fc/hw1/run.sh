#!/bin/bash

python3 hw.py
cd tex
pdflatex hw.tex
pdflatex solved.tex
cd ..
mv tex/hw.pdf finished/
mv tex/solved.pdf finished/
