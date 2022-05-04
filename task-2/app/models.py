from app import db

class Employee(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column('EmployeeId', db.Integer, primary_key=True)
    last_name = db.Column('LastName', db.String(20))
    first_name = db.Column('FirstName', db.String(20))
    title = db.Column('Title', db.String(30))
    reports_to = db.Column('ReportsTo', db.Integer)
    birth_date = db.Column('BirthDate', db.DateTime)
    hire_date = db.Column('HireDate', db.DateTime)
    address = db.Column('Address', db.String(70))
    city = db.Column('City', db.String(40))
    state = db.Column('State', db.String(40))
    country = db.Column('Country', db.String(40))
    postal_code = db.Column('PostalCode', db.String(10))
    phone = db.Column('Phone', db.String(24))
    fax = db.Column('Fax', db.String(24))
    email = db.Column('Email', db.String(60), index=True, unique=True)

    def __repr__(self):
        return f'<Employee {self.employee_id} - {self.first_name} {self.last_name}>'