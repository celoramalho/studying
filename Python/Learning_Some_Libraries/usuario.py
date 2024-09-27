class User:
    def __init__(self, private_data_file_path):
        with open(private_data_file_path, "r") as private_data_file:
            private_data = private_data_file.read().split('\n')
        
        self.name = private_data[0]
        self.mail = private_data[1]
        self.password = private_data[2]
        self.phone = private_data[3]
        
    def get_user_info(self):
        return {
            'name': self.__user_name,
            'mail': self.__user_mail,
            'phone': self.__user_phone
        }
    
    def update_user_mail(self, new_mail):
        self.__user_mail = new_mail

    def update_user_phone(self, new_phone):
        self.__user_phone = new_phone

    def update_password(self, new_password):
        self.__user_password = new_password

def display_user_info(self):
        print(f"User Name: {self.__user_name}")
        print(f"User Mail: {self.__user_mail}")
        print(f"User Phone: {self.__user_phone}")