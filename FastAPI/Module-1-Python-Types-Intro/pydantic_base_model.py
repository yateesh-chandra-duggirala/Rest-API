from datetime import datetime

from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str = 'John Die'
    signup_ts : datetime = datetime.now()
    friends : list[int | float] = []

external_data = {
    "id" : "123",
    # "signup_ts" : "2019-01-03 00:00:00",
    "friends" : [1, 2.7, "3"],
}

user = User(**external_data)
user.signup_ts = user.signup_ts.strftime("%Y-%m-%d %H:%M:%S")
print(user)

print(user.id)