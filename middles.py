class Middles:

    def info(req):
        req.send_response(200)
        print(f'A GET TO :{req.path}')
        return req

    def post_info(req):
        print(f'A POST TO :{req.path}')
        data = req.getPostData()
        print(data)
        return req
