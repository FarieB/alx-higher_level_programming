#!/usr/bin/python3
import py_compile
import dis

if __name__ == "__main__":
    compiled_file = "hidden_4.pyc"

    # Load the compiled module
    try:
        code = py_compile.load_compiled("__hidden__", compiled_file)
    except FileNotFoundError:
        print(f"Error: {compiled_file} not found.")
        exit(1)

    # Extract and print names that do not start with __
    names = [name for name in dir(code) if not name.startswith("__")]

    # Sort and print the names
    for name in sorted(names):
        print(name)

