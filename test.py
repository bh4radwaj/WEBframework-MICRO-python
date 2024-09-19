#!/usr/bin/python3
from core import Micro
from controller import Controller
import secrets

app = Micro
PORT = 5000

app.set('views','./templates')
app.set('secret',secrets.token_hex(10))

app.get('/', Controller.index)
app.get('/about', Controller.about)
app.get('/services', Controller.services)
app.get('/login', Controller.getLogin)
app.get('/register', Controller.getRegister)

app.post('/register', Controller.register)
app.post('/login', Controller.login)

app.run('127.0.0.1',PORT)

