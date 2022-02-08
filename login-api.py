def login(username, pwd):
    if username == pwd:
        return True
    else:
        return False
print(login("deepa", "deepa"))
print(login("deepa","sukum"))
