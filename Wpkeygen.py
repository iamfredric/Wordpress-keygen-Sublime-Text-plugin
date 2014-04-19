import sublime, sublime_plugin, hashlib, random

class WpkeygenCommand(sublime_plugin.TextCommand):

    def run(self, edit):
    	ListReplacements = []
    	SecondRound = []
    	Hasher = hashlib.sha1()
      	RegionsResult = self.view.find_all(r"(define\(')([A-Z_]+)(_)(KEY|SALT)(',)(.*?)(\);)", sublime.IGNORECASE, "\\1\\2\\3\\4\\5'KUKEN'\\7", ListReplacements)
      	for i, thisregion in reversed(list(enumerate(RegionsResult))):
			hashstring = "%032x" %  random.getrandbits(128)
			Hasher.update(hashstring)
			newsalt = ListReplacements[i].replace('KUKEN', Hasher.hexdigest())
			self.view.replace(edit, thisregion, newsalt)
