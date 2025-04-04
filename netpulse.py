import socket
import sys
import os
from colorama import Fore, Style
if "--help" in sys.argv:
    print(f"""
                        {Fore.RED}NetPulse Listener{Style.RESET_ALL}
{Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}{Fore.GREEN}-c{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}]{Style.RESET_ALL}: {Fore.LIGHTBLACK_EX}Listen continuously{Style.RESET_ALL}
{Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}{Fore.GREEN}-p {Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}<PORT>{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}]{Style.RESET_ALL}: {Fore.LIGHTBLACK_EX}Listen on port. Use {Fore.GREEN}--raw{Style.RESET_ALL}{Fore.LIGHTBLACK_EX} flag if your service is not web-based.{Style.RESET_ALL}
{Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}{Fore.GREEN}-r {Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}<FILE>{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}]{Style.RESET_ALL}: {Fore.LIGHTBLACK_EX}Response to show{Style.RESET_ALL}
""")
    sys.exit()
HOST = "0.0.0.0"
PORT = 80
continuous = False
response_body = "NetPulse Listener works!"
args = sys.argv[1:]
i = 0
while i < len(args):
    if args[i] == "-c":
        continuous = True
    elif args[i] == "-p" and i + 1 < len(args):
        try:
            PORT = int(args[i + 1])
            i += 1
        except ValueError:
            print(f"{Fore.RED}[!]{Style.RESET_ALL} {Fore.YELLOW}Invalid port number{Style.RESET_ALL}")
            sys.exit(1)
    elif args[i] == "-r" and i + 1 < len(args):
        file_path = args[i + 1]
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    response_body = file.read()
            except Exception as e:
                print(f"{Fore.RED}[!]{Style.RESET_ALL} {Fore.YELLOW}Error reading file: {e}{Style.RESET_ALL}")
                sys.exit(1)
        else:
            print(f"{Fore.RED}[!]{Style.RESET_ALL} {Fore.YELLOW}File not found: {file_path}{Style.RESET_ALL}")
            sys.exit(1)
        i += 1
    i += 1
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
    except Exception as e:
        print(f"{Fore.RED}[!]{Style.RESET_ALL} {Fore.YELLOW}An exception occurred: {e}{Style.RESET_ALL}")
        sys.exit(1)
    print(f"{Fore.BLUE}[*]{Style.RESET_ALL} {Fore.YELLOW}Listening on {HOST}:{PORT}{Style.RESET_ALL}" if not continuous else f"{Fore.BLUE}[*]{Style.RESET_ALL} {Fore.YELLOW}Listening on {HOST}:{PORT} continuously{Style.RESET_ALL}")
    print(f"{Fore.BLUE}[*]{Style.RESET_ALL} {Fore.YELLOW}Press{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}CTRL + C{Style.RESET_ALL} {Fore.YELLOW}to exit.{Style.RESET_ALL}")
    while True:
        try:
            client_socket, addr = server_socket.accept()
        except KeyboardInterrupt:
            print(f"\n{Fore.LIGHTRED_EX}[X]{Style.RESET_ALL} {Fore.YELLOW}Server shutting down.{Style.RESET_ALL}")
            sys.exit()
        print(f"{Fore.GREEN}[+]{Style.RESET_ALL} {Fore.YELLOW}Connection received from {addr}{Style.RESET_ALL}")
        request = client_socket.recv(1024).decode()
        print(f"{Fore.GREEN}[+]{Style.RESET_ALL} {Fore.YELLOW}Received: \n{Fore.CYAN}{request}{Style.RESET_ALL}")
        if "--raw" not in sys.argv:
            response = f"""
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: {len(response_body)}

{response_body}
"""
        else:
            response = response_body
        client_socket.sendall(response.encode())
        client_socket.close()
        if not continuous:
            print(f"{Fore.LIGHTRED_EX}[X]{Style.RESET_ALL} {Fore.YELLOW}Exiting. Use -c to listen continuously.{Style.RESET_ALL}")
            break