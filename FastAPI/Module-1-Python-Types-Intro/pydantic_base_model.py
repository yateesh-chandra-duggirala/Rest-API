from datetime import datetime

from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str = 'John Die'
    signup_ts : datetime = datetime.now()
    friends : list[int] = []

external_data = {
    "id" : "123",
    # "signup_ts" : "2019-01-03",
    "friends" : [1, "2", b"3"],
}

user = User(**external_data)
print(user)

print(user.id)