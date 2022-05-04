from app import app, models

@app.route('/')
@app.route('/index')
def index():
    employees = models.Employee.query.all()

    for employee in employees:
        print(employee.employee_id, employee.first_name, employee.last_name)

    return 'rendered'


@app.route('/users', methods=['GET'])
def get_users():
    employees = models.Employee.query.all()

    return {"docs": [employee.to_dict() for employee in employees]}

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    print(id)
    employee = models.Employee.query.get(id)
    return employee.to_dict()

@app.route('/users', methods=['POST'])
def create_user():
    return 'created'

