'''import json


def test():
    myDict=["mimi"]
    json.dumps(myDict, open("test.json", "w"))
    print("blqq")

def main():
    print(test())


'''
import json
def main():
    data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
    print('DATA:', repr(data))

    data_string = json.dumps(data)
    print('JSON:', data_string)

if __name__ == '__main__':
    main()
