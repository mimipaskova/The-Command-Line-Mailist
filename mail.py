from user import User
from json import dumps
from json import loads

def help():
    print("Here is a full list of commands:")
    print("* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier")
    print("* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>")
    print("* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.")
    print("* update_subscriber <unique_list_identifier> <unique_name_identifier> - updates the information for the given subscriber in the given list")
    print("* remove_subscriber <unique_list_identifier> <unique_name_identifier> - Removes the given subscriber from the given list")
    print("* create <list_name> - Creates a new empty list, with the given name.")
    print("* update <unique_list_identifier>  <new_list_name> - Updates the given list with a new name.")
    print("* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.")
    print("* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.")
    print("* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.")
    print("* exit - this will quit the program")

def show_lists(lists):
    for i in range(len(lists)):
        print("[%d] %s"%(i + 1, lists[i].list_name)

def show_list(list_of_users):
    for i in range(len(list_of_users)):
        print("[%d] %s - %s"% (i + 1, list_of_users[i].name, list_of_users[i].email))

def add_subscriber(lists, listname):
    name = input("name>")
    email = input("email>")
    new_user = User(name, email)
    lists.add(new_user, listname)

def import_from_json(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return json.loads(content)

def export(dictionary, filename):
    file = open(filename + ".json", "w")
    file.write(dumps(dictionary))
    file.close()



def main():
    print("Hello Stranger! This is a cutting-edge, console-based mail-list!\n" +
        "Type help, to see a list of commands.\n")

    while True:
        command = input(">")
        if command == "help":
            help()



if __name__ == '__main__':
    main()