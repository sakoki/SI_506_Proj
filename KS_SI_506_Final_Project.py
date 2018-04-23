# SI 506 F17 Final Project 
# Author: Koki Sasagawa 

# Project Requirements:
# 1. Get data from 2 different REST APIs
# 2. Cache all data from REST APIs in one file
# 3. Define at least 2 classes with a constructor, string method, one additional method, and 3 instance variables (minimum). 
# 4. Create at least 1 instance of the class you define
# 5. You MUST use each instance of the classes you create: Invoke the string method and additional method for each. 
# 6. You MUST perform at least 1 sort with a key parameter on data. 
# 7. Define at least 2 functions outside the class definitions that have more than one line inside the function body. (Can be functions to get data from API)
# 8. Your code must create a file that is clearly structured for output. 


# Import Libraries:
import json
import sys
import tweepy
import nltk
from time import strftime

# https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
# usage should be python3 part1.py <username> <num_tweets>

def tweet_access(user_name, num_tweets):
	""" Accept user name(string) and number of tweets(integer) and returns a list of status objects from Twitter. """ 

	# Assign keys & tokens
	my_key = ''
	my_secret = ''
	my_access_token = ''
	my_access_token_secret = ''

	# Authorization using keys and token
	auth = tweepy.OAuthHandler(my_key, my_secret)
	auth.set_access_token(my_access_token, my_access_token_secret)

	# Create interface using authentication 
	api = tweepy.API(auth)

	# Make request 
	tweet_content = api.user_timeline(screen_name = user_name, count = num_tweets)

	return tweet_content


class Tweet: 
	""" Class that represents a single tweet and its contents. """
	def __init__(self, tweet):
		self.text = tweet['text']		
		self.user = tweet['user']['name']
		self.time = tweet['created_at']
		self.favorite = tweet['favorite_count']


	def __str__(self):
		return "{}, {}: {}"

	def 

	def nounCount():


class Song:


def unique_request(user_name):
	return user_name + strftime("%H:%M:%S")

def tweet_stat_analyzer(list_of_tweets):
	""" Accept list of status objects and returns number of original tweets, favorited original tweets, and retweeted original tweets. """
	
	# Initialize dictionary
	tweet_stats = {} 

	# Initialize key-pair values 
	tweet_stats['orig_tweets'] = 0  # The number of original tweets
	tweet_stats['orig_fav'] = 0     # The number of times the original tweets in the analyzed set were favorited
	tweet_stats['orig_retweet'] = 0 # The number of times the original tweet in the analyzed set were retweeted by others

	# TEST: Check Contents (comment out for final code)
	# file1 = open('file1.txt', 'w')
	# file1.write(json.dumps(list_of_tweets[0]._json))
	# file1.close()
	# status = list_of_tweets[8]._json
	# print(status['favorite_count'])
	# print(status['retweet_count'])
	# print(status.keys())

	for x in range(len(list_of_tweets)):
		# JSON formatted tweet 
		status = list_of_tweets[x]._json
		key = status.keys()

		# tweet text
		sentence = status['text']

		if 'retweeted_status' not in key: # Only retweeted tweets have this key
			tweet_stats['orig_tweets'] += 1 
			# Number of times it was FAVORITED
			tweet_stats['orig_fav'] += status['favorite_count'] 
			# Number of times it was RETWEETED
			tweet_stats['orig_retweet'] += status['retweet_count']

	return tweet_stats

def sentence_analyzer(list_of_tweets):
	""" Accept list of status objects and returns top 5 verbs, nouns, and adjectives. """

	# Initialize word_bank which contains all encountered nouns, verbs, adjectives and their counts.
	word_bank_V = {}
	word_bank_N = {}
	word_bank_A = {} 

	for x in range(len(list_of_tweets)):
		# JSON formatted tweet 
		status = list_of_tweets[x]._json

		# sentences contains the actual tweet text
		sentence = status['text']

		# The TweetTokenizer() can account for words with apostrophes, but results in varying word tagging. 
		# tokenizer = nltk.tokenize.TweetTokenizer()
		# token = tokenizer.tokenize(sentence)

		# Tokenize the tweet text 
		token = nltk.word_tokenize(sentence) # this method can not account for words with apostrophes.

		# Tag the tokens before filtering
		before_filter_tag = nltk.pos_tag(token) # result is a list of tuples.

		# Filter out words that do NOT start with alphabetic character. Also ignore 'http', 'https', and 'RT'
		exclude = 'http'
		filter_tag = [x for x in before_filter_tag if (x[0][0].isalpha() and x[0] != 'RT' and x[0].startswith(exclude) == False)]

		for (wd, tg) in filter_tag:
			# If tag is noun add 1 
			if tg.startswith('NN') == True:
				if wd not in word_bank_N:
					word_bank_N[wd] = 0
				word_bank_N[wd] += 1 
			# If tag is verb add 1
			if tg.startswith('VB') == True:
				if wd not in word_bank_V:
					word_bank_V[wd] = 0
				word_bank_V[wd] += 1
			#if tag is adjective add 1 
			if tg.startswith('JJ') == True:
				if wd not in word_bank_A:
					word_bank_A[wd] = 0
				word_bank_A[wd] += 1

	# Get the top 5 most common words
	t5n = sorted(word_bank_N, key = lambda d: word_bank_N[d], reverse = True)[:5]
	t5v = sorted(word_bank_V, key = lambda d: word_bank_V[d], reverse = True)[:5]
	t5a = sorted(word_bank_A, key = lambda d: word_bank_A[d], reverse = True)[:5]

	# Initialize string variables 
	resultV = ''
	resultN = ''
	resultA = ''

	# Format output as string 
	for v in t5v:
		resultV += '{}({})'.format(v, word_bank_V[v]) + ' '
	for n in t5n:
		resultN += '{}({})'.format(n, word_bank_N[n]) + ' '
	for a in t5a:
		resultA += '{}({})'.format(a, word_bank_A[a]) + ' '

	results = [resultV, resultN, resultA]

	return results

def main(username = sys.argv[1], num_tweets = sys.argv[2]):
	
	# Load content of tweets into tweet 
	tweets = tweet_access(username, num_tweets)
	# Analyze the tweet, return tweet stats 
	stats = tweet_stat_analyzer(tweets)
	# Analyze the tweet, return most common words
	common_words = sentence_analyzer(tweets)

	# Print Results
	print('USER: {}'.format(username))
	print('TWEETS ANALYZED: {}'.format(num_tweets))
	print('VERBS: {}'.format(common_words[0]))
	print('NOUNS: {}'.format(common_words[1]))
	print('ADJECTIVES: {}'.format(common_words[2]))
	print('ORIGINAL TWEETS: {}'.format(stats['orig_tweets']))
	print('TIMES FAVORITED (ORIGINAL TWEETS ONLY): {}'.format(stats['orig_fav']))
	print('TIMES RETWEETED (ORIGINAL TWEETS ONLY): {}'.format(stats['orig_retweet']))

# Invoke Function
main()

































# import webbrowser
# from requests_oauthlib import OAuth2Session
# from requests_oauthlib.compliance_fixes import facebook_compliance_fix


# ########## FACEBOOK API ##########
# APP_ID     = '298348213988097'
# APP_SECRET = '7085bf7d3d0a5d2a3435340b5728cdf2'

# # Global facebook_session variable, needed for handling FB access below
# facebook_session = False

# # Function to make a request to Facebook provided.
# # Reference: https://requests-oauthlib.readthedocs.io/en/latest/examples/facebook.html
# def makeFacebookRequest(baseURL, params = {}):
#     global facebook_session
#     if not facebook_session:
#         # OAuth endpoints given in the Facebook API documentation
#         authorization_base_url = 'https://www.facebook.com/dialog/oauth'
#         token_url = 'https://graph.facebook.com/oauth/access_token'
#         redirect_uri = 'https://www.programsinformationpeople.org/runestone/oauth'

#         scope = ['user_posts','pages_messaging','user_managed_groups','user_status','user_likes']
#         facebook = OAuth2Session(APP_ID, redirect_uri=redirect_uri, scope=scope)
#         facebook_session = facebook_compliance_fix(facebook)

#         authorization_url, state = facebook_session.authorization_url(authorization_base_url)
#         print('Opening browser to {} for authorization'.format(authorization_url))
#         webbrowser.open(authorization_url)

#         redirect_response = input('Paste the full redirect URL here: ')
#         facebook_session.fetch_token(token_url, client_secret=APP_SECRET, authorization_response=redirect_response.strip())

#         return facebook_session.get(baseURL, params=params)


# class Post():
#     '''object representing status update'''

#     def __init__(self, post_dict={}):
#         if 'comments' in post_dict:
#             self.comments = post_dict['comments']['data']
#         else:
#             self.comments = []

#         if 'likes' in post_dict:
#             self.likes = post_dict['likes']['data']
#         else:
#             self.likes = []

#         if 'message' in post_dict:
#             self.message = post_dict['message']
#         else:
#             self.message = ''


# baseurl = 'https://graph.facebook.com/me/feed' # Replace "me" with the group id if you are using a public group instead

# # OK, now: What function do you need to invoke with what input to make this happen? HINT: Use the Facebook Graph API Explorer (https://developers.facebook.com/tools/explorer/) to test the parameters of your request. The response should return data for the message, likes, and comments of each post.

# # Write code for PROBLEM 4 here:
# #me/feed/?fields=message,likes,comments&limit=50
# params_diction = {}
# params_diction['fields'] = 'message, likes, comments'
# params_diction['limit'] = 100
# #params_diction = {'fields': ['message','likes','comments'], 'limit': 50}
# hundred_result = makeFacebookRequest(baseurl, params = params_diction)
# hundred_posts_data = json.loads(hundred_result.text)

# post_insts = [Post(x) for x in hundred_posts_data['data']]

########## TWITTER API ##########

def sentence_analyzer(list_of_tweets):
	""" Accept list of status objects and returns top 5 verbs, nouns, and adjectives. """

	# Initialize word_bank which contains all encountered nouns, verbs, adjectives and their counts.
	word_bank_V = {}
	word_bank_N = {}
	word_bank_A = {} 

	for x in range(len(list_of_tweets)):
		# JSON formatted tweet 
		status = list_of_tweets[x]._json

		# sentences contains the actual tweet text
		sentence = status['text']

		# The TweetTokenizer() can account for words with apostrophes, but results in varying word tagging. 
		# tokenizer = nltk.tokenize.TweetTokenizer()
		# token = tokenizer.tokenize(sentence)

		# Tokenize the tweet text 
		token = nltk.word_tokenize(sentence) # this method can not account for words with apostrophes.

		# Tag the tokens before filtering
		before_filter_tag = nltk.pos_tag(token) # result is a list of tuples.

		# Filter out words that do NOT start with alphabetic character. Also ignore 'http', 'https', and 'RT'
		exclude = 'http'
		filter_tag = [x for x in before_filter_tag if (x[0][0].isalpha() and x[0] != 'RT' and x[0].startswith(exclude) == False)]

		for (wd, tg) in filter_tag:
			# If tag is noun add 1 
			if tg.startswith('NN') == True:
				if wd not in word_bank_N:
					word_bank_N[wd] = 0
				word_bank_N[wd] += 1 
			# If tag is verb add 1
			if tg.startswith('VB') == True:
				if wd not in word_bank_V:
					word_bank_V[wd] = 0
				word_bank_V[wd] += 1
			#if tag is adjective add 1 
			if tg.startswith('JJ') == True:
				if wd not in word_bank_A:
					word_bank_A[wd] = 0
				word_bank_A[wd] += 1

	# Get the top 5 most common words
	t5n = sorted(word_bank_N, key = lambda d: word_bank_N[d], reverse = True)[:5]
	t5v = sorted(word_bank_V, key = lambda d: word_bank_V[d], reverse = True)[:5]
	t5a = sorted(word_bank_A, key = lambda d: word_bank_A[d], reverse = True)[:5]

	# Initialize string variables 
	resultV = ''
	resultN = ''
	resultA = ''

	# Format output as string 
	for v in t5v:
		resultV += '{}({})'.format(v, word_bank_V[v]) + ' '
	for n in t5n:
		resultN += '{}({})'.format(n, word_bank_N[n]) + ' '
	for a in t5a:
		resultA += '{}({})'.format(a, word_bank_A[a]) + ' '

	results = [resultV, resultN, resultA]

	return results


with open('emo_scores.csv', 'w') as outfile1:
    outfile1.write("emo_scores, comment_counts, like_counts\n")
    for post in post_insts:
        outfile1.write("{}, {}, {}\n".format(post.emo_score(), len(post.comments), len(post.likes)))







