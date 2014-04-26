import sublime, sublime_plugin, random, string, os

class WpkeygenCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		ListReplacements = []

		RegionsResult = self.view.find_all(r"(define\(')([A-Z_]+)(_)(KEY|SALT)(',)(.*?)(\);)", sublime.IGNORECASE, "\\1\\2\\3\\4\\5'THISBITSHOLDBEREPLACED'\\7", ListReplacements)

		for i, thisregion in reversed(list(enumerate(RegionsResult))):
			newsalt = ListReplacements[i].replace('THISBITSHOLDBEREPLACED', self.rsv())
			self.view.replace(edit, thisregion, newsalt)

	def rsv(self):
		length = 64
		chars = string.ascii_letters + string.digits + '!@#$%^&*()`|_}-&><#{=.][;:+/'
		random.seed = (os.urandom(1024))
		return ''.join(random.choice(chars) for i in range(length))




