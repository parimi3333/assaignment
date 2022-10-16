from flask import *
app = Flask(__name__)
heading1 = ('No','SKU','SKU Description','Standard Crate Quantity','Procured Quantity')
data1 = ('1','10000298','Mango Banganapalli 1kg','18000','36190')

heading = ('No','Crate','SKU','Packed Quantity','Crate Weight','Final crate')
data = (
    ('1','3e410b75b4','10000298','18100','18100','0'),
    ('2','7c2eba029c','10000298','18090','18090','0')
)

@app.route('/')
def fun2():
    return render_template('home.html',heading1=heading1,data1=data1,heading=heading,data=data)
if __name__ == '__main__':
    app.run()