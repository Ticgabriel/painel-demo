from pathlib import Path
import json, datetime
out=Path(__file__).parent
(out/'src').mkdir(exist_ok=True)
today=datetime.date(2026,10,23)
def day(n):return (today+datetime.timedelta(days=n)).isoformat()
fields=['component','fleet','seller','client','site','os','type','status','situation','piecesNote','note','nextAction','owner','actionDue','reviewDate','forecast','confirmed','requisition','nf','order','parts','services','arrival','notification','opened','budgetForecast','quoted','approved','shipped','internal','invoice','invoiceMonth']
phases=['Notificação','Orçamento','Negociação','Aprovado','Pronto','Enviado'];situations=['Em andamento','Aguardando peças','Aguardando terceiro','Aguardando envio do orçamento','Aguardando negociação/aprovação','Aguardando programação/recurso','Aguardando teste/liberação','Aguardando coleta']
actions=['Confirmar programação','Acompanhar pedido de peças','Acompanhar serviço externo','Enviar orçamento','Obter Pedido do Cliente','Programar serviço','Realizar teste','Programar coleta']
rows=[]
for i in range(48):
 n=[1,2,4][i%3];nums=[str(800000000+i*100+j+1) for j in range(n)];r={k:'' for k in fields};r.update(id=f'demo-row-{i+1:03}',component=['Motor','Transmissão','Cilindro hidráulico','Comando final','Conversor','Bomba hidráulica'][i%6]+f' · DEMO {i+1:02}',fleet=['320','950','D8','777'][i%4],seller=f'Comercial Exemplo {i%3+1}',client=f'Cliente Demonstração {i%12+1:03}',site=['Unidade Norte','Unidade Sul',''][i%3],os='/'.join([nums[0]]+[x[-2:] for x in nums[1:]]),type='Rentável' if i%2 else 'Garantia',history=[],sap=[],archived=i>=46,primary={})
 children=[]
 for j,number in enumerate(nums):
  x=i+j;orders=[dict(id=f'demo-order-{i}-{j}-1',pedido=str(9900000000+i*10+j),due=day((x%20)-3),note='Prazo sintético de fornecimento.')] if x%3 else []
  if x%5==0:orders.append(dict(id=f'demo-order-{i}-{j}-2',pedido=str(9800000000+i*10+j),due=day(15+x%10),note='Segundo pedido fictício; verificar previsão.'))
  values={k:'' for k in fields if k not in ['component','fleet','seller','client','site','os','type','piecesNote','order']};values.update(status=phases[x%6],situation=situations[x%8],note=('Contato comercial fictício; aguardando retorno do cliente.' if x%4 else 'Cliente solicitou revisão de escopo.\nConferir montagem e previsão antes de responder.'),nextAction=actions[x%8] if x%7 else '',owner=['Planejador','Comercial','Oficina','Terceiro'][x%4],actionDue=day((x%15)-6) if x%7 else '',reviewDate=day(x%10-2) if x%4 else '',forecast=day(7+x%35),confirmed=day(-(x%12)-1) if x%4 else '',requisition=str(97000000+x),parts=5500+i*275+j*95,services=2000+i*135+j*40,arrival=day(-45+i%12),notification=day(-43+i%12),opened=day(-40+i%12),quoted=day(-20+i%8) if x%6>1 else '',approved=day(-10+i%6) if x%6>2 else '',invoice='Sim' if x%3 else 'Não',invoiceMonth='2026-10',internal='Registro criado artificialmente para testes de uso. Nenhuma OS real está representada.')
  if i==3 and j==1:values['nextAction']='Solicitar avaliação técnica detalhada do componente e confirmar a disponibilidade de recursos da oficina'
  quarantine=day(-51 if i==45 else -3) if i in [43,44,45] and j==0 else ''
  if quarantine:values['status']='Reprovado'
  children.append(dict(number=number,values=values,orders=orders,quarantineAt=quarantine,history=[dict(at=day(-2)+'T12:00:00Z',text='Dados fictícios gerados para avaliação.')]))
 r['children']=children;r.update(children[0]['values']);r['history']=[dict(at=day(-2)+'T12:00:00Z',text='Atendimento inteiramente fictício.')];r['sap']=[dict(os=nums[0],client=r['client'],model=r['fleet'],serial=f'DEMO-{i:04}',service=r['component'],parts=children[0]['values']['parts'],stage=children[0]['values']['status'],origin=r['type'],dates={'Data PR':children[0]['values']['forecast']})];rows.append(r)
(out/'src/seed.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));(out/'src/multi.json').write_text(json.dumps(rows[12:30],ensure_ascii=False,indent=2))
