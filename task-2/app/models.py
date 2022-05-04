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

    def to_dict(self):
        # TODO: add options to hide/show some fields data
        data = {
            'employee_id': self.employee_id,
            'last_name': self.last_name,
            'first_name': self.first_name,
            'title': self.title,
            'reports_to': self.reports_to,
            'birth_date': self.birth_date,
            'hire_date': self.hire_date,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'postal_code': self.postal_code,
            'phone': self.phone,
            'fax': self.fax,
            'email': self.email
        }

        return data