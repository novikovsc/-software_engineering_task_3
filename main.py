import datetime

from fastapi import FastAPI

app = FastAPI()

item = {"1": "monday",
        "2": "tuesday",
        "3": "wednesday",
        "4": "thursday",
        "5": "friday",
        "6": "saturday",
        "7": "sunday"}



@app.get("/day/{day_of_week}")
async def read_item(day_of_week: int):
    if day_of_week == 1:
        return {"day": "monday"}
    if day_of_week == 2:
        return {"day": "tuesday"}
    if day_of_week == 3:
        return {"day": "wednesday"}
    if day_of_week == 4:
        return {"day": "thursday"}
    if day_of_week == 5:
        return {"day": "friday"}
    if day_of_week == 6:
        return {"day": "saturday"}
    if day_of_week == 7:
        return {"day": "sunday"}
    return {"item_id": "Not found"}


@app.post("/all")
async def root():
    return item

@app.post("/getdate")
async def root():
    return {"time": datetime.datetime.now()}
