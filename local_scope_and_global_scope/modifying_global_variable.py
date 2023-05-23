enemies = 1


def modify_global_variable():
    global enemies
    enemies += 1


modify_global_variable()
print(enemies)
