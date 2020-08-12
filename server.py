from flask import Flask , render_template  ,request , redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
   
@app.route('/<string:page_name>')
def open_page_html(page_name):
    return render_template(page_name +'.html')
   

@app.route('/submit_form', methods=['POST', 'GET'])
def login():
	if request.method =='POST':
		data = request.form.to_dict()
		write_to_database(data)
		write_to_csv(data)
		return redirect('/tnx')
			

def write_to_database(data):
	with open('database.txt' , 'a+') as database:
		database.write(str(data)+'\n')

def write_to_csv(data):
	email = data['email']
	subject = data['subject']
	message = data['message']
	with open('database.csv' , 'a' , newline='') as database_csv:
		writer = csv.writer(database_csv , delimiter=',',   quotechar='"' , quoting=csv.QUOTE_MINIMAL)
		writer.writerow([email,subject,message])
