from middles import Middles
from core import Micro

class Controller:

    @Micro.middle(Middles.info)
    def index(req):
        req.setHeader('content-type','text/html')
        req.setHeader('Set-Cookie','name=test')
        req.sessions.set("sneee","sn!!")
        req.sessions.set("pword","2345")
        req.view('index.html')

    @Micro.middle(Middles.info)
    def about(req):
        # co = filter(None, req.headers.get_all('cookie', []))
        # cookie_str = ', '.join(co)
        # print(cookie_str)
        print(req.sessions.get("sneee"))
        req.sessions.set("kneee","kn!!")
        req.setHeader('content-type','text/html')
        req.view('about.html')

    @Micro.middle(Middles.info)
    def services(req):
        req.sessions.pop("kneee")
        req.setHeader('content-type','text/html')
        req.view('services.html')

    @Micro.middle(Middles.info)
    def getLogin(req):
        req.setHeader('content-type','text/html')
        req.view('login.html')

    @Micro.middle(Middles.info)
    def getRegister(req):
        req.send_response(200)
        req.view('register.html')

    @Micro.middle(Middles.post_info)
    def register(req):
        req.redirect('/login')

    # @Micro.middle(Middles.post_info)
    def login(req):
        data = req.getPostData()
        print("kbj")
        print(req.sessions.getAll())
        if(data['pword'][0]==req.sessions.get('pword') and req.sessions.get('sneee')=='sn!!'):
            req.redirect('/about')
        req.redirect('/')
