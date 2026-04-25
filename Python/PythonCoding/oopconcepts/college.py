class College:
    def __init__ (self, cname, ccode, ccity):
        self.collname = cname
        self.collcode = ccode
        self.collcity = ccity

    def welcome_message(self):
        print('Welcome to our College !!!')

    def display_college_details(self):
        print(f'College Code:{self.collcode}\n'f'College Name:{self.collname}\n'f'College City: {self.collcity}')
