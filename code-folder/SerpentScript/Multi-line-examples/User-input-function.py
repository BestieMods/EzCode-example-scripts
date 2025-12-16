def UserInput(prompt)
  user_value = input(prompt)
  return user_value
name = UserInput("Enter your username: ")
print("Hello, " + name + ", change the script to use the UserInput function anywhere, you can even build a MadLibs game!")
