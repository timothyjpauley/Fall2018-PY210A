print('+ '+'- '*4+'+ '+'- '*4+'+''\n'
+'|'+" "*9+'|'+' '*9+'|'+'\n'
+'|'+" "*9+'|'+' '*9+'|'+'\n'
+'|'+" "*9+'|'+' '*9+'|'+'\n'
+'|'+" "*9+'|'+' '*9+'|'+'\n'
+'+ '+'- '*4+'+ '+'- '*4+'+''\n'
+'|'+" "*9+'|'+' '*9+'|'+'\n'
+'|'+" "*9+'|'+' '*9+'|'+'\n'
+'|'+" "*9+'|'+' '*9+'|'+'\n'
+'|'+" "*9+'|'+' '*9+'|'+'\n'
+'+ '+'- '*4+'+ '+'- '*4+'+''\n')

a = '+ '+'- '*4+'+ '+'- '*4+'+'
b = '|'+" "*9+'|'+' '*9+'|'

print((a+'\n'+(b+'\n')*4)*2+a)



# solution 1
# triple quotes??
print("""+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +""")


# solution 2 : use variables, never repeat your code
def print_grid(n):
	print("+" + "-"*n + "+" + "-"*n + "+")
	print("|" + " "*n + "|" + " "*n + "|")
	print("+" + "-"*n + "+" + "-"*n + "+")
	print("|" + " "*n + "|" + " "*n + "|")
	print("+" + "-"*n + "+" + "-"*n + "+")

print_grid(5)	