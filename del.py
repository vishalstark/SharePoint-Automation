import base64

PASSWORD = input('Enter password : ')
new_password = base64.b64encode(PASSWORD.encode("utf-8"))



actual_password = base64.b64decode(new_password).decode("utf-8")

print(f'Actual Password : {actual_password}')
