favorite_languages = {'jen': 'python',
                      'boyang': 'python', 'lisa': 'C#', 'tom': 'Java'}
friends = ['lisa', 'tom']
# print("lisa's favorite language is " +
#      favorite_languages['lisa'].title() + " !")
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " +
              favorite_languages[name].title() + "!")
for language in favorite_languages.values():
    print(language.title())

for name in sorted(favorite_languages.keys()):
    print(name.title() + " , thank you for taking the poll.")

for language in set(favorite_languages.values()):
    print(language.title())
