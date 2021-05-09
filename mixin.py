'''
 Mixin - это особый вид множественного наследования. 
 Есть две основные ситуации, в которых используются миксины: 
 Если хотите предоставить классу множество дополнительных функций. 
 Если хотите использовать одну особенность в разных классов.
'''


class Ancestor:
    def __init__(self):
        pass


class Parent1(Ancestor):
    def __init__(self, status):
        pass


class Parent2(Ancestor):
    def __init__(self, name):
        pass


class Child(Parent1, Parent2):
    pass

