raw_data= [22, 80, 443, 8080, 21]

less_than_100 = list(filter(lambda x: x<100,raw_data))

selected_port = list(map(lambda port: f"{port}:OPEN", less_than_100))
#list와 map은 반드시 list()로 한번 더 묶어주기
print(selected_port)