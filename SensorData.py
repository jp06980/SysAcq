import time, requests, csv
def sendMSG(msg):
		apiKey = '93fd03331cb480fa60ca493e50'
		msg = requests.post('https://api.groupme.com/v3/bots/post', params={'bot_id': apiKey, 'text':msg})
try:
	filename = time.strftime('sensordata_%Y_%m_%d_%H.csv')
	r = requests.get('https://russellthackston.me/etl/' + filename, headers={'Authorization' : '2134cc80b3633199b90766812a857bb1'})
	reader = r.text.split('\n')
	lowCharge = [reader.pop(0)]
	for line in reader:
		x = line.split(',')
		if len(x) == 4 and float(x[3]) < 5: 
			print(x)
			lowCharge.append(line)	
	filetoSend = '\n'.join(lowCharge)
	files = {'file': (filename, filetoSend)}
	post = requests.post('https://russellthackston.me/etl-drop/index.php', headers = {'Authorization' : '2134cc80b3633199b90766812a857bb1'}, files = files)
	sendMSG(post.text)
except Exception as e:
	sendMSG(e)