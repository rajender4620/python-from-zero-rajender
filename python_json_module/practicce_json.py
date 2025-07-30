import json

profile = "flutter"


with open("C:/python-from-zero-rajender/python_json_module/user_profile.json", "a") as f:

    json.dump(profile, f, indent=2)

# with open("C:/python-from-zero-rajender/python_json_module/user_profile.json", "r") as f:

#     print(json.load(f))
