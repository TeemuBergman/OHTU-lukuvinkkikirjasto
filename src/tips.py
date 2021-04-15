#from .db_wrapper import db_wrapper as default_db_wrapper
import string


class Tips:
    def __init__(self, db_handler):
        self.db_handler = db_handler
        self.allowed_name_chars = string.ascii_letters + string.digits + "åäöÅÄÖ .,@%_"
        self.allowed_url_chars = string.ascii_letters + string.digits + "%/:.@?_=-"
        self.allowed_name_length = 100
        self.allowed_url_length = 200
        self.allowed_min_length = 3

    def add_tip(self, author: str, url: str):
        if self.validate(author, self.allowed_name_chars, self.allowed_name_length, self.allowed_min_length) and \
                self.validate(url, self.allowed_url_chars, self.allowed_url_length, self.allowed_min_length
        ):
            fake_user_id = 0
            fake_book_name ="name of book here"
            tip_data = {"author": author, 
                        "url": url, 
                        "user_id": fake_user_id,
                        "book_name": fake_book_name
                        }
            return self.db_handler.insert(tip_data)
        else:
            print("not valid input")
            return False


    # for input validation.
    # parameters:
    # field = the actual value
    # encoding = accepted chars
    # max_length = maximum length of field
    # min_length = minimum lenght of field
    def validate(self, field, encoding: str, max_length: int, min_length: int):
        if len(field) > max_length or len(field) < min_length:
            print(f"Validate: fault: {field} is too long or short")  # debug info
            return False

        for character in field:
            if character not in encoding:
                print(f"Validate: fault: {character} is not in {encoding}")  # debug info
                return False

        return True

    def display_all(self):
        return self.db_handler.display_all_tips()

    def search_by_writer_name(self, name: str):
        if self.validate(name, self.allowed_name_chars, self.allowed_name_length, self.allowed_min_length):
            result = self.db_handler.search_by_writer_name(name)
            if len(result) > 0:
                return result
