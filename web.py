from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)




    
@app.route("/")
def index ():
    return render_template('index.html')


@app.route("/<string:page_name>")
def page (page_name):
    return render_template(page_name)



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data=request.form.to_dict()
        write_to_csv(data)
        write_to_txt(data)
        return redirect('thankyou.html')

    else:
        return 'sorry something goes wrong'


def write_to_txt(data):
    with open('info.txt', mode='a')as database2:

        name=data['name']
        email= data['email']
        subject=data['subject']
        message= data['message']
        file= database2.write(f'\n{name},{email},{subject},{message}')

def write_to_csv(data):
    with open('info.csv', 'w', newline='') as database:
        name=data['name']
        email= data['email']
        subject=data['subject']
        message= data['message']
        csvwriter = csv.writer(database, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(['name','email','subject','message'])
        