from db_wrapper import db_wrapper as default_db_wrapper
import string


class Tips:
    def __init__(self, db_handler=default_db_wrapper):
        self.db_handler = db_handler
        self.allowed_name_chars = string.ascii_letters + string.digits + "åäöÅÄÖ .,@%_"
        self.allowed_url_chars = string.ascii_letters + string.digits + "%/:.@?_=-"
        self.allowed_name_length = 100
        self.allowed_url_length = 200
        self.allowed_min_length = 3

    def add_tip(self, name: str, url: str):
        if self.validate(name, self.allowed_name_chars, self.allowed_name_length, self.allowed_min_length) and \
                self.validate(url, self.allowed_url_chars, self.allowed_url_length, self.allowed_min_length):
            return self.db_handler.insert({"name": name, "url": url})
        else:
            print("not valid input")
            return False

    # parameters:
    # field = the actual value
    # encoding = accepted chars
    # length = maximum length of field
    # min_length = minimum lenght of field
    def validate(self, field, encoding: str, length: int, min_length: int):
        if len(field) <= length and len(field) >= min_length:
            for character in field:
                if character not in encoding:
                    return False
            return True

    def display_all(self):
        return self.db_handler.display_all_tips()

    def search_by_writer_name(self, name: str):
        if self.validate(name, self.allowed_name_chars, self.allowed_name_length, self.allowed_min_length):
            if self.db_handler.search_by_writer_name(name)[0]:
                return self.db_handler.search_by_writer_name(name)[1].fetchall()
