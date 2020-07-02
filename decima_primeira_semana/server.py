from bottle import Bottle

from url import app as urls


app = Bottle()
app.merge(urls)
app.run(host='0.0.0.0')
