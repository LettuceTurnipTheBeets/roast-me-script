# roast-me-script
This script uses PRAW (https://praw.readthedocs.io/en/latest/#) and the Reddit API to scrape the contents of r/roastme with the goal of finding the best roast comments.  It will then output the best comments to an html file for analysis.  The best comments are listed with a picture and description of the initial post.  To run the script you will need to enter in some variables:

Range:  Date Range of the posts to analyze.  This is inclusive.
Comment Quality factor:  Number of upvotes the post and the comment has to have.

## Example Usage
	python start.py --range 12/1/2018-12/8/2018 --cqf 1000