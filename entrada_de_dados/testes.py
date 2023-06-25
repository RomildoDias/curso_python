prompt = 'fale algo e eu repito pra vocâ: '
prompt += '\nPara sair digite "sair": '

active = True

while active:
    message= input(prompt)
    if message == "sair" :
     active = False
     print(message)