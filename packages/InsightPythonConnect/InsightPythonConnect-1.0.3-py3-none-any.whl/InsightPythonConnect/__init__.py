from IPython.display import display, clear_output
import ipywidgets as widgets
import requests


def login():
    global login_uid; global login_pwd; global login_btn
    login_uid = widgets.Text(value='', placeholder='Enter username',description='Username')
    login_pwd = widgets.Password(value='',placeholder='Enter password', description='Password')
    login_btn = widgets.Button(description='Login')

    display(widgets.VBox([login_uid, login_pwd, login_btn]))
    login_btn.on_click(clickEvent)

def clickEvent(a):
    uid = login_uid.value
    pwd = login_pwd.value
    print('uid:',uid,'\npwd:',pwd)
    if not (uid.strip() and pwd.strip()):
        print('Username or password is Empty')
    else:  
        login_btn.on_click(get_url)

def get_url(a):
    login_uid.close()
    login_pwd.close()
    login_btn.close()
    clear_output()

    response = requests.get('https://proteusvision.com/ibase/login/index.html')
#     print(type(str(response)),str(response),)
    if str(response) == '<Response [200]>':
        display('Login Successful')
#         sessionId = ''
#         return sessionId
    else:
        print('Login Unsucessful')
    
def getVisual():
    login_uid.close()
    login_pwd.close()
    login_btn.close()
    clear_output()

#     if not sessionId:
#         print('You need to login first and then access getVisual ')
#     else:
    visualId_tbox = widgets.Text(
    value='',
    placeholder='Enter Visual id ',
    description='Visual Id: ',
    disabled=False
    )
    outputType__tbox = widgets.Text(
    value='',
    placeholder='Enter Output Type ',
    description='Output Type: ',
    disabled=False
    )

    Submit = widgets.Button(
    description='Submit',
    disabled=False,
    button_style='', 
    tooltip='Click me',
    icon='' 
    )
    display(widgets.VBox([visualId_tbox, outputType__tbox, Submit]))