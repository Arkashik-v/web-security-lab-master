import base64

import json


token = input("JWT: ").strip()

parts = token.split(".")

if len(parts) != 3:

    raise ValueError("JWT должен содержать 3 части")


def read_part(value):

    padded = value + "=" * (-len(value) % 4)

    raw = base64.urlsafe_b64decode(padded)

    return json.loads(raw.decode("utf-8"))


print("HEADER:")

print(json.dumps(read_part(parts[0]), indent=2))

print("PAYLOAD:")

print(json.dumps(read_part(parts[1]), indent=2))

print("SIGNATURE (Base64url):", parts[2])