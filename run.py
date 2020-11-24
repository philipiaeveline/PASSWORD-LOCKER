import random
import string
import pyperclip
class User:
    userList = []
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.isLoggedin = False
    def createUser(user_name, password):
        """
        method to create new user account
        """
        newUser = User(user_name, password)
        return newUser
    def login(self):
        """
        method that allows a user to login  credentials
        """
        print("Kudos. proceed")
    def saveUser(self):
        """
        method that adds user to the list
        """
        User.userList.append(self)
    @classmethod
    def displayUser(cls):
        """
        method that displays saved users
        """
        return cls.userList
    def deleteUser(self):
        """
        method that delete a selected user
        """
        User.userList.remove(self)
if __name__ == "__main__":
    pass
class Credentials:
    credentials = []
    def __init__(self, accountName, accountUsername, accountPassword):
        """
        crede
        """
        self.accountName = accountName
        self.accountUsername = accountUsername
        self.accountPassword = accountPassword
    def saveCredential(self):
        """
        method that adds credentials to the list
        """
        Credentials.credentials.append(self)
    @classmethod
    def createCredential(self, accountName, accountUsername, accountPassword):
        """
        method that creates a new credential
        """
        newCredential = Credentials(
            accountName, accountUsername, accountPassword)
        return newCredential
    def searchCredential(accountName):
        """
        method that searches a new credential and returns the credential
        """
        if Credentials.credentials:
            for credential in Credentials.credentials:
                if credential.accountName == accountName:
                    return credential
            print("No such an account")
        else:
            print("No credentials saved")
    def displayCredential():
        """
        methods to display all saved credentials
        """
        if (len(Credentials.credentials) > 0):
            return Credentials.credentials
    @classmethod
    def credentialExist(self, accountName):
        """
        method that checks if a credentials exists
        """
        if Credentials.credentials:
            for credential in Credentials.credentials:
                if credential.accountName == accountName:
                    return True
            print("No such an account")
        else:
            print("No credentials saved")
    def deleteCredential(accountName):
        """
        method that deletes a credential
        """
        for credential in Credentials.credentials:
            if credential.accountUsername == accountName:
                Credentials.credentials.remove(credential)
    def passwordGenerate(stringLength=8):
        """
        method that generate a random password
        """
        password = string.ascii_lowercase + string.ascii_uppercase + "#*%"
        return ''.join(random.choice(password) for i in range(int(stringLength)))
    def copypassword(parameter_list):
        """
        method that allows copying of password to keyboard
        """
        pass
if __name__ == "__main__":

    isTrue = True
    print("Hello.This is a website application where user will create an accont, login and save his/here account")
    while isTrue == True:
        print(
            "Use these short code to proceed:\n\n 1. c.acc-Create new Account\n 2. lgn-Login\n 3. exit-Exit")
        shortCode = input().lower()
        if shortCode == 'c.acc':
            print("New Account")
          
            print("Username")
            user_name = input()
            while True:
                print(
                    "1. own - own password?\n 2. random - generate random password")
                passwordOption = input()
                if passwordOption == 'own':
                    print("Your Password")
                    password = input()
                    break
                elif passwordOption == 'random':
                    password = Credentials.passwordGenerate()
                    break
                else:
                    print("PasswordOption Invalid")
            createUser = User.createUser(user_name, password)
            User.saveUser(createUser)
            print("\n")
            print(
                f"Hi {user_name} Your Account has been created sucessfully\n")
            print(f"Your username is {user_name} and password is {password}\n")
        elif shortCode == 'lgn':
            print("*"*3)
            print("Enter your username and password")
            print("*"*10)
            print("Username")
            user_name = input()
            print("Password")
            password = input()
            for user in User.userList:
                if user_name == user.user_name:
                    if user.password == password:
                        print(user.login())
                    else:
                        print("password invalid")
                        break
                else:
                    print("username Invalid")
                    break
            break
        elif shortCode == 'exit':
            print("Bye. See you some other time.")
            break
        else:
            print("Invalid shortcode\n")
    while True:
        print("What would like to do?\n\n Use these shortcodes to proceed\n 1. store - Store new Credential \n 2. show - Display existing Credential\n 3. see.acc - Find a credential \n 4. del.acc -  Delete an existing Credential \n 5. exit - Exit Application")
        shortCode = input().lower()
        if shortCode == 'store':
            print("New Credential Account")
            print("*"*50)
            print("\n")
            print("Account Name e.g Facebook")
            AccountName = input()
            print("Account's UserName")
            accountUserName = input()
            while True:
                print(
                    "1. own - You want to type your own password?\n 2. random -  generate random password")
                PasswordOption = input().lower()
                if PasswordOption == 'random':
                    print("Account's Password :")
                    accountPassword = input()
                    break
                elif PasswordOption == 'random':
                    accountPassword = Credentials.passwordGenerate()
                    break
                else:
                    print("Password Invalid")
            newC = Credentials.createCredential(
                AccountName, accountUserName, accountPassword)
            Credentials.saveCredential(newC)
            print("\n")
            print("Your Account's Credentials has been saved!")
            print("\n")
            


        elif shortCode == 'show':
            if Credentials.displayCredential():
                print("List of your credentials include:\n")
                for credential in Credentials.credentials:
                    accountName = credential.accountName
                    accountuser = credential.accountUsername
                    accountpass = credential.accountPassword
                    print(
                        f"Account Name : {accountName}\n Account Username : {accountuser}\n Account Password: {accountpass}\n")
            else:
                print("You do not have saved credentials at the moment\n")
        elif shortCode == 'see.acc':
            print("Account name: ")
            AccountName = input()
            if Credentials.credentialExist(AccountName):
                searchAccount = Credentials.searchCredential(AccountName)
                print(
                    f"Account name: {searchAccount.accountName}\n Account's Username: {searchAccount.accountUsername}\n Account's Password : {searchAccount.accountPassword}")
            else:
                print("No such an account name!\n")
        elif shortCode == 'del.acc':
            print("Account name you would like to delete?")
            AccountName = input()
            if Credentials.credentialExist(AccountName):
                Credentials.deleteCredential(AccountName)
                print("Account was deleted Successfully")
            else:
                print("No such an account name")
        elif shortCode == 'exit':
            print("Thank You So Much.Welcome once again")
            isTrue = False
        else:
            print("invalid short code")