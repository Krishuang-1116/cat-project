from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        name = request.form['name']
        age = float(request.form['age'])
        weight = float(request.form['weight'])
        body_temp = float(request.form['body_temp'])
        vomit = 'vomit' in request.form  

        health_status = f"{name} is {age} years old and weighs {weight} kg."
        if body_temp > 39.5 and vomit:
            detailed_status = "High risk of FIP. Visit a vet immediately."
        else:
            detailed_status = "No immediate concerns detected."

        return render_template('result.html', health_status=health_status, detailed_status=detailed_status)
    
    return render_template('check.html')

@app.route('/criteria')
def criteria():
    return render_template('criteria.html')

if __name__ == '__main__':
    app.run(debug=True)
