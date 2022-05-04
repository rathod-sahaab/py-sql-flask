from app import app, models

@app.route('/')
@app.route('/index')
def index():
    employees = models.Employee.query.all()

    for employee in employees:
        print(employee.employee_id, employee.first_name, employee.last_name)

    return 'rendered'


@app.route('/users', )
def get_users():
    employees = models.Employee.query.all()

    for employee in employees:
        print(employee.employee_id, employee.first_name, employee.last_name)
