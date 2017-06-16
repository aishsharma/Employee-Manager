import bottle
from bottle import response
from server import EmployeeDao

from server.models import Employee

app = bottle.Bottle()


@app.hook('after_request')
def enable_cors():
	"""
	You need to add some headers to each request.
	Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
	"""
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@app.route("/")
def health_check():
	return {"msg": "Hello World"}


@app.get("/api/employees")
def get_employees():
	employees = EmployeeDao.get_employees()
	return {"employees": employees}


@app.get("/api/employees/<employee_id:int>")
def get_employee(employee_id: int):
	employee = EmployeeDao.get_employee(int(employee_id))
	return {"employee": employee}


@app.post("/api/employees/new")
def new_employee():
	first_name = str(bottle.request.POST.first_name).strip()
	last_name = str(bottle.request.POST.last_name).strip()
	email = str(bottle.request.POST.email).strip()
	gender = str(bottle.request.POST.gender).strip()
	salary = round(float(str(bottle.request.POST.salary).strip()), 2)

	employee = Employee(-1, first_name, last_name, email, gender, str(salary))
	EmployeeDao.new_employee(employee)


@app.put("/api/employees/edit")
def edit_employee():
	id = int(str(bottle.request.POST.id).strip())
	first_name = str(bottle.request.POST.first_name).strip()
	last_name = str(bottle.request.POST.last_name).strip()
	email = str(bottle.request.POST.email).strip()
	gender = str(bottle.request.POST.gender).strip()
	salary = round(float(str(bottle.request.POST.salary).strip()), 2)
	employee = Employee(-1, first_name, last_name, email, gender, str(salary))
	EmployeeDao.update_employee(employee)
