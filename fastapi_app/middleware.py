from starlette.exceptions import HTTPException


def file_extension_sign(file):
    if file.filename.split('.')[1] != "sign":
        raise HTTPException(status_code=415, detail='Incorrect file extension')
    return file