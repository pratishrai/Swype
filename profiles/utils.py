def photo_path(instance, filename):
    return f"photos/{getattr(instance, 'id', filename)}"

def get_company_dict(company):
    return {
        'name': company.name,
        'bio': company.bio,
        'website_url': getattr(company, 'website_url', None),
        'linkedin_url': getattr(company, 'linkedin_url', None)
    }

def get_employee_dict(employee):
    return {
        'name': employee.name,
        'bio': employee.bio,
        'skills': getattr(employee, 'skills', None),
    }

def get_employer_dict(employer):
    return {
        'name': employer.name,
        'company': get_company_dict(employer.company or {})
    }
