#!/usr/bin/python3
import hidden_4

def main():
# Retrieve and sort the attributes as required
for name in sorted(dir(hidden_4)):
# Filter out dunder methods
if not name.startswith("__"):
print(name)

Ensure it runs only as a script
if name == "main":
main()
