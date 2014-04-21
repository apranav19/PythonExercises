# The anagram class
class Anagram(object):
	def __init__(self, word):
		self.word = word.lower()
		self.dict = {}

	# Alphabetically sort all the letters in a word
	def normalize(self, word):
		listw = list(word)
		listw.sort()
		return ''.join(listw)

	def preq_checks(self, word, req_length):
		return (self.word != word and len(word) == req_length)

	def norm_check(self, norm_word, raw_word):
		return (norm_word == self.normalize(raw_word))

	# Check if any of the words in the list are anagrams of the current instance
	def match(self, wordlist):
		normalized_word = self.normalize(self.word)
		req_length = len(normalized_word)
		wordlist = map(str.lower, wordlist)
		result_list = filter(self.norm_check, filter(preq_checks, wordlist))
		for word in wordlist:
			# Check word length
			if len(word) != req_length:
				continue
			# Check for same words
			if self.word == word:
				continue
			# Check for normalized forms
			if normalized_word == self.normalize(word.lower()):
				result_list.append(word)
		return result_list
