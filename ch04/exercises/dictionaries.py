article = ("Alcohol abuse is the second most common form of substance abuse in the United States, after tobacco addiction. Some people are more severely affected than others. When an individual's drinking causes distress or harm, that's called an alcohol use disorder. An estimated 10% of adult men and 5% of adult women have an alcohol use disorder.")

subs = {
  "substance abuse": "poop",
  "tobacco addiction":"pooping",
  "affected":"pooped on",
  "disorder":"dispooper",
}

for key, value in subs.items():
  article = article.replace(key, value)
  print(article)