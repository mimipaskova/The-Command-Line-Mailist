class MailListFileAdapter():
    def __init__(self, mail_list):
        self.mail_list = mail_list

    def get_file_name(self):
        return self.mail_list.get_name().replace(" ", "_")

    def format_for_save(self):
        subscribers = self.mail_list.list_of_subscribers()
        subscribers = list(map(lambda x: "%s - %s"%(x[0], x[1]), subscribers)
        return subscribers

    def save_to_file(self):
        f = open(self.get_file_name(), "w")
        content = "\n".join(self.format_for_save())
        f.write(content)
        f.close()