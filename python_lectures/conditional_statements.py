age = 18
if age >= 18:
	print("You are adult.:")
elif age == 60:
	print("You are senior.")
else:
	print("You are minor")


# ​​Ternary

status = "Adult" if age >= 18 else "Minor"
print(status)


# match case

role = "admin"

match role:
    case "admin":
        print("Welcome Admin")
    case "moderator":
        print("Welcome moderator")
    case "user":
        print("Welcome user")
    case _:
        print("Unrecognized role")
