import uuid


def upload_image_path(obj, filename):
    ext = filename.split(".")[-1]
    filename = f"blog/{uuid.uuid4()}.{ext}"
    return filename
