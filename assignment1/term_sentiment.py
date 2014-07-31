import sys

def hw():
	afinnfile = open('AFINN-111.txt')
	outputfile = open('output.txt')
	scores = {} # initialize an empty dictionary

	for line in afinnfile:
		term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)
	print scores.items()

	new_sentiments_total_score = {}
	new_sentiments_word_count = {}
    for line in outputfile:
    	try:
			text = json.loads(line)['text']
		except KeyError:
			sys.stdout.write("0\n")
			continue
		words = text.split(" ");
		for i in range(0, len(words)):
			for j in range(i, len(words)):
				if words[i] in scores and words[j] not in scores:
					if words[j] not in new_sentiments:
						new_sentiments_total_score[words[j]] = scores[words[i]]
						new_sentiments_word_count[words[j]] = 1
					else:
						new_sentiments_total_score[words[j]] += scores[words[i]]
						new_sentiments_word_count += 1
	for new_sentiment in new_sentiments_total_score:
		avg_score = new_sentiments_total_score[new_sentiment] / new_sentiments_word_count[new_sentiment]
		sys.stdout.write(new_sentiment + " " + avg_score + "\n")

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
