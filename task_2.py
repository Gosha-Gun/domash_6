spamers_list = []
with open(file="nginx_logs.txt", mode='r', encoding="utf-8") as myfile:
    for line in myfile:
        remote_addr = line.split(" - - ")[0]
        spamers_list.append(remote_addr)
spamers = max(set(spamers_list), key=spamers_list.count)
spamers_numbers = spamers_list.count(spamers)
print(f"спамер с ip:{spamers} оставлял запрос на сайте {spamers_numbers} раз")

