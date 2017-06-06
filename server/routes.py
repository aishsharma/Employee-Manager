import bottle, decimal
from server import EmployeeDao
from server.models import Employee

from server.models import Employee

app = bottle.Bottle()


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


@app.put("/api/employees/edit")
def edit_employee():
	id = int(str(bottle.request.POST.id).strip())
	first_name = str(bottle.request.POST.first_name).strip()
	last_name = str(bottle.request.POST.last_name).strip()
	email = str(bottle.request.POST.email).strip()
	gender = str(bottle.request.POST.gender).strip()
	salary = round(float(str(bottle.request.POST.salary).strip()), 2)

	employee = Employee(-1, first_name, last_name, email, gender, str(salary))
