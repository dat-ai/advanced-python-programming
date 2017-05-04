
class Descriptor:
    def __get__(self, instance, owner):
        """
        Overriding an existing getter
        :param instance: whoever calling this Descriptor object
        :param owner: class of instance
        :return: attribute value
        """
        print(self, instance, owner)

        def __set__(self, instance, value):
            """
            :param instance: 
            :param value: 
            :return: none
            """
        def __delete__(self, instance):
            """
    
            :param instance: 
            :return: nothing 
            """


class Subject:
    attr = Descriptor()

X = Subject()
X.attr
