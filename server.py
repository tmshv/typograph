# -*- coding: utf-8 -*-

from flask import Flask, request
from EMT import EMTypograph
import cgi
import logging


app = Flask(__name__)
logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'/var/log/typograph.log')


def typo(data):
    EMT = EMTypograph()
    EMT.set_text(data)    
    result = EMT.apply()
    return result    


def get_unicode(data, e='utf-8'):
    try:    
        return data.decode(e)
    except:
        return None


@app.route('/', methods=['POST'])
def main():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    content_type, attrs = cgi.parse_header(request.headers['content-type'])
    if content_type.startswith('text/plain'):
        e = attrs['charset'] if 'charset' in attrs else 'utf-8'
        u = get_unicode(request.data, e)
        if u:
            logging.info(u'%s, %s' % (ip, u))
            return typo(u)
        else:
            return 'Wrong encoding. Use UTF-8', 400
    else:
        return 'Wrong format. Use text/plain', 400 



if __name__ == '__main__':
    app.run(host='0.0.0.0')

