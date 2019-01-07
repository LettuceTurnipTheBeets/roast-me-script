import praw
from settings_secret import *
import timeit
import time
import sys


def roastme(cqf):
	start_time = timeit.default_timer()
	reddit = praw.Reddit(client_id=client_id,
	                     client_secret=client_secret,
	                     user_agent=user_agent)
	rank = []

	for submission in reddit.subreddit('roastme').hot(limit=1000):
		if submission.score >= cqf:
			submission.comments.replace_more(limit=0)
			for comment in submission.comments:
				if comment.score >= cqf:
					rank.append([comment.score, comment.body])

	rank = sorted(rank)
	rank.reverse()

	datetime = time.strftime("%Y%m%d%H%M%S")

	file = open('{}-{}-{}.txt'.format(filepath, cqf, datetime), 'w', encoding="utf-8")

	for index, r in enumerate(rank):
		file.write('{}: {}\n'.format(index, r[1]))

	print('Elapsed Time: {} seconds'.format(timeit.default_timer() - start_time))
	file.close() 


if __name__ == "__main__":
    cqf = int(sys.argv[1])
    roastme(cqf)