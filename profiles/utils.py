def photo_path(instance, filename):
    return f"photos/{getattr(instance, 'id', filename)}"
