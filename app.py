from flask import Flask, render_template, request



app = Flask(__name__)

class ChatState:
    def __init__(self):
        self.step = 0
        self.user_name = ""
        self.user_email = ""
        self.cont = ""
        self.education = ""
        self.agree = ""
        self.interest = ""
        self.course = ""
        self.internship_option = ""
        self.int_interest = ""
        self.course_int = ""
        self.non_tech = None

state = ChatState()

@app.route("/", methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        if state.step == 0:
            state.user_name = request.form["user_name"]
            state.step = 1
        elif state.step == 1:
            state.user_email = request.form["user_email"]
            state.step = 2
        elif state.step == 2:
            state.cont = request.form["cont"]
            state.step = 3
        elif state.step == 3:
            state.education = request.form["education"]
            state.step = 4
          
        elif state.step == 4:
            state.agree = request.form["agree"]
            if state.education == "Tech" or state.agree.lower() == "yes":
                state.step = 5
            elif state.education == "Non-tech" or state.agree.lower() == "yes":
                state.non_tech = 5
            else:
                state.step = 3
        
        elif state.step == 5:
            state.course = request.form["course"]
            state.step = 6
        elif state.step == 6:
            state.internship_option = request.form["internship_option"]
            state.step = 7
            
        elif state.step == 7:
            if "interest" in request.form:
                state.int_interest = request.form["interest"]
            state.step = 8
            
    elif request.method == "GET" and state.step > 0:
        state.step -= 1  # Navigate back one step

    return render_template("index.html", state=state)



 
