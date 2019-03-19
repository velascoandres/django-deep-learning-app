def handle_uploaded_file(f):
    import uuid
    path = 'media/uploads/{}{}'.format(f.name, uuid.uuid4())
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        return path
