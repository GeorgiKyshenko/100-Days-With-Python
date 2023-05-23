enemies = 1
soldiers = 1


# we can not modify global variable inside a function (local scope) without the key word - "global"
# it is not a good practice to modify global variable inside a local scope !!!
def func_modify_enemies():
    enemies = 2
    print(f"Inside the local scope the enemies are {enemies}")


def func_modify_soldiers(modify_soldiers):
    return modify_soldiers + 1


func_modify_enemies()
print(f"Outside of the local scope the enemies are {enemies}")
soldiers = func_modify_soldiers(soldiers)
print(soldiers)
