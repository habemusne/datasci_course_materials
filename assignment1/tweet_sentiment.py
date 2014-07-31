import sys
import json

def hw():
	afinnfile = open('AFINN-111.txt')
	outputfile = open('output.txt')
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
	print scores.items() # Print every (term, score) pair in the dictionary

	for line in outputfile:
		try:
			text = json.loads(line)['text']
		except KeyError:
			sys.stdout.write("0\n")
			continue
		tweet_score = 0
		words = text.split(" ");
		for word in words:
			try:
				word_score = scores[word]
			except KeyError:
				continue
			tweet_score += scores[word]
		sys.stdout.write(str(tweet_score) + "\n")

def lines(fp):
	print str(len(fp.readlines()))

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	hw()
	lines(sent_file)
	lines(tweet_file)

if __name__ == '__main__':
	main()
