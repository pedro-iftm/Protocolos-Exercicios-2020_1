from bottle import Bottle

from controller import app as contacts


app = Bottle()
app.merge(contacts)
app.run(host='0.0.0.0')
