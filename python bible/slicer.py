# get user's email address
email = input("What is your email address?: ").strip()
# slice out the username
user = email[:email.index("@")]
print(user)
# slice out domain name
domain = email[email.index("@")+1:]
print(domain)
# format message
output = "Your username is {} and your domain name is {}".format(user, domain)
# display output message
print(output)
