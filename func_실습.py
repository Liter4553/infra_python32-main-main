raw_data= [22, 80, 443, 8080, 21]

less_than_100 = list(filter(lambda x: x<100,raw_data))

selected_port = list(map(lambda port: f"{port}:OPEN", less_than_100))
print(selected_port)