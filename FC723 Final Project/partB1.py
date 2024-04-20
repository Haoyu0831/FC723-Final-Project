import string
import random

# Set to store existing booking references to make sure it is unique
existing_references = set()

# Define a function which can produce a random reference
def produce_reference():
    
    while True:
        # Generate a random string of 8 alphanumeric characters
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        # Check if it is unique by looking up in the existing references set
        if reference not in existing_references:
            existing_references.add(reference)
            return reference


print(produce_reference())