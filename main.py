from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    mismatch=""
    bad_password=""
    bad_username=""
    bad_email=""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']
        mismatch=""
        bad_password=""
        bad_username=""
        error_bool=False
        if verify != password:
            mismatch="These passwords do not match."
            error_bool=True
        if len(password) <3 or len(password) >20:
            bad_password="Please enter a password that is between 3 and 20 characters long"
            error_bool=True
        if len(username) <3 or len(username) >20:
            bad_username="Please enter a username that is between 3 and 20 characters long"    
            error_bool=True
        if is_email(email) == False and len(email) > 0:
            bad_email="That email didn't turn out to be structured correctly.  Please try again."
            error_bool=True
        if error_bool == False:  
            return redirect('/welcome?username='+username)
    return render_template("signup.html", mismatch=mismatch, bad_password=bad_password, bad_username=bad_username, bad_email=bad_email)

def is_email(email):
    find_at = email.find('@')
    has_at = find_at >= 1
    if not has_at:
        return False
    find_dot = email.find('.')
    correct_dot = find_dot > find_at
    if not correct_dot:
        return False
    else:
        return True

@app.route("/welcome")
def welcome_in():
    username = request.args.get("username")  
    return render_template("welcome.html", username=username)

@app.route("/")
def index():
    return redirect("/signup")

if __name__ == "__main__":
    app.run()