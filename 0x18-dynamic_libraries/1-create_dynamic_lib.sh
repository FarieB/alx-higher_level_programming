#!/bin/bash

# Compile all .c files into a shared dynamic library liball.so
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 -shared -fPIC *.c -o liball.so
