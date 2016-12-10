from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Welcome to my world!"


@app.route('/school')
def go_school():
    return redirect('http://techkids.vn')


@app.route('/bmi/<int:w>/<int:h>')
def yourbmi(w,h):
    bmi=w/(h*h/10000)
    result=""
    if bmi<16:
        result= "Serevely underweight"
    elif bmi<=18.5:
        result= "Underweight"
    elif bmi <=25:
        result= "Normal"
    elif bmi <= 30:
        result= "Overweight"
    else:
        result= "Obese"
    return render_template("BMI.html",h=h,w=w,result=result)


if __name__ == '__main__':
    app.run()
