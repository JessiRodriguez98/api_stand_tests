headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}
product_ids = {
    "ids": [1, 2, 3]
}


def get_user_body(first_name):
    body = user_body.copy()
    body["firstName"] = first_name
    return body
