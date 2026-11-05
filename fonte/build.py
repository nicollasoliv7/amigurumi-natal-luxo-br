import re, html, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from svgs import S
BASE='imagens/'
TARJ='https://hand.nexoradigital.store/tarjetas/'
CHECKOUT='#SEU-LINK-DE-CHECKOUT'
NAME={'hero-vitrina-navidena':'hero-vitrine-natal','avatar-1':'avatar-1','avatar-2':'avatar-2','avatar-3':'avatar-3','antes-piezas-sueltas':'antes-pecas-soltas','despues-coleccion':'depois-colecao',
'paso-elige':'passo-escolha','paso-teje':'passo-crochete','paso-eleva':'passo-eleve','paso-exhibe':'passo-exiba','tab-pasion':'aba-paixao','tab-regalar':'aba-presentear','tab-vender':'aba-vender',
'col-santa':'colecao-papai-noel','col-renos-duendes':'colecao-renas-duendes','col-munecos-nieve':'colecao-bonecos-neve','col-dulce-navidad':'colecao-doce-natal','col-amigos-invierno':'colecao-amigos-inverno','col-adornos-arbol':'colecao-enfeites-arvore','col-mini-regalos':'colecao-mini-presentes','col-piezas-estrella':'colecao-pecas-estrela',
'mockup-patron-interior':'mockup-receita-por-dentro','mockup-indice-visual':'mockup-indice-visual','mockup-producto-completo':'mockup-produto-completo','bono-codigo-amigurumi':'bonus-codigo-amigurumi','bono-acabado-boutique':'bonus-acabamento-boutique','bono-calculadora':'bonus-calculadora','bono-vende-coleccion':'bonus-venda-sua-colecao','mockup-oferta':'mockup-oferta'}
t=open('template.html',encoding='utf-8').read()
css=open('style.css',encoding='utf-8').read()
js=open('app.js',encoding='utf-8').read()

luces=[('oro','4%','6%','150px','0s','11s'),('rojo','80%','3%','120px','-3s','12s'),('crema','62%','20%','58px','-5s','8s'),('verde','12%','30%','74px','-1s','10s'),('oro','88%','36%','160px','-6s','13s'),('rojo','-6%','52%','130px','-2s','12s'),('crema','56%','46%','38px','-3s','8s'),('oro','34%','50%','46px','-6s','9s'),('crema','70%','90%','44px','-1s','8s'),('oro','8%','88%','60px','-7s','10s')]
puntos=[('18%','24%','16px','-1s','3.2s'),('86%','16%','12px','-2s','2.6s'),('8%','46%','14px','-0.5s','3.6s'),('94%','54%','18px','-1.6s','2.9s'),('30%','38%','10px','-2.4s','3.1s'),('66%','34%','12px','-0.8s','2.4s'),('14%','66%','16px','-1.9s','3.4s'),('84%','70%','12px','-2.8s','2.8s'),('40%','80%','14px','-1.2s','3.3s'),('60%','76%','10px','-0.3s','2.7s')]
L=''.join(f'<i class="am-luz-{c}" style="--x:{x};--y:{y};--t:{s};--retraso:{r};--dura:{d}"></i>' for c,x,y,s,r,d in luces)
L+=''.join(f'<i class="am-luz-punto" style="--x:{x};--y:{y};--t:{s};--retraso:{r};--dura:{d}"></i>' for x,y,s,r,d in puntos)
F='<span class="am-foco"></span>'*34

G={'d01':('modelo-01','Papai Noel com lanterna e arvorezinha'),'d04':('modelo-04','Papai Noel Pascoalzinho sentado na poltrona'),'d05':('modelo-05','Ursinho branco com capuz e jaqueta vermelha'),'d06':('modelo-06','Guirlanda «Feliz Natal» com duendes, Papai Noel e Mamãe Noel'),'d09':('modelo-09','Enfeites natalinos sobre uma mesa de madeira'),'d12':('modelo-12','Urso-polar com cachecol roxo'),'d16':('modelo-16','Três bolas de Natal'),'b04':('modelo-basico-04','Duende com gorro verde'),'b06':('modelo-basico-06','Casinha de gengibre com porta vermelha'),'gs':('galeria-papai-noel','Papai Noel e Mamãe Noel'),'gm':('galeria-mini-presentes','Mini Papai Noel, boneco de neve, presentes e meia'),'ge':('galeria-pecas-estrela','Árvore, casinha de gengibre e rena'),
'c1':('colecao-papai-noel','Coleção Papai Noel e Mamãe Noel'),'c2':('colecao-renas-duendes','Coleção Renas e Duendes'),'c3':('colecao-bonecos-neve','Coleção Bonecos de Neve'),'c4':('colecao-doce-natal','Coleção Doce Natal'),'c5':('colecao-amigos-inverno','Coleção Amigos do Inverno'),'c6':('colecao-enfeites-arvore','Coleção Enfeites para a Árvore'),'c7':('colecao-mini-presentes','Coleção Mini Presentes'),'c8':('colecao-pecas-estrela','Coleção Peças Estrela')}
filas=[(1,'izq',8,'4.5s',['d01','c3','gs','b06','c2','d12','c7','d16']),
(2,'der',8,'5.5s',['d04','c5','b04','c4','gm','d05','c8','d09']),
(3,'izq',8,'5s',['d06','c1','ge','c6','d01','b04','c3','gs']),
(4,'der',9,'6s',['d16','c2','d12','gm','c5','b06','d05','c7','d04'])]
FI=''
for n,d,p,r,items in filas:
    lis=''.join(f'<li class="am-diseno"><div class="am-ph am-ph-1x1"><img src="imagens/{G[k][0]}.webp" alt="{G[k][1]}" width="560" height="560" loading="lazy"></div></li>' for k in items)
    FI+=f'    <div class="am-fila" tabindex="0" role="group" aria-label="Modelos da coleção, fileira {n}"><ul class="am-pista am-pista-{d}" style="--piezas: {p}; --ritmo: {r}">{lis}</ul></div>\n'

cols=[('col-santa','Papai Noel e Mamãe Noel','',('Ideal para presentear','')),('col-renos-duendes','Renas e Duendes','',None),('col-munecos-nieve','Bonecos de Neve','',None),('col-dulce-navidad','Doce Natal','(gengibre, casinhas, bengalas)',None),('col-amigos-invierno','Amigos do Inverno','(pinguins, ursos, bichinhos)',None),('col-adornos-arbol','Enfeites para a Árvore','',None),('col-mini-regalos','Mini Presentes','(detalhes pequenos, chaveiros)',None),('col-piezas-estrella','Peças Estrela','(personagens grandes, centros de mesa)',('Brilha na vitrine',' am-alt'))]
CO=''
for f,h,det,pil in cols:
    p=f'\n        <span class="am-coleccion-pildora{pil[1]}">{pil[0]}</span>' if pil else ''
    dd=f'\n        <span class="am-coleccion-det">{det}</span>' if det else ''
    CO+=f'''    <li class="am-coleccion">
      <div class="am-coleccion-media">
        <div class="am-ph am-ph-1x1"><img src="I/{f}.webp" alt="Coleção {h}" loading="lazy"></div>{p}
      </div>
      <div class="am-coleccion-cuerpo">
        <h3>{h}</h3>{dd}
      </div>
    </li>
'''
tabla=[('Horas pulando entre Pinterest e YouTube','Tudo num índice visual'),('Muitas em inglês ou incompletas','Passo a passo e em português'),('Modelos que não combinam entre si','Uma coleção harmoniosa'),('Cores aleatórias','Paletas natalinas de luxo'),('Não sabe quanto cobrar','Calculadora de Preço Justo'),('Não sabe como mostrar','Guia de fotos e publicação'),('Começa quando lembra','Um calendário até dezembro')]
TA=''.join(f'          <tr><td><span class="am-celda"><i data-svg="28"></i><span>{a}</span></span></td><td><span class="am-celda"><i data-svg="27"></i><span>{b}</span></span></td></tr>\n' for a,b in tabla)
pila=[('Coleção Natalina de Luxo (mais de 800 receitas)','R$261',0),('Guia Método Vitrine de Natal™','R$106',0),('Índice Visual','R$50',0),('Videoaulas de técnica amigurumi','R$150',0),('Baú de Natal','R$106',0),('Código Amigurumi™','R$67',1),('Acabamento Boutique + Paletas','R$161',1),('Calculadora de Preço Justo','R$94',1),('Guia Venda a sua Coleção + Calendário','R$156',1)]
PI=''.join(f'      <div class="am-pila-fila" role="row"><span class="am-pila-nombre" role="cell">{"<span class=\"am-pila-bono\">BÔNUS</span>" if b else ""}{n}</span><span class="am-pila-valor" role="cell">{v}</span></div>\n' for n,v,b in pila)
CH=''
for i in range(1,9):
    CH+=f'''    <li class="am-captura"><div class="am-ph am-ph-9x16 am-ph-chat">
        <span class="am-chat" aria-hidden="true"><span class="am-chat-estado"></span><span class="am-chat-cab"><i></i><b></b></span><span class="am-chat-cuerpo"><span class="am-burbuja am-entra-b"></span><span class="am-burbuja am-entra-b am-corta"></span><span class="am-chat-foto"></span><span class="am-burbuja am-sale-b"></span><span class="am-burbuja am-entra-b am-corta"></span></span></span>
        <span class="am-ph-nombre" aria-hidden="true"><i data-svg="49"></i>depoimento-{i:02d}</span>
        <!-- DEPOIMENTO {i}: troque por <img src="SUA-IMAGEM.webp" alt="Depoimento de cliente ({i} de 8)" loading="lazy"> -->
      </div></li>
'''
faq=[('Serve para mim se eu só quero crochetar para mim ou para presentear?','Sim. A maioria usa para presentear e decorar. Vender é uma opção, não uma obrigação.'),('Como é por dentro?','Uma biblioteca no seu celular com os modelos por coleção, cada receita passo a passo e um calendário da temporada.'),('É um produto físico?','Não. É uma coleção 100% digital: receitas e materiais que você baixa ou consulta no celular ou computador. Não enviamos bonecos.'),('Como recebo o material?','Logo após o pagamento você recebe o seu acesso por e-mail.'),('Preciso saber crochê?','A coleção foi pensada para quem já crocheta. Se quiser revisar técnicas, ela inclui videoaulas de amigurumi.'),('As receitas indicam o nível de dificuldade?','As receitas não são classificadas por nível de dificuldade. Porém, são explicadas de forma clara e organizada para você seguir cada projeto sem complicação.'),('As receitas estão em português?','Sim. Além disso, o Código Amigurumi™ te ajuda com abreviações de diferentes países.'),('Quais materiais eu preciso?','Linha (de preferência de algodão), agulha de crochê, enchimento, olhos de segurança e agulha de tapeçaria. Cada receita indica o que você precisa.'),('Posso acessar pelo celular?','Sim, por qualquer celular, tablet ou computador.'),('O acesso expira?','Não. Você paga uma vez e o acesso é seu.'),('O que acontece com os bônus se eu não comprar agora?','Seus 4 bônus ficam reservados enquanto o contador da oferta estiver correndo. Quando ele termina, a coleção continua disponível, mas sem os bônus.'),('É pagamento único?','Sim, R$55 uma única vez. Sem mensalidades.'),('Vocês garantem que eu vou vender?','Não. Damos os modelos, o acabamento e as ferramentas para você preparar a sua coleção e oferecê-la. O que você conquistar depende de você. Mas uma coisa é certa: você vai chegar preparada.'),('E se não for para mim?','Você tem 7 dias de garantia. Se não for para você, devolvemos o seu dinheiro.')]
FA=''
for i,(q,a) in enumerate(faq,1):
    FA+=f'''      <div class="am-faq-item">
        <h3><button type="button" class="am-faq-q" id="am-faq-q{i}" aria-expanded="false" aria-controls="am-faq-a{i}">{q}<span class="am-faq-mas" aria-hidden="true"><i data-svg="52"></i></span></button></h3>
        <div class="am-faq-a" id="am-faq-a{i}" role="region" aria-labelledby="am-faq-q{i}"><p class="am-faq-a-in">{a}</p></div>
      </div>
'''
for k,v in {'LUCES':L,'FOCOS':F,'FILAS':FI.rstrip('\n'),'COLECCIONES':CO.rstrip('\n'),'TABLA':TA.rstrip('\n'),'PILA':PI.rstrip('\n'),'CHATS':CH.rstrip('\n'),'FAQ':FA.rstrip('\n'),'CHECKOUT':CHECKOUT}.items():
    t=t.replace('{{'+k+'}}',v)
t=t.replace('{{CSS}}',css).replace('{{JS}}',js)
t=re.sub(r'src="I/([\w-]+)\.webp"',lambda mm:'src="imagens/'+NAME[mm.group(1)]+'.webp"',t).replace('src="T/','src="'+TARJ)
t=re.sub(r'(<img (?![^>]*am-pago)[^>]*?)(\s*/?>)',r'\1 onerror="this.hidden=true"\2',t)
t=re.sub(r'<i data-svg="(\d+)"></i>',lambda m:S[int(m.group(1))],t)
assert '{{' not in t, re.findall(r'\{\{\w+\}\}',t)
open(os.path.join(os.path.dirname(__file__),'..','index.html'),'w',encoding='utf-8').write(t)
print(len(t))
