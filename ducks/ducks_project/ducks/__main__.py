import duck

def main():
    print "Running!"

    print "testing a mallard duck:"
    drake = duck.MallardDuck(name="Ashley")
    drake.display()
    drake.quack()
    drake.fly()



if __name__ == "__main__":
    main()



# Questions
# 1 Why do I have to do duck.MallardDuck? If I import duck, doesn't it import all of the 
#   classes inside the module automatically?