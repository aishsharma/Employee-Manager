class Employee:
	def __init__(self, id: int, first_name: str, last_name: str, email: str, gender: str, salary: str):
		self.id = id
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.gender = gender
		self.salary = salary

	def __str__(self) -> str:
		string = f"{self.id}, {self.first_name} {self.last_name}, {self.gender}, {self.email}, {self.salary}"
		return string

	def get_tuple(self):
		return self.first_name, self.last_name, self.gender, self.email, self.salary
