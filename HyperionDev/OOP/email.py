#An Email Simulation
class Email():
    def __init__(self, has_been_read, email_contents, is_spam, from_address):
        self.has_been_read = has_been_read
        self.email_contents = email_contents
        self.is_spam = is_spam
        self.from_address = from_address

    # The constructor should initialise the sender’s email address
    def get_from_address(self):
        return self.from_address
    
    # The constructor should also initialise has_been_read and is_spam to false.
    def get_has_been_read(self):
        self.has_been_read = False

    def get_is_spam(self):
        self.is_spam = False
    
    # Create a function in this class called mark_as_read which should change has_been_read to true.
    def mark_as_read(self):
        self.has_been_read = True
    
    # Create a function in this class called mark_as_spam which should change is_spam to true.
    def mark_as_spam(self):
        self.is_spam = True
    
# Create a list called inbox to store all emails (note that you can have a list of objects).
inbox = []

# add_email - which takes in the contents and email address from the received email to make a new Email object.
def add_email(email_contents, from_address):
    new_email = Email(False, email_contents, False, from_address)
    inbox.append(new_email)
    
# get_count - returns the number of messages in the store.
def get_count():
    return len(inbox)

# get_email - returns the contents of an email in the list. For this, allow the user to input an index 
# i.e. get_email(i) returns the email stored at position i in the list. Once this has been done, has_been_read should now be true.
def get_email(index):
    email = inbox[index]
    email.has_been_read = True
    return email.email_contents
    
# get_unread_emails - should return a list of all the emails that haven’t been read.
def get_unread_emails():
    unread_emails = []
    for email in inbox:
        if email.has_been_read == False:
            unread_emails.append(email)
    return unread_emails
    
#  get_spam_emails - should return a list of all the emails that have been marked as spam.
def get_spam_emails():
    spam_emails = []
    for email in inbox:
        if email.is_spam == True:
            spam_emails.append(email)
    return spam_emails
    
# delete - deletes an email in the inbox.
def delete(index):
    inbox.pop(index)
    
user_choice = ""


while user_choice != "quit":
    # display the list of emails and their indexes
    for i, email in enumerate(inbox):
        print(f"{i} - {email.email_contents}")
        print()
    user_choice = int(input("""What would you like to do 
    1. Read
    2. Mark Spam
    3. Send
    4. get_count
    5. get_spam_emails
    6. get_unread_emails
    7. delete
    8. quit
    : """))

    if user_choice == 1:
        # get the index of email to read
        index = int(input("Enter the index of the email you would like to read: "))
        # get the email contents
        if index < len(inbox):
            print(get_email(index))
        else:
            print("Invalid index. Please enter a valid index.")

    elif user_choice == 2:
        # get the index of the email to mark as spam
        index = int(input("Enter the index of the email you would like to mark as spam: "))
        # mark the email as spam
        if index < len(inbox):
            inbox[index].mark_as_spam()
            print("Email marked as spam")
        else:
            print("Invalid index. Please enter a valid index.")    
    
    elif user_choice == 3:
        # get the email contents
        email_contents = input("Enter the contents of the email you would like to send: ")
        # get the sender's email address
        from_address = input("Enter the sender's email address: ")
        add_email(email_contents, from_address)
        print("Email sent")

    elif user_choice == 4:
        print(f"There are {get_count()} emails in the inbox")

    elif user_choice == 5:
        print("Spam emails:")
        for email in get_spam_emails():
            print(email.email_contents)
        # spam_emails = inbox.get_spam_emails()
        # for email in spam_emails:
        #     print(email.email_contents)

    elif user_choice == 6:
        print("Unread emails:")
        for email in get_unread_emails():
            print(email.email_contents)
    
    elif user_choice == 7:
        index = int(input("Enter the index of the email you want to delete: "))
        delete(index)
        print("Email deleted")

    elif user_choice == 8:
        print("Quitting")
        break

    else:
        print("Oops - incorrect input")
