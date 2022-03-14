def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True
# validate_user("", -1)
# print(validate_user("", 1))
# print(validate_user("rabiul", 1))
# print(validate_user(88, 1)) # raise error because integer has no len function
# print(validate_user([], 1))
# print(validate_user(["name"], 1)) # will raise error
