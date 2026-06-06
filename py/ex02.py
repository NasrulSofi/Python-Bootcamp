Text = """Python is a powerful programming language. It's easy to learn
and versatile!
You can use Python for web development, data science, and
automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""

Wordlist = Text.split() #splitting the paragraph into single words.

Wordcount = len(Wordlist) #total words in a paragraph

Charcount = Text.strip() #removing spaces from paragraph

Chartotal = len(Charcount) #counting total characters

Sentences = Text.count(".") + Text.count("!") + Text.count(",") #using the punctuation marks as sentences


print(f"Total Words:{Wordcount}")
print(f"Total Characters:{Chartotal}")
print(f"Total Sentences:{Sentences}")