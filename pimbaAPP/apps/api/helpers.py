

def handle_uploaded_file(f):
    with open('media/uploads/{}'.format(f), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
