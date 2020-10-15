from flask import Flask, render_template, request
from redis import Redis

application = Flask(__name__)
redis = Redis(host='redis', port=6379)
redis.set('yes', 0)
redis.set('no', 0)
redis.set('no_one', 0)

@application.route("/")
def hello():
    return render_template('form.html')
    

@application.route("/vote", methods=['GET', 'POST'])
def vote():
    if request.method =='POST':
        vt = request.form.get('vote')
        redis.incr(vt)

    yes_votes = redis.get('yes')
    no_votes = redis.get('no')
    correct_votes = redis.get('no_one')
    return render_template('results.html', yes_votes=yes_votes, no_votes=no_votes, correct_votes=correct_votes)

        




if __name__ == "__main__":
    application.run(host='0.0.0.0')
