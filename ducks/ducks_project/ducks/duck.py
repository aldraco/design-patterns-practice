import abc

# make a class for Ducks

class Duck(object):
    """Creates a Duck"""
    __metaclass__ = abc.ABCMeta
    # should have an instance of a flying behavior
    # should have an instance of a quack behavior

    @abc.abstractproperty
    def name(self):
        return "Abstract method"
        # Don't need to save a value for name on the base class.

    @name.setter
    def name(self, new_name):
        return;


    def __init__(self):
        if self.name:
            print "Hi, I'm a duck named {}.".format(self.name)
        else:
            print "Hi, I'm an anonymous duck."

        # question: can I also find the subclass's name to use it here?
        # I.e. can I say "I am a Mallard Duck named Ashley?"
    @abc.abstractproperty
    def flying_behavior(self):
        return "should never get here"

    @abc.abstractmethod
    def quack(self):
        # this works, even though this version of the class knows nothing about
        # a quack_behavior variable. I don't have to override this anywhere.
        # self.quack_behavior.quack()
        pass
        # I can either make this a concrete method that calls self.quack_behavior,
        # or I can make it an abstract method that does something or nothing.
        # If it's abstract then each inheriting class has to implement it to work.

    def fly(self):
        self.flying_behavior.fly()


    def display(self):
        pass

class QuackBehavior(object):
    """Abstract base class for quacking behaviors."""
    def quack():
        pass

class AudibleQuack(QuackBehavior):
    """Subclass implementation/interface for normal quacking"""
    def quack(self):
        print "QUACK QUACK QUACK!"

class NormalFlying(object):
    """Trying this without the intermediate class"""
    def fly(self):
        print "Flying gently across the sky"


class MallardDuck(Duck):
    #quack_behavior = AudibleQuack()
    #flying_behavior = NormalFlying()
    # You can set the values here to attach them to self, or
    # you can just use properties
    #species = "Mallard"
    # why does this work to attach variables to "self?"

    @property
    def flying_behavior(self):
        return NormalFlying()

    @property
    def quack_behavior(self):
        return AudibleQuack()

    @property
    def species(self):
        return "Mallard"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name



    def __init__(self, name=None):
        self.name = name
        return super(MallardDuck, self).__init__()

    def display(self):
        print "Look, I'm a Mallard Duck!"

    def quack(self):
        self.quack_behavior.quack()

    


# Observations:
# since ducks are dynamically typed, I am not required to declare the type of the quack behavior.
# So then how do I tell the base class to expect a quack behavior?

# How do I get to the instance variable's name and other items I might want ot use? super()?
# or where do I pass in instance variable state things, like a name for the duck?

# how to organize all of these base classes and implementations?
# Probably should look at Django to see how they do it?


