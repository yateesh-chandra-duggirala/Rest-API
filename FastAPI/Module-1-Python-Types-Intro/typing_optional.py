from typing import Optional

def say_hi(name : Optional[str] = None):
    if name is not None:
        print(f"hey {name}")
    else :
        print("Hello World")

say_hi(9)