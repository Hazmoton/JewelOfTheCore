from flask import Flask, render_template, request
# Flask is thw webpage app holder ig,
# render_template lets merender html templates??? 
# request handles inomming requests, like form submissions


# Creating a Flask instance
app=Flask(__name__)
#Home route
@app.route('/')
def home():
    #return "<h1>Welcome to My Flask App AHHHH!</h1>"
    return render_template('quiz.html')
#Defines a new route, result, which handles the posting
@app.route('/result',methods=['POST'])
def result():
    #this defines the function, result()
    answer1=request.form.get('question1')
    answer2=request.form.get('question2')
    answer3=request.form.get('question3')
    # descision matrix is here
    if answer1=='1' and answer2=='1' and answer3=='1':
        color='Blue'
    elif answer1=='2' and answer2=='2' and answer3=='2':
        color='Red'
    else:
        color='Green'
    return render_template('result.html',color=color)

#Run app if file is executed directly
if __name__=='__main__':
    app.run(debug=True)