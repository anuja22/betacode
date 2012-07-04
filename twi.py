#hello!!

from string import Template
from flask import Flask, render_template, request	#not requests
import tweepy
import datetime

app = Flask(__name__)

@app.route('/')
def func1():
    return render_template('http://gradetweeple.pagekite.me/index.html')

@app.route("/grade", methods=["POST"])
def func2():
	un = request.form["uname"]
	#Get the User object for twitter...
	user = tweepy.api.get_user(un)
	x=user.screen_name
	y=user.followers_count
	z=user.statuses_count
	w=user.friends_count
	twit=user.created_at
	u=user.profile_image_url
	s=str(getgrade(y,w,z,twit))
	return render_template("http://gradetweeple.pagekite.me/twi2.html",u=u,x=x,twit=twit,y=y,z=z,w=w,s=s)
'''
def getretweets(user):
	consumerkey= "eWzjVEsOkQwIC6ZF8jf05A"
	consumersecret= "8EchxD8Ov0KW4qAvZlNlURq24uPO0fjEOxC4shy5ZI"
	accesstoken="82608614-dgjLGXx4PBwg8P8EGM4YoTeLXXxNF7b8f56sT63k"
	accesstokensecret="GuorkgDOPfu7IDgmDlTceMCDi7hBPYmNRoV2GeKE"

	auth = tweepy.OAuthHandler(consumerkey,consumersecret)
	auth.set_access_token(accesstoken, accesstokensecret)
	api = tweepy.API(auth)

	for status in tweepy.Cursor(api.user_timeline, id=user).items(5): 
#		print "\nlast 5 tweets! - " + status.text
		retweet=status.text
		give_eghtml(retweet)

def give_eghtml(retweet):
	return render_template("eg.html",retweet=retweet)


def posttweet(user):
	consumerkey= "eWzjVEsOkQwIC6ZF8jf05A"
	consumersecret= "8EchxD8Ov0KW4qAvZlNlURq24uPO0fjEOxC4shy5ZI"
	accesstoken="82608614-dgjLGXx4PBwg8P8EGM4YoTeLXXxNF7b8f56sT63k"
	accesstokensecret="GuorkgDOPfu7IDgmDlTceMCDi7hBPYmNRoV2GeKE"

	auth = tweepy.OAuthHandler(consumerkey,consumersecret)
	auth.set_access_token(accesstoken, accesstokensecret)
	api = tweepy.API(auth)
							     
	api.update_status('Tweeted via Tweepy!aya! =)')	#user?????
	'''
def getdays(twit):
	now=datetime.datetime.now()
	duration = now-twit
	return duration.days

def getgrade(a,c,b,twit):
	fer=float(a) #followers
	fing=float(c) #following
	no_of_tweets=float(b)
	no_of_days=float(getdays(twit))

	r1=fer/fing
	r2=no_of_tweets/no_of_days

	#calculate r1
	if r1 == 0:
		m1=0
	else:
		for i in range(1,11):
			y=i-1
			if r1<=i and r1>y:
				m1=i*5
			else:
				continue

	#calculate r2
	if r2== 0:
		m2=0
	else:
		for i in range(1,11):
			y=i-1
			if r2<=i and r2>y:
				m2=i*5
			else:
				continue

	grade=m1+m2
	return grade

#posttweet('anuja_22')

#getretweets('anuja_22')

if __name__ == '__main__': #imp to make it run!!!
    app.run(debug=True)
