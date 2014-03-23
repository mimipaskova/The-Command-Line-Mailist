from json import dumps
from json import loads
from maillist import MailList

def help():
    print("Here is a full list of commands:")
    print("* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier")
    print("* show_list <unique_list_identifier>- Prints all people,one person at a line, that are subscribed for the list. The format is: <Name> - <Email>")
    print("* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.")
    print("* update_subscriber <unique_list_identifier> <unique_name_identifier> - updates the information for the given subscriber in the given list")
    print("* remove_subscriber <unique_list_identifier> <unique_name_identifier> - Removes the given subscriber from the given list")
    print("* create <list_name> - Creates a new empty list, with the given name.")
    print("* update <unique_list_identifier>  <new_list_name> - Updates the given list with a new name.")
    print("* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.")
    print("* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.")
    print("* export <unique_list_identifier>- Exports the given list into JSON file,named just like the list. All white spaces are replaced by underscores.")
    print("* delete <unique_list_identifier> - Remove the given list from mail list")
    print("* exit - this will quit the program")

def show_lists(lists):
    new_format = []
    for i in range(len(lists)):
        new_format.append("[%d] %s"%(i + 1, lists[i].get_name()))
    return "\n".join(new_format)

def show_list(one_list):
    new_format = []
    elements = one_list.list_of_subscribers()
    for i in range(len(elements)):
        new_format.append("[%d] %s - %s"%((i + 1), elements[i][0], elements[i][1]))
    return "\n".join(new_format)

def add_subscriber(one_list):
    name = input("name>")
    email = input("email>")
    if one_list.is_add(email):
        return "A person with the given email <%s> is already in the list!"%(email)
    else:
        one_list.add_subscriber(name, email)
        return "%s <%s> was added to %s!"%(name, email, one_list.get_name())

def update_subscriber(one_list, index):
    elements = one_list.list_of_subscribers()
    if len(elements) > index and index >= 0:
        print("Updating: %s - %s"%(elements[index][0], elements[index][1]))
        new_name = input("enter new name>")
        new_email = input("enter new email>")
        if new_name != "" and new_email != "":
            one_list.update_subscriber(elements[index][0], new_name, new_email)

def remove_subscriber(one_list, index):
    elements = one_list.list_of_subscribers()
    if len(elements) > index and index >=0:
        one_list.remove_subscriber(elements[index][1])
        print("<%s> was removed from the list <%s>"%(elements[index][0], one_list.get_name()))

def create_list(listname):
    new_list = MailList(listname)
    return new_list

def has_list(lists, listname):
    for l in lists:
        if l.get_name() == listname:
            return True
    return False

def delete_list(lists, index):
    if len(lists) > index:
        agreement = input("Are you sure you want to delete <Hack Bulgaria>?\nY/N>")
        if agreement == "Y":
            new_list = []
            for i in range(len(lists)):
                if i != index:
                    new_list.append(lists[i])
            print("<%s> was deleted"%(lists[index].get_name()))
            return new_list
        else:
            print("You crazy bastard. Stop playing with fire!")

def update_listname(lists, listname, new_list_name):
    for l in lists:
        if l.get_name() == listname:
            l.set_name(new_list_name)

def search_email(lists, email):
    where = []
    for i in range(len(lists)):
        if lists[i].is_add(email):
            where.append("[%d] %s"%(i + 1, lists[i].get_name()))
    return where

def merge_lists(list1, list2, new_list):
    new_content = list1.merge_lists(list2.get_subscribers())
    for key in new_content:
        new_list.add_subscriber(key, new_content[key])

def import_from_json(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return json.loads(content)

def export(dictionary, filename):
    file = open(filename + ".json", "w")
    file.write(dumps(dictionary))
    file.close()

def split_command(command):
    return command.split(" ")

def main():
    lists = []
    print("Hello Stranger! This is a cutting-edge, console-based mail-list!\n" +
        "Type help, to see a list of commands.\n")
    while True:
        command = input(">")
        com = split_command(command)
        if com[0] == "help":
            help()
        elif com[0] == "show_lists":
            print(show_lists(lists))
        elif com[0] == "show_list" and len(com) == 2:
            if len(lists) > int(com[1]) - 1:
                print(show_list(lists[int(com[1]) - 1]))
            else:
                print("List with unique identifier <%d> was not found!"%(int(com[1])))
        elif com[0] == "add" and len(com) == 2:
            if len(lists) > int(com[1]) - 1:
                print(add_subscriber(lists[int(com[1]) - 1]))
            else:
                print("List with unique identifier <%d> was not found!"%(int(com[1])))
        elif com[0] == "update_subscriber" and len(com) == 3:
            if len(lists) > int(com[1]) - 1:
                if len(lists[int(com[1]) - 1].list_of_subscribers()) >= int(com[2]):
                    update_subscriber(lists[int(com[1]) - 1], int(com[2]) - 1)
                else:
                    print("Subscriber with identifider <%d> was not found in the list <%s>"%(int(com[2]), lists[int(com[1]) - 1].get_name()))
            else:
                print("List with unique identifier <%d> was not found!"%(int(com[1])))

        elif com[0] == "remove_subscriber" and len(com) == 3:
            if len(lists) > int(com[1]) - 1:
                if len(lists[int(com[1]) - 1].list_of_subscribers()) >= int(com[2]):
                    remove_subscriber(lists[int(com[1]) - 1], int(com[2]) - 1)
                else:
                    print("Subscriber with identifider <%d> was not found in the list <%s>"%(int(com[2]), lists[int(com[1]) - 1].get_name()))
            else:
                print("List with unique identifier <%d> was not found!"%(int(com[1])))

        elif com[0] == "create" and len(com) > 1:
            listname = " ".join(com[1::])
            if not has_list(lists, listname):
                lists.append(create_list(listname))
                print("New list <%s> was created."%(listname))
            else:
                print("A list with name <%s> already exists!"%(listname))

        elif com[0] == "update" and len(com) > 2:
            new_list_name = " ".join(com[2::])
            old_name = lists[int(com[1]) - 1].get_name()
            update_listname(lists, old_name, new_list_name)
            print("Updated <%s> to <%s>"%(old_name, new_list_name))

        elif com[0] == "delete" and len(com) == 2:
            if len(lists) > int(com[1]) - 1:
                lists = delete_list(lists, int(com[1]) - 1)
            else:
                print("List with unique identifier <%d> was not found!"%(int(com[1])))

        elif com[0] == "search_email" and len(com) == 2:
            where = search_email(lists, com[1])
            if where == []:
                print("<%s> was not found in the current mailing lists."%(com[1]))
            else:
                print("<%s> was found in:"%(com[1]))
                print("\n".join(where))
        elif com[0] == "merge_lists" and len(com) == 4:
            n, m = int(com[1]) - 1, int(com[2]) - 1
            if not has_list(lists, com[3]) and n >= 0 and m >= 0 and n < len(lists) and m < len(lists):
                lists.append(create_list(com[3]))
                merge_lists(lists[n], lists[m], lists[len(lists) - 1])
                print("Merged lists <%s> and <%s> into <%s>"%(lists[n].get_name(), lists[m].get_name(), com[3]))
            else:
                print("Incorrect input")

        elif com[0] == "exit":
            break
        else:
            print("Unknown command! Please type help!")



if __name__ == '__main__':
    main()
