import praw
from settings_secret import *
import timeit
import time
import sys


def roastme(cqf, start_date, end_date):
	start_time = timeit.default_timer()
	reddit = praw.Reddit(client_id=client_id,
	                     client_secret=client_secret,
	                     user_agent=user_agent)

	#print(reddit.read_only)  # Output: True

	#total = 1
	rank = []

	api_time = timeit.default_timer()
	print('begin')
	print(cqf)
	print(start_date)
	print(end_date)

	roast = reddit.subreddit('roastme').hot(limit=100)
	print(timeit.default_timer() - api_time)

	for submission in roast:
		if submission.score >= 1000:
			for_time = timeit.default_timer()
			submission.comments.replace_more(limit=0)
			#top_level_comments = list(submission.comments)
			print('top level comments: {}'.format(len(submission.comments)))
			for comment in submission.comments:
				#if comment
				#body = comment.body
				#if body != '[removed]' and comment.score >= 1000:
				if comment.score >= 1000:
					rank.append([comment.score, comment.body])
					#print('{}: {}'.format(comment.score, body))
					#total += 1

		print(timeit.default_timer() - for_time)
	    #print('{}: {}'.format(index + 1, submission.title))

	rank = sorted(rank)
	rank.reverse()

	datetime = time.strftime("%Y%m%d%H%M%S")

	file = open('{}-{}-{}-{}.txt'.format(filepath, cqf, start_date.replace('/', '-'), end_date.replace('/', '-')), 'w', encoding="utf-8")

	for index, r in enumerate(rank):
		#print('{}: {}'.format(*r[0], *r[1]))
		#print(*r)
		file.write('{}: {}\n'.format(index, r[1]))

	print('Elapsed Time: {} seconds'.format(timeit.default_timer() - start_time))


	 
	#file.write('Hello World')
	 
	file.close() 





if __name__ == "__main__":
    cqf = int(sys.argv[1])
    start_date = sys.argv[2]
    end_date = sys.argv[3]
    roastme(cqf, start_date, end_date)