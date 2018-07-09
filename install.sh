#!/usr/bin/bash

pyenv install 2.7.15
pyenv install 3.5.5

mkdir ~/Python/Tasks/01/2.7.15 ~/Python/Tasks/01/3.5.5

cd ~/Python/Tasks/01/2.7.15
pyenv local 2.7.15
pyenv virtualenv env2

cd ~/Python/Tasks/01/3.5.5
pyenv local 3.5.5
pyenv virtualenv env3


