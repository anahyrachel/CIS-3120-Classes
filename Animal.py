class Animal:
    def __init__(self, name, species): 
        self._name= name
        self._species= species
        print('Hello, I am', self._name, ',a', self._species)

    def talk(self):
        print('I', self._name,'like to bark')
    
    def eat (self, food):
        print ('I', self._name, 'like to eat' ,food )

    def sleep (self, hours):
        print ('I', self._name, 'like to sleep for' ,hours, 'hours')
    
    def play (self, toy):
        print ('I', self._name, 'like to play with' ,toy)
    
    def breed (self, breed):
        print ('I', self._name, 'am a', breed)
