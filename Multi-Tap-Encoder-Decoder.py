import PySimpleGUI as sg
import re

def decode(phrase):
	phrase = phrase.upper()
	result = ""
	p_dict = get_presses()
	found_comb = []
	for ch in phrase:
		if(ch not in "79"):
			try:
				reg = re.compile(ch + "{1,3}")
				m = re.findall(reg, phrase)
				for key in p_dict:
					if int(m[0]) == key and key not in found_comb:
						result += p_dict[key] * len(m)
						found_comb.append(key)
			except:
				pass
		elif(ch in "79"):
			try:
				reg = re.compile(ch + "{1,4}")
				m = re.findall(reg, phrase)
				for key in p_dict:
					if int(m[0]) == key and key not in found_comb:
						result += p_dict[key] * len(m)
						found_comb.append(key)
			except:
				pass

	print(result)


def encode(phrase):
	phrase = phrase.upper()
	result = ""
	p_dict = get_presses()
	for ch in phrase:
		for chars in p_dict.items():
			try:
				if ch in chars: result += str(chars[0])
			except:
				pass
	print(result)

def get_presses():
    presses = { 1: ' ',
    			2: 'A',
    			22: 'B',
    			222: 'C',
    			3: 'D',
    			33: 'E',
    			333: 'F',
    			4: 'G',
    			44: 'H',
    			444: 'I',
    			5: 'J',
    			55: 'K',
    			555: 'L',
    			6: 'M',
    			66: 'N',
    			666: 'O',
    			7: 'P',
    			77: 'Q',
    			777: 'R',
    			7777: 'S',
    			8: 'T',
    			88: 'U',
    			888: 'V',
    			9: 'W',
    			99: 'X',
    			999: 'Y',
    			9999: 'Z',
    			'*': '*',
    			0: '0',
    			'#': '#' }
    return presses

sg.theme('LightTeal')
layout = [ [sg.Radio('', "Radio1", default=True), sg.Text("Input text to encode: "), sg.InputText()],
		   [sg.Radio('', "Radio1"), sg.Text("Input text to decode: "), sg.InputText()],
		   [sg.Button('Process', size=(10, 1)), sg.Button("Close", size=(10,1))] ]

window = sg.Window("Multi-Tap Encoder/Decoder", layout)
while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == "Close": break
	if event == "Process":
		if(values[0]): encode(values[1])
		if(values[2]): decode(values[3])

window.close()