# 3. Создайте программу для игры в "Крестики-нолики".
#  1 | 2 | 3
# -----------
#  X |   |
# ---------
#   |   |

in_value = [[0 for i in range(3)] for j in range(3)]

print(in_value)

def my_field_display(arg_input):
    for i in range(len(arg_input)) :
        print(f"| {arg_input[i]} |")

# in_value = [ [f,f,f],
#              [f,f,f],
#              [f,f,f] ]

my_field_display(in_value)