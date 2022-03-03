with open(file="nginx_logs.txt", mode='r', encoding="utf-8") as myfile:
    for line in myfile:
        remote_addr = line.split(" - - ")[0]
        type_and_resource = line.split('"')[1]
        request_type = type_and_resource.split()[0]
        requested_resource = type_and_resource.split()[1]
        request_list = (str(remote_addr), str(request_type), str(requested_resource))
        print(request_list)
