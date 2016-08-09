'''Our friendly friend Pete is really a nice person, but he tends to be rather... Inappropriate.

And possibly loud, if given enough ethanol and free rein, so we ask you to write a function that should take its not always "clean" speech and 
cover as much as possible of it, in order not to offend some more sensible spirits.

For example, given an input like

What the hell am I doing here? And where is my wallet? PETE SMASH!
You are expected to turn it into something like:

W**t t*e h**l am i d***g h**e? A*d w***e is my w****t? P**e s***h!
In case you didn't figure out the rules yet: any words longer than 2 characters need to have its "inside" 
(meaning every character which is not the first or the last) changed into *;
 as we do not want Pete to scream too much, 
 every uppercase letter which is not at the beginning of the string or 
 coming after a punctuation mark among [".","!","?"] needs to be put to lowercase; spaces and other punctuation marks can be ignored.

Conversely, you need to be sure that the start of each sentence has a capitalized word at the beginning. 
Sentences are divided by the aforementioned punctuation marks.

Finally, the function will take an additional parameter consisting of an array/list of allowed words which are not to be replaced.

Extra cookies if you can do it all in some efficient way and/or using our dear regexes ;)

Note: Absolutely not related to a certain codewarrior I know :p
'''

'''Test.describe("Basic tests")
Test.assert_equals(pete_talk("I want to punch someone in the face"),"I w**t to p***h s*****e in t*e f**e")
Test.assert_equals(pete_talk("uh!"),"Uh!")
Test.assert_equals(pete_talk("What the hell am I doing here? And where is my wallet? PETE SMASH!"),"W**t t*e h**l am i d***g h**e? A*d w***e is my w****t? P**e s***h!")
Test.assert_equals(pete_talk("I want to punch someone in the face",["someone","face"]),"I w**t to p***h someone in t*e face")
Test.assert_equals(pete_talk("I want to punch someone in the face",["drink","job","girls"]),"I w**t to p***h s*****e in t*e f**e")'''


def pete_talk(speech,ok):
	val = speech.split(' ')
    str = ''
    for v in val:
        if(v not in ok and len(v) > 2):
            l = len(v) - 2
            str += = str(v[0] + (l * '*') + v[-1])
        else:
            str += str(v)
    return str
    


pete_talk("Basic tests", "Sa")