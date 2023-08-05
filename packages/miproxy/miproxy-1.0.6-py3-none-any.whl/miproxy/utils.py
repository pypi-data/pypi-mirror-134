def interceptor(request, ip='1.33.184.141'):
    del request.headers['X-FORWARDED-FOR']
    request.headers['X-FORWARDED-FOR'] = ip
