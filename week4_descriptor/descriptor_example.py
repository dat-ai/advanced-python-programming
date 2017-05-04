# Example of how to use descriptors
# TL;DR : Create an alias to existing attributes

class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print("fetch...")
        return self._name

    def set_name(self, value):
        print("Change...")
        self._name = value

    def delete_name(self):
        print("Removing...")
        del self._name

    # Alias name --> _name
    name = property(fget=get_name,
                    fset=set_name,
                    fdel=delete_name,
                    doc="An Alias to self._name")

p = Person("Dat 1")
print(p.name)

p.set_name("Dat 2")
print(p.name)


print("This object is : ", p.name)
X.attr