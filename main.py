# from turtle import Turtle, Screen
#
# slowy = Turtle()
#
# # print(slowy)
# slowy.shape("turtle")
#
# slowy.color("blue")
#
# # move the turtle forward by 100 paces
# slowy.forward(100)
#
# Screen().exitonclick()

# print(Screen().canvheight)

# Pretty Table

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])

table.align = "l"

print(table)