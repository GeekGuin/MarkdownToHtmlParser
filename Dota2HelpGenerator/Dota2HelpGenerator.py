import os

def getFileNames():
	namesList = []
	indir = './../graphics/Dota_2_Assets/'
	for root, dirs, filenames in os.walk(indir):
		for f in filenames:
			namesList.append(f[0:len(f)-4])
	return namesList
	
def writeNames(t, f):
	i = 0
	f.write('### ')
	for name in t:
		formattedName = ':' + name + ':'
		string = '`' + formattedName + '` ' + formattedName + ', '
		i += 1
		if i == 4:
			i = 0
			string += '\n ### '
		f.write(string)


fout = open('../Dota2.html', 'w')

initialHtml = '<!doctype html>\n' + '<html>\n' + '<head>\n' + '\t<meta charset="utf-8"/>\n' + '</head>\n' + '<body>\n'
endHtml = '\t<script src="scripts/markedCustom.js"></script>\n' + '\t<script type="text/javascript" src="scripts/doParse.js"></script>' + '</body>\n' + '</html>\n'
fout.write(initialHtml)
fout.write('<h1> Available Dota 2 emojis: </h1>')

namesList = getFileNames()
fout.write('\t<textarea id="input" oninput="update()" style="display:none;">')

writeNames(namesList, fout)
	
#~ strIn = '## `:charm_slark:` :charm_slark:, `:riki:` :riki:\n'
#~ fout.write(strIn)
#~ fout.write(':chen:')
fout.write('\t</textarea>')
fout.write('<div id="content"></div>')
fout.write(endHtml)
fout.close()
