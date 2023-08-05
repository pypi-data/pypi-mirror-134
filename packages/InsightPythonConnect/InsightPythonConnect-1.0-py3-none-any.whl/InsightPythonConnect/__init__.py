from IPython.display import display, clear_output
import ipywidgets as widgets

login_uid = widgets.Text(value='', placeholder='Enter username',description='Username')
login_pwd = widgets.Password(value='',placeholder='Enter password', description='Password')
login_btn = widgets.Button(description='Login')

def login():
    aa =display(widgets.VBox([login_uid, login_pwd, login_btn]))
    login_btn.on_click(clickEvent)
    
def clickEvent(a):
    uid = login_uid.value
    pwd = login_pwd.value
    print('uid:',uid,'\npwd:',pwd)
    
    if not (uid.strip() and pwd.strip()):
        print('Username or password is Empty')
    else:  
        
        login_btn.on_click(getVisual)
                
def getVisual(z):
    
    login_uid.close()
    login_pwd.close()
    login_btn.close()
    clear_output()
    
#     sessionId='abc'
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
    
