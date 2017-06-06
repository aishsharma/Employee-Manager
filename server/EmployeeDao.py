from typing import List, Tuple, Dict
from models import Employee

import sqlite3 as sqlite


def get_employees() -> List[Dict]:
	connection = sqlite.connect("Employees.sqlite")
	sql: str = "SELECT id, first_name, last_name, email, gender, salary FROM employees"

	cursor = connection.cursor()
	cursor.execute(sql)

	employees: List[Dict] = []

	for row in cursor:
		employee = Employee(id=row[0], first_name=row[1], last_name=row[2],
		                    email=row[3], gender=row[4], salary=row[5])
		employees.append(employee.__dict__)
	connection.close()

	return employees


def get_employee(employee_id: int) -> Dict:
	connection = sqlite.connect("Employees.sqlite")
	sql: str = "SELECT id, first_name, last_name, email, gender, salary FROM employees WHERE id = ?"

	cursor = connection.cursor()
	cursor.execute(sql, (employee_id,))

	row = cursor.fetchone();
	employee = Employee(id=row[0], first_name=row[1], last_name=row[2],
	                    email=row[3], gender=row[4], salary=row[5])
	connection.close()

	return employee.__dict__


def new_employee(employee: Employee):
	connection = sqlite.connect("Employees.sqlite")
	sql: str = "INSERT INTO employees(first_name, last_name, gender, email, salary) Values (?,?,?,?,?)"

	cursor = connection.cursor()
	print(cursor.execute(sql, employee.get_tuple()))

	connection.close()


def update_employee(employee: Employee):
	connection = sqlite.connect("Employees.sqlite")
	sql: str = """UPDATE employees 
		SET first_name = ?, last_name = ?, gender = ?, email = ?, salary = ?
		WHERE id = ?"""

	cursor = connection.cursor()
	cursor.execute(sql, (employee.first_name, employee.last_name, employee.gender, employee.email, employee.salary,
	                     employee.id,))

	connection.close()


def delete_employee(employee_id: int):
	connection = sqlite.connect("Employees.sqlite")
	sql: str = "DELETE FROM employees WHERE id = ?"

	cursor = connection.cursor()
	cursor.execute(sql, (employee_id,))

	connection.close()
