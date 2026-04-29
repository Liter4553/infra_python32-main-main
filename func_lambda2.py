people = [
    {"name": "Alice", "age": 25, "city": "Seoul"},
    {"name": "Bob", "age": 30, "city": "Busan"},
    {"name": "Charlie", "age": 28, "city": "Incheon"},
    {"name": "David", "age": 35, "city": "Daegu"},
    {"name": "Eve", "age": 22, "city": "Daejeon"},
    {"name": "Frank", "age": 40, "city": "Gwangju"},
    {"name": "Grace", "age": 27, "city": "Suwon"},
    {"name": "Hannah", "age": 33, "city": "Ulsan"},
    {"name": "Ian", "age": 29, "city": "Jeju"},
    {"name": "Jane", "age": 31, "city": "Sejong"}
]

def after10y(v):
    v["age"] + 10


#print(list(map(lambda v: v{"name": v["name"], "age": v["age"] + 10}, people)))
people = list(map(lambda x: {**x, "age": x['age'] + 10}, people))
print(people)