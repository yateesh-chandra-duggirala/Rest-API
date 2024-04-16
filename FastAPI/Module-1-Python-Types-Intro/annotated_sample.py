from typing import Annotated

def say_hi(name : Annotated[str, "Metadata"]) -> str :
    return f"Hi {name}"

print(say_hi("Yateesh"))