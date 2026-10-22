import logging

logging.basicConfig(
    filename="login.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

employees={
    "jerin":"abc",
    "cyril":"def"
}

class InvalidLoginError(Exception):
    pass

attempts=0
max_attempts=3

while attempts<max_attempts:
    try:
        username=input("Enter username:")
        password=input("Enter password:")
        
        if username not in employees or employees[username]!=password:
            raise InvalidLoginError("Invalid username or password")
        
        print("Login Successfull")
        logging.info(f"Successfull Login: {username}")
        break
    except InvalidLoginError as e:
        attempts+=1
        print("Login Failed")
        logging.warning(f"Failed login attempt: {username}")
    
    except Exception as e:
        print("An error occurred")
        logging.error(f"Error: {e}")
    
else:
    print("Maximum login attempt exceeded. Try again")
    logging.error(f"Maximum login attempt exceeded")