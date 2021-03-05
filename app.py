from flask import Flask,render_template,request
app = Flask(__name__,template_folder="templates")

@app.route('/')
@app.route('/index')
def hello():
    return render_template('index.html')

@app.route('/data',methods=['POST'])
def func_name():    
    temp = ""    
    actual_data = {}

    for data in request.form:
        
        # Splits the Name of the Data Sent
        dataset = data.split('_')
        
        print(data)        



        
    return actual_data

if __name__ == '__main__':
    app.run(debug=True,port=5000)