from flask import Flask, render_template, request
import copy, random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/introduction")
def introduction():
    return render_template("introduction.html")


QArray: {}


first_questions = {
    'According to the new 2017 NIST guidelines, how often should you change your password?': ['Never', 'Every month', 'Every 6 months', 'Every year'],
    'Which password would be considered the strongest?': ['$33H3rg0f@$t', 's3aSh311', 'tHur$d@y808', 'asdfghjkl123'],
    'Which Wireless Security Protocol is currently the strongest?': ['WPA3', 'WPA2', 'WPA', 'WEP'],
    'How effective is deleting a file off of your computer?': ['Not effective, it’s still possible for hackers to access it.', 'Somewhat effective, you just need to delete it from the recycle bin as well.', 'Effective, it’s still stored on the computer but hackers can’t access it.', 'Very effective, once deleted it’s gone forever.'],
    'Which of the following actions is the riskiest to do online?': ['Sharing pictures of landmarks while on vacation', 'Posting about your feelings', 'Posting pictures of your meals throughout the day', 'Sharing a funny experience you had that week'],
    'Should you use public wifi?': ['It’s okay as long as you use secure networks like VPN','No, it’s not safe at all','It depends on whoever is hosting the wifi','Public wifi provides you with the same security as private ones.'],
    'Which is the closest definition to phishing?': ['Disguising as a credible source in order to obtain personal information.', 'Hacking into a computer and searching (fishing) for personal information', 'A virus that goes through all the files on a computer and reports back the most relevant information.', 'A type of malware especially used against large companies and organizations.'],
    'What can you look at in an email in order to determine whether it is a phishing attempt?':['All options are correct', 'Any words or phrases that urge you to follow their instructions', 'Links included in the email', 'Sender’s email address'],
    'As of 2018, which types of malware are the most common?': ['Combination of many', 'Adware', 'Virus', 'Trojan'],
    'How can malware infect your computer?': ['All options are correct', 'Through spam emails', 'With an infected USB drive', 'Through downloaded software']
}


Quizquestions = copy.deepcopy(first_questions)

q = Quizquestions

correctquiz = 0

selected_keys = []


def shuffle(q):
    global selected_keys
    i = 0
    while i < len(q):
        current_selection = random.choice(list(q))
        if current_selection not in selected_keys:
            selected_keys.append(current_selection)
        i = i+1
    return selected_keys


@app.route('/questions')
def quiz():
    for i in Quizquestions.keys():
        random.shuffle(Quizquestions[i])
    return render_template('questions.html', q=Quizquestions, o=Quizquestions)


@app.route('/instructions', methods=['POST'])
def answers():
    for i in Quizquestions.keys():
        global correctquiz
        answered = request.form[i]
        if first_questions[i][0] == answered:
            correctquiz = correctquiz+1
    return '<h1> How to play: </h1> <h5> You have submitted your answers.</h5> ' \
           '<p> The following screen is supposed to simulate an email inbox for a Mr. John Doe. ' \
           'Going through the different emails sent to his inbox, identify which of the emails would be considered a ' \
           'phishing attempt. </p> <a href="/inbox">CONTINUE</a>'


second_questions = {
    'Email 1': ['No', 'Yes'],
    'Email 2': ['No', 'Yes'],
    'Email 3': ['Yes', 'No'],
    'Email 4': ['No', 'Yes'],
    'Email 5': ['Yes', 'No'],
}
gamequestions = copy.deepcopy(second_questions)

correctgame = 0


@app.route('/inbox')
def game():
    for i in gamequestions.keys():
        random.shuffle(gamequestions[i])
    return render_template('inbox.html', q=gamequestions, o=gamequestions)


@app.route("/email1")
def email1():
    return render_template("email1.html")


@app.route("/email2")
def email2():
    return render_template("email2.html")


@app.route("/email3")
def email3():
    return render_template("email3.html")


@app.route("/email4")
def email4():
    return render_template("email4.html")


@app.route("/email5")
def email5():
    return render_template("email5.html")


@app.route("/results", methods=['POST'])
def results():
    for i in gamequestions.keys():
        global correctgame
        answered = request.form[i]
        if second_questions[i][0] == answered:
            correctgame = correctgame+1
    return render_template("results.html")


@app.route("/finalresults")
def finalresults():
    return '<h1>Correct Questions (out of 10): <u>'+str(correctquiz)+'</u></h1>' \
           '<h1>Correct Identified Emails (out of 5): <u>'+str(correctgame)+'</u></h1>' \
           '<a href="/resources">CONTINUE</a>'


@app.route("/resources")
def resources():
    return render_template("resources.html")


if __name__ == "__main__":
    app.run(debug=True)
