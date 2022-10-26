 class UserUpdateMixin:
    def changePassword(self, new_password):
        self.password = new_password
class User(UserUpdateMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._original_username = username
    
    def _update_original_username(self):
        self._original_username = self.username
class UserExists(Exception):
    pass

class UserDatabase:
    def __init__(self):
        self.database = {}
    
    def add_user(self, user):
        if user.username in self.database:
            raise UserExists
        self.database[user.username] = user

    def get_users(self):
        return self.database

    def update_user(self, user):
        if user.username in self.database:
            raise UserExists
        
        self._update_original_username()
        self.database[user.username] = user
        del self.database[user._original_username]
class MainApp:
    def __init__(self):
        self.database = {}
        self.logged_in_user = None

    def show_main_menu(self):
        while True:
            print('1 - Register')
            print('2 - Login')
            print('3 - Logout')
            print('4 - Change Password')
            print('5 - Check Info')
            print('6 - Exit')

            _ = ""
            try: _ = int(input('What do you want to do? '))
            except ValueError:
              print('Incorrect Entry!')
            
            if _ == 6:
                print('Goodbye!')
                break

            if _ == 1:
                self.register()
            
            elif _ == 2:
                self.login()
                
            elif _ == 3:
                self.logout()
                
            elif _ == 4:
                self.change_password()

            elif _ == 5:
                self.checkInfo()

            else:
                print('Incorrect entry!, Try again?')

    def register(self):
        username = input('Username:')

        if username in self.database:
            print('This username is already taken.')
            return

        password = input('Password:')

        self.database[username] = User(username, password)
    
    def login(self):
        username = input('Username:')

        if username not in self.database:
            print('Username or password is not valid.')
            return

        password = input('Password:')

        user = self.database[username]

        if user.password != password:
            print('Username or password is not valid.')
            return
        
        self.logged_in_user = user
        print('Logged in.')
    
    def logout(self):
        if not self.logged_in_user:
            print('You are not logged in.')
            return
        
        self.logged_in_user = None
        print('Logged out.')

    def change_password(self):
        if not self.logged_in_user:
            print('You are not logged in.')
            return

        new_password = input('Password:')

        self.logged_in_user.change_password(new_password)
        print('Password changed.')

    def checkInfo(self):
        if self.logged_in_user:
            print(f'Your current Username: {self.logged_in_user.username}')
            print(f'Your current Password: {self.logged_in_user.password}')
        
        if not self.logged_in_user:
            print('Log in first!')
 def run_app():
    app = MainApp()
    app.show_main_menu()
