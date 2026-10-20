capacity = 20
n = 5
bikes_list = [0, 4, 10, 18, 20]
status_list = []
service_requiered = 0

for i in range(len(bikes_list)):
    if bikes_list[i] == 0:
        service_requiered += 1
        status_list.append("EMPTY")
        print(f"OBSERVATION {i+1}: EMPTY")
    elif bikes_list[i] == capacity:
        service_requiered += 1
        status_list.append("FULL")
        print(f"OBSERVATION {i+1}: FULL")
    elif 4*bikes_list[i] <= capacity:
        service_requiered += 1
        status_list.append("LOW")
        print(f"OBSERVATION {i+1}: LOW")
    elif 4*(capacity - bikes_list[i]) <= capacity:
        service_requiered += 1
        status_list.append("HIGH")
        print(f"OBSERVATION {i+1}: HIGH")
    else:
        status_list.append("OK")
        print(f"OBSERVATION {i+1}: OK")
print(f"SERVICE REQUIRED: {service_requiered}")