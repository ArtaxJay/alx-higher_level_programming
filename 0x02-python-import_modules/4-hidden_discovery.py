import py_compile

# Compile the .pyc file to .py
py_compile.compile('hidden_4.pyc')

# Import the module and list its names
import hidden_4

for nm in dir(hidden_4):
    if not nm.startswith("__"):
        print(nm)
