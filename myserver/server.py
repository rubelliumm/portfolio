# import socket

# HOST = '0.0.0.0'
# PORT = 8080


# class server():
#     def __init__(self):
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#             s.bind((HOST, PORT))
#             print('server created at: ... localhost')
#             s.listen()
#             conn, addr = s.accept()
#             while conn:
#                 print(f'Connected by {addr}')
#                 while True:
#                     data = conn.recv(1024)
#                     if not data:
#                         break
#                     conn.sendall(data)
