from flask import Flask, render_template, render_template_string, request

import csv
import matplotlib.pyplot as plt
import time


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def save_data():
    data1 = request.form['name']
    data2 = request.form['email']
    data3 = request.form['age']
    data4 = request.form['mobile']
    data5 = request.form['role']
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([data1, data2, data3, data4, data5])
    return render_template('success.html')

def get_role_count():
    role_count = {}
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[-1] not in role_count:
                role_count[row[-1]] = 1
            else:
                role_count[row[-1]] += 1
    return role_count

@app.route('/chart')
def show_chart():
    # Read the data from the CSV file
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        all_rounders = 0
        wicket_keepers = 0
        batsman = 0
        bowler = 0
        for row in reader:
         if len(row) >= 5:  # Only read the first 5 columns of each row
            if row[4] == 'all-rounder':
                all_rounders += 1
            elif row[4] == 'wicket-keeper':
                wicket_keepers += 1
            elif row[4] == 'batsman':
                batsman += 1
            elif row[4] == 'bowler':
                bowler += 1

    # Create the pie chart
    labels = ['All-rounders', 'Wicket-keepers','Batsman','Bowler']
    sizes = [all_rounders, wicket_keepers,batsman,bowler]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.set_title('Player Type Distribution')

    # Save the chart to a file
    plt.savefig('static/chart.png')

    # Render the HTML template
    chart_url = '/static/chart.png'
    return render_template('chart.html', chart_url=chart_url)


@app.route('/faq')
def faq():
    return render_template('faq.html')
def chatbot_response(message):
    var_time = time.ctime()
    qna = {
        "Hi" : "Hello",
        "hi" : "Hello",
        "Hello" : "Hi",
        "hello" : "Hi",
        "Hey" : "wassup",
        "hey" : "wassup",
        "what is your name" : "My name is ChatBot",
        "What is your name" : "My name is ChatBot",
        "how are you" : "I'am Fine, what about you",
        "How are you" : "I'am Fine, what about you",
        "I am fine" : "Ok",
        "i am fine" : "Ok",
        "Fine" : "Ok",
        "fine" : "Ok",
        "what is the time now" : var_time,
        "Bye" : "See you later",
        "bye" : "See you later",
        "ok" : "See you later",
        "Ok" : "See you later",
        "what is this website about" : "This is a Cricket Registration website",
        "what is analysis" : "it shows a pie chart according to position",
        "can you help me to register" : "sure , First fill the information on home page and submit,then check out the competition in analysis section",
        "can you help me register" : "sure , First fill the information on home page and submit,then check out the competition in analysis section",
        
    }

    return qna.get(message, "I'm sorry, I didn't understand that.")
@app.route('/faq', methods=['POST'])
def get_bot_response():
    user_message = request.form['message']
    bot_response = chatbot_response(user_message)
    return render_template('faq.html', message=user_message, response=bot_response)




@app.route('/table')
def table():
    with open('data.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))
    return render_template('table.html', data=data)


       
        

 

if __name__ == '__main__':
    app.run(debug=False)
