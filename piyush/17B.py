class InvalidDateException(Exception):
    pass

class Date:
    def accept_date(self):
        self.day = int(input("Enter day: "))
        self.month = int(input("Enter month: "))
        self.year = int(input("Enter year: "))
    
    def display_date(self):
        if self.is_valid_date(self.day, self.month, self.year):
            print("Date:", self.day, "/", self.month, "/", self.year)
        else:
            raise InvalidDateException("Invalid date")
    
    def is_valid_date(self, day, month, year):
        if day < 1 or day > 31:
            return False
        if month < 1 or month > 12:
            return False
        if year < 0:
            return False
        return True

d = Date()
d.accept_date()
d.display_date()