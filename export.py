import json
def main():
    data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
    #print('DATA:', repr(data))

    data_string = json.dumps(data)
    print(data_string)

if __name__ == '__main__':
    main()
