class Urls:
    BASE_URL = "https://www.saucedemo.com/"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
    
class LoginData:
    VALID_LOGIN = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    
    GLITCH_LOGIN = "performance_glitch_user"
    LOCKED_LOGIN = "locked_out_user"
    WRONG_PASSWORD = "123456"
    
    EMPTY_LOGIN = ""
    EMPTY_PASSWORD = ""
    
class Messages:
    ERROR_INVALID_CREDENTIALS = "Epic sadface: Username and password do not match any user in this service"
    ERROR_LOCKED_OUT = "Epic sadface: Sorry, this user has been locked out."
    ERROR_USERNAME_REQUIRED = "Epic sadface: Username is required"
    
class Timeouts:
    IMPLICIT_WAIT = 5
    EXPLICIT_WAIT = 10