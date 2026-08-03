from jose import jwt

# Secret key
SECRET_KEY = "mysecretkey"

# Payload (Dictionary)
data = {
    "user_id": 1,
    "username": "Fasiha"
}

# JWT Token banana (Sign)
token = jwt.encode(
    data,
    SECRET_KEY,
    algorithm="HS256"
)

print("Token:", token)

# JWT Verify karna
payload = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=["HS256"]
)

print("Payload:", payload)