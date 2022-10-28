from fastapi.responses import FileResponse
from fastapi import APIRouter, UploadFile
from fastapi_app import middleware
from fastapi_app.verify import utils
from starlette.background import BackgroundTasks
from starlette.exceptions import HTTPException
import os


router = APIRouter()


def remove_files(path: str) -> None:
    """Delete signature FILE.sign in directory(temporary_files dir)"""
    os.remove(path)


@router.post("/sign")
async def get_signature_of_file(file: UploadFile) -> FileResponse:
    """Handler for presenting a server-signed file to the user"""
    filename = file.filename.split('.')[0]
    path = utils.asymmetric_encryption(file.file, filename=filename)

    back_task = BackgroundTasks()
    back_task.add_task(remove_files, path)

    return FileResponse(f"temporary_files/{filename}.sign",
                        filename=f"{filename}.sign",
                        media_type="application/data-form",
                        background=back_task
                        )


@router.post("/verify", description="first: file, second: digital signature")
async def check_digital_signature(files: list[UploadFile]) -> dict:
    """Handler for verifying the digital signature of a file"""
    if len(files) > 2 or len(files) < 2:
        raise HTTPException(status_code=422, detail='The number of uploaded files is more than 2. '
                                                    'You need to send a file and its digital signature')
    file, signature = files
    signature = middleware.file_extension_sign(signature)
    answer: bool = await utils.signature_validator(file, signature)
    return {"response": {"VALID" if answer else "INVALID"}}
