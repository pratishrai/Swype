PLACEHOLDER_PHOTO_DICT = {
    'url': '/static/img/placeholder.png'
}

def photo_path(instance, filename):
    return f"photos/{getattr(instance, 'id', filename)}"

def get_company_dict(company):
    return {
        'name': company.name,
        'bio': company.bio,
        'website_url': getattr(company, 'website_url', None),
        'linkedin_url': getattr(company, 'linkedin_url', None),
        'photo': get_image_dict(company.photo) if company.photo else PLACEHOLDER_PHOTO_DICT
    }

def get_employee_dict(employee):
    return {
        'id': employee.id,
        'name': employee.name,
        'bio': employee.bio,
        'skills': getattr(employee, 'skills', None),
        'photo': get_image_dict(employee.photo) if employee.photo else PLACEHOLDER_PHOTO_DICT
    }

def get_employer_dict(employer):
    return {
        'id': employer.id,
        'name': employer.name,
        'company': get_company_dict(employer.company) if employer.company else None,
        'photo': get_image_dict(employer.photo) if employer.photo else PLACEHOLDER_PHOTO_DICT
    }

def get_image_dict(image):
    return {
        'url': image.url,
    }
