class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores): # def init của Person được kế thừa bằng cách dùng hàm super()
        super().__init__(firstName, lastName, idNumber) # thao tác: gọi lại hàm __init__
        self.scores = scores
    def calculate(self):
        total = sum(scores)/int(len(scores))
        if 90 <= total <= 100:
            return 'O'
        elif 80 <= total < 90:
            return 'E'
        elif 70 <= total < 80:
            return 'A'
        elif 55 <= total < 70:
            return 'P'
        elif 40 <= total < 55:
            return 'D'
        elif total < 40:
            return 'T'
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())