import base64   

def main():
    with open('/home/goodman/school/next.py/unit_6/msg.txt', 'r') as f:
        flag = f.read()

    print(base64.b64decode(flag).decode())

if __name__ == '__main__':
    main()