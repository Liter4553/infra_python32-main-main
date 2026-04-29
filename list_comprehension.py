#server_list = []

#for i in range(0, 10):
#    server = f"SVG-{i+1:02d}"
#   server_list.append(server)

#print(server_list)


server_list = [f"SVG-{i+1:02d}" for i in range(0, 10) if i % 2 ==1]
print(server_list)