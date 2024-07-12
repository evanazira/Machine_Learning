class circle:

    def __init__(self, radius):
        #change 
        self._radius = 0 #Initialize
        if (isinstance(radius,int)):
            self._radius = radius
        else:
            print("Invalid Radius")
    
    #getter method and setter method
    def getRadius(self):
        return self._radius

    def setRadius(self, radius):
        if(isinstance(radius,int)):
            self._radius = radius

        else:
            print("Invalid radius")

        
    #property is a class
    #we are calling/invoking the calss by passing the method as argumnrt
    radius = property(getRadius, setRadius)

    def area(self):
        return 3.14 * self._radius *self._radius

    def circumstances(self):
        return 2*3.14*self._radius
    
    # def __str__(self):
    #     return f"Radius of the circle is {self._radius}"
    
mycircle = circle(20) #checking the instrontor is an  int
print(circle)
# mycircle._radius = 30
# mycircle.radius = 30  #must make it private
print(mycircle)
print(mycircle.area())