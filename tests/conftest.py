import os

# Define the path to the __init__.py file inside tests/
init_file = os.path.join(os.path.dirname(__file__), "__init__.py")

# Check if __init__.py exists, if not, create it
if not os.path.exists(init_file):
    open(init_file, 'w').close()
