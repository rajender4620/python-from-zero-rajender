"""🔥 Custom Error Classes in Python
If built-in exceptions like ValueError, TypeError, etc. don’t express your specific error case, you define your own by subclassing Exception.

✅ Step-by-Step Brutal Breakdown
1. Create a Custom Error Class
python
Copy
Edit
class WeakPasswordError(Exception):
    pass
Now you can raise WeakPasswordError(...) just like any built-in error.

2. Use It in a Function
python
Copy
Edit
def check_password(password):
    if len(password) < 6:
        raise WeakPasswordError("Password is too short!")
    print("✅ Password is strong.")
3. Handle It with try/except
python
Copy
Edit
try:
    check_password("abc")
except WeakPasswordError as e:
    print("❌ Custom Error Caught:", e)
✅ You Can Also Customize the Class
If you want to get fancy:

python
Copy
Edit
class WeakPasswordError(Exception):
    def __init__(self, password, message="Weak password detected"):
        self.password = password
        self.message = message
        super().__init__(f"{message}: '{password}'")
Usage:

python
Copy
Edit
raise WeakPasswordError("abc123")
Output:

nginx
Copy
Edit
Weak password detected: 'abc123'
🧪 Brutal Task
Make a custom exception class:

python
Copy
Edit
class InvalidAgeError(Exception):
    pass
Then use it in a function:

python
Copy
Edit
def validate_age(age):
    if age < 0:
        raise InvalidAgeError("Age can't be negative")
    print("Age is valid")
Test it with try/except."""
