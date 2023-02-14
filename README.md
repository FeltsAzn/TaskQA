# The main task. 


To run the script you need to do the following:. Set the cryptography library to properly run the script from the terminal:

```bash
pip install cryptography
```

(click library may also be needed). 

Enter the folder with the script and place your data in the folder with the script (the script will search files relative to the folder. the script itself). 

Open the terminal in the script folder and write:
```bash
python ecdsa_digital_signature.py --f <source file> --s <digital signature of file> --k <Public key>```
```

Also can write:
```bash
python ecdsa_digital_signature.py

... Filename: <source file> 

... Signature: <digital signature of file> 

... Key: <Public key>
```
Note: The "task" folder contains test data. To use it, you need to write "task/",
before the file name. because the script will try to find files in its location folder.

## An additional task 

To run the web application on FastAPI, go to the fastapi_app file and start the start_app.py. 
(for easy start, open the IDE and install via pip file requirements.txt)

Or is located in the root folder and via the IDE terminal (in my case Pycharm) and write:
```bash
uvicorn fastapi_app.start_app:app
```

After file launch start_app.py in terminal will sent info: 

```bash
INFO:     Will watch for changes in these directories: ['<Полный путь месторасположения приложения>']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [14854] using StatReload
INFO:     Started server process [14856]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Next step is opening browser on http://127.0.0.1:8000/docs link and we can interact with API (FastAPI have a swagger for creation doc page).

### Main page
![Alt text](https://github.com/FeltsAzn/TaskQA/blob/master/screenshots/main_page.png)


### Endpoint for make a digital signature on this file

Push **"Try"**

Loading file, which you need signing


![Alt text](https://github.com/FeltsAzn/TaskQA/blob/master/screenshots/sign.png)




### Server response

Upload the digital signature of this file to your computer (click Download file)

![Alt text](https://github.com/FeltsAzn/TaskQA/blob/master/screenshots/sign_response.png)


### Verify the digital signature

To verify your file and digital signature, you need to send the original file and its digital signature (which you have downloaded from /sign).

!!! IMPORTANT: first the original file is downloaded, then the digital signature (also there is a limit of 2 files for correct verification)

![Alt text](https://github.com/FeltsAzn/TaskQA/blob/master/screenshots/verify.png)

### Server response

Get information about the validity of your file and its digital signature in response {resposne: ANSWER}

![Alt text](https://github.com/FeltsAzn/TaskQA/blob/master/screenshots/verify_response.png)

