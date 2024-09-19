#!/usr/bin/python3
from http.server import HTTPServer,BaseHTTPRequestHandler
import subprocess
# from pwn import *
import os
import cgi
import secrets
import json


from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random


def clean(st):
    last = ""
    for i in st:
        if i!='0':
            last+=i
    return last

def get_zf(st):
    ln = len(st)
    dv = int(ln/16)
    # print(dv)
    if dv==0: zf=16
    else: zf=(dv+1)*16
    return zf


# password = "testest"
# hasher = SHA256.new(password.encode('utf-8'))
# key =  hasher.digest()
# key = "A"*32

# iv = Random.new().read(16)
# iv = "hi".zfill(16)

# encryptor = AES.new(key,AES.MODE_CBC,iv)
# decryptor = AES.new(key,AES.MODE_CBC,iv)

# text = "HelloWorld!"



class Micro(BaseHTTPRequestHandler):
    gets = []
    posts = []
    # test
    sess = {"one":1}
    views = ''
    secret = ''


    def do_GET(self):
        print("heeeee")

        if self.path.endswith(".js"):
            # print("jsss")
            # print(111)
            # print(self.path)
            filename = self.path.strip('/')
            # print(filename)
            with open(self.views+'/'+filename,"r") as fl:
                # big bug found!!
                self.send_response(200)
                self.send_header("content-type","text/javascript")
                self.end_headers()
                cntnt = fl.read()
                self.wfile.write(cntnt.encode())

        if self.path.endswith(".css"):
            # print("jsss")
            # print(111)
            # print(self.path)
            filename = self.path.strip('/')
            # print(filename)
            with open(self.views+'/'+filename,"r") as fl:
                # big bug found!!
                self.send_response(200)
                self.send_header("content-type","text/stylesheet")
                self.end_headers()
                cntnt = fl.read()
                self.wfile.write(cntnt.encode())

        SELF = self
        class Sessions:
            def get(key):
                return SELF.sess.get(key)
            def set(key,value):
                SELF.sess.setdefault(key,value)
            def getAll():
                return SELF.sess
            def clear():
                SELF.sess = {}
            def pop(key):
                try:
                    SELF.sess.pop(key)
                except:
                    pass

        self = SELF
        self.sessions = Sessions



        co = self.headers.get_all('cookie', [])
        # print("len::"+str(len(co)))
        # print(co)
        # cookie_str = b', '.join(co)
        if(len(co)>=1):
            # print(co[-1])
            try:
                co = co[-1].split(';')[1].split('=')[-1]
            except:
                pass
            print(co)
            # print(1)
            dcted = subprocess.run(["./test.js","-D",co],capture_output=True).stdout.decode().strip('\n')
            # print(1)
            # print(2)
            print(dcted)
            print(2)
            self.sess = json.loads(dcted)
            print(self.sess)
            # enced = co[-1]
            # enced = enced.zfill(get_zf(enced))
            # print(decryptor.decrypt(enced.encode()))

        def setHeader(head,value):
            self.send_header(head,value)

        def end_head():
            all_ = self.sessions.getAll()
            st = json.dumps(all_)
            # print(st)
            enced = subprocess.run(["./test.js","-E",st],capture_output=True).stdout.decode().strip('\n')
            self.setHeader('Set-Cookie','decrypt_it='+enced)
            self.end_headers()
        self.end_head = end_head
        def view(template):
            self.end_head()
            if(self.views.endswith('/')):
                template = self.views+template
            elif not self.views.endswith('/'):
                template = self.views+'/'+template
            with open(template,'r') as f:
                cont = f.read()
                cont = cont.encode()
                self.wfile.write(cont)

        self.view = view
        self.setHeader = setHeader
        for i in self.gets:
            # print(f'this is i {i}')
            if(len(i.items())==1):
                for j in i.items():
                    # print(f'this is j {j}')
                    if(self.path.endswith(j[0])):
                        j[1](self)
            else:
                arr = []
                for j in i.items():
                    arr.append(j)
                if(self.path.endswith(arr[0][0])):
                    self = arr[1][1](self)
                    arr[0][1](self)

    def do_POST(self):

        def getPostData():
            a,b = cgi.parse_header(self.headers.get('content-type'))
            b['boundary'] = bytes(b['boundary'],'utf-8')
            b['CONTENT-LENGTH'] = int(self.headers.get('content-length'))
            if a=='multipart/form-data':
                data = cgi.parse_multipart(self.rfile,b)
                # print(data)
                return data

        def setHeader(head,value):
            self.send_header(head,value)

        def redirect(location):
            self.send_response(302)
            self.setHeader('Location',location)
            self.end_headers()



        def view(template):
            self.end_headers()
            if(self.views.endswith('/')):
                template = self.views+template
            elif not self.views.endswith('/'):
                template = self.views+'/'+template
            with open(template,'r') as f:
                cont = f.read()
                cont = cont.encode()
                self.wfile.write(cont)

        self.view = view
        self.setHeader = setHeader
        self.redirect = redirect
        self.getPostData = getPostData



        SELF = self
        class Sessions:
            def get(key):
                return SELF.sess.get(key)
            def set(key,value):
                SELF.sess.setdefault(key,value)
            def getAll():
                return SELF.sess
            def clear():
                SELF.sess = {}
            def pop(key):
                try:
                    SELF.sess.pop(key)
                except:
                    pass

        self = SELF
        self.sessions = Sessions


        # SELF = self
        # class Sessions:
            # def get(key):
                # return SELF.sess.get(key)
            # def set(key,value):
                # SELF.setHeader('Set-Cookie',str(key)+'='+str(value))
            # def pop(key):
                # try:
                    # SELF.sess.pop("key")
                # except:
                    # pass


        # self.sessions = Sessions

        # self.sessions.se

        for i in self.posts:
            # print(f'this is i {i}')
            if(len(i.items())==1):
                for j in i.items():
                    # print(f'this is j {j}')
                    if(self.path.endswith(j[0])):
                        j[1](self)
            else:
                arr = []
                for j in i.items():
                    arr.append(j)
                if(self.path.endswith(arr[0][0])):
                    self = arr[1][1](self)
                    arr[0][1](self)

    def middle(mid):
        def dec(og_func):
            def wrapper(self):
                self = mid(self)
                og_func(self)
            return wrapper
        return dec



    @classmethod
    def get(cls,path,func,**kwargs):
        if kwargs.get('middle'):
            cls.gets.append({path:func,'middle':kwargs.get('middle')})
        else:
            cls.gets.append({path:func})


    @classmethod
    def post(cls,path,func,**kwargs):
        if kwargs.get('middle'):
            cls.posts.append({path:func,'middle':kwargs.get('middle')})
        else:
            cls.posts.append({path:func})

    @classmethod
    def set(cls,key,value):
        if key=='views':
            cls.views = value
            print(f'views folder set to: {cls.views}')
        elif key=='secret':
            cls.secret = value
            print(f'secret set to: {cls.secret}')

    @classmethod
    def run(cls,host,port):
        server = HTTPServer((host,port),Micro)
        print(f'server started at http://localhost:{port}')
        server.serve_forever()



