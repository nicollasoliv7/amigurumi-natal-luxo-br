"""Gera os PDFs de entregáveis do app (app/pdfs/) a partir de HTML, usando o Chrome.
Uso:  python3 fonte/pdfs/gerar_pdfs.py
Requer: pip install playwright  (e um Chrome/Chromium instalado)
"""
import asyncio, os, html, pathlib
from playwright.async_api import async_playwright

RAIZ = pathlib.Path(__file__).resolve().parents[2]
TMPI = pathlib.Path('/tmp/pdf-imagens'); TMPI.mkdir(exist_ok=True)
def _prep():
    from PIL import Image
    for f in (RAIZ / 'imagens').glob('*.webp'):
        im = Image.open(f).convert('RGB'); im.thumbnail((900, 900))
        im.save(TMPI / f.name, 'JPEG', quality=78, optimize=True, progressive=True)
_prep()
IMG = TMPI.as_uri() + '/'
FON = (RAIZ / 'app' / 'fontes').as_uri() + '/'
OUT = RAIZ / 'app' / 'pdfs'
OUT.mkdir(parents=True, exist_ok=True); (OUT / 'extras').mkdir(exist_ok=True)
E = html.escape

CSS = f"""
@font-face{{font-family:F;src:url({FON}Fraunces_600SemiBold.woff2);font-weight:600}}
@font-face{{font-family:F;src:url({FON}Fraunces_800ExtraBold.woff2);font-weight:800}}
@font-face{{font-family:F;src:url({FON}Fraunces_700Bold_Italic.woff2);font-weight:700;font-style:italic}}
@font-face{{font-family:N;src:url({FON}NunitoSans_400Regular.woff2);font-weight:400}}
@font-face{{font-family:N;src:url({FON}NunitoSans_600SemiBold.woff2);font-weight:600}}
@font-face{{font-family:N;src:url({FON}NunitoSans_700Bold.woff2);font-weight:700}}
@font-face{{font-family:N;src:url({FON}NunitoSans_800ExtraBold.woff2);font-weight:800}}
@page{{size:A4;margin:0}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:N,sans-serif;color:#2b2422;font-size:11.5pt;line-height:1.55;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
h1,h2,h3{{font-family:F,serif;margin:0;line-height:1.15}}
em{{font-family:F,serif;font-style:italic;font-weight:700;color:#7a1f2b}}
p{{margin:0 0 8px}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;background:#fbf7f0;padding:20mm 18mm 22mm}}
.pg:last-child{{page-break-after:auto}}
.capa{{padding:0;background:linear-gradient(180deg,#1f3d2e,#122419);color:#fbf7f0;display:flex;flex-direction:column}}
.capa-img{{height:150mm;position:relative}}
.capa-img img{{width:100%;height:100%;object-fit:cover;display:block}}
.capa-img::after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 55%,#1f3d2e)}}
.capa-txt{{padding:8mm 18mm 0;flex:1}}
.capa .tag{{display:inline-block;font-weight:800;font-size:9pt;letter-spacing:.2em;color:#7a1f2b;background:linear-gradient(180deg,#f8e9bf,#dcbb73);padding:5px 14px;border-radius:99px;margin-bottom:6mm}}
.capa h1{{font-size:34pt;color:#fffaf1;font-weight:800}}
.capa h1 em{{color:#f3dca4}}
.capa .sub{{font-size:13pt;color:#fbf7f0cc;margin-top:5mm;max-width:150mm}}
.capa .rod{{padding:0 18mm 14mm;font-size:9pt;color:#d9c39a;letter-spacing:.12em;font-weight:700}}
.cab{{display:flex;justify-content:space-between;font-size:8pt;letter-spacing:.16em;font-weight:800;color:#a27d3b;border-bottom:1px solid #e9dcc3;padding-bottom:4mm;margin-bottom:8mm}}
.num{{position:absolute;bottom:10mm;left:0;right:0;text-align:center;font-size:8.5pt;color:#928a80}}
.ceja{{font-size:8.5pt;font-weight:800;letter-spacing:.18em;color:#7a1f2b;text-transform:uppercase;margin-bottom:3mm}}
h2{{font-size:22pt;font-weight:800;margin-bottom:5mm}}
h3{{font-size:13.5pt;font-weight:800;margin-bottom:2mm}}
.lead{{font-size:12pt;color:#5e574f;margin-bottom:7mm}}
.card{{background:#fff;border:1px solid #ece3d6;border-radius:4mm;padding:4mm 5mm;margin-bottom:3mm;break-inside:avoid}}
.ouro{{border:1.5px solid #c9a45c}}
table{{width:100%;border-collapse:collapse;font-size:10pt}}
th{{background:#7a1f2b;color:#fff;text-align:left;padding:2.6mm 3mm;font-size:8.5pt;letter-spacing:.1em;text-transform:uppercase}}
td{{padding:2.4mm 3mm;border-bottom:1px solid #ece3d6;vertical-align:top;background:#fff}}
td code{{font-family:N;font-weight:800;color:#7a1f2b;background:#f6f2ec;padding:1px 6px;border-radius:5px;white-space:nowrap}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:4mm}}
.grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:3.5mm}}
.passo{{display:grid;grid-template-columns:30mm 1fr;gap:6mm;align-items:center}}
.passo img{{width:30mm;height:30mm;border-radius:50%;object-fit:cover;border:2px solid #d9c39a}}
.badge{{display:inline-block;font-family:F;font-weight:800;color:#7a1f2b;font-size:11pt}}
.check{{display:flex;gap:3mm;align-items:flex-start;padding:2mm 0;border-bottom:1px dashed #e4d8c2}}
.check:last-child{{border:0}}
.box{{width:5mm;height:5mm;border:1.6px solid #b8914a;border-radius:1.4mm;flex-shrink:0;margin-top:1mm}}
.cores{{display:flex;height:16mm;border-radius:3mm;overflow:hidden;margin-bottom:3mm}}
.cores div{{flex:1;display:flex;align-items:flex-end;justify-content:center;font-size:7pt;font-weight:800;padding-bottom:1.5mm}}
.msg{{background:#e7f3df;border-radius:3mm 3mm 3mm 1mm;padding:4mm;white-space:pre-wrap;font-size:10.5pt}}
.linha{{border-bottom:1px solid #cbbfa9;height:9mm}}
.ficha td{{height:10mm}}
.destaque{{background:linear-gradient(180deg,#9a2c3d,#6f1b27);color:#fff;border-radius:4mm;padding:6mm;text-align:center}}
.destaque b{{font-family:F;font-size:20pt;display:block}}
.thumb{{border-radius:3mm;overflow:hidden;border:2px solid #fff;box-shadow:0 2px 6px #0002;aspect-ratio:1/1;position:relative}}
.thumb img{{width:100%;height:100%;object-fit:cover;display:block}}
.thumb span{{position:absolute;left:0;right:0;bottom:0;color:#fff;font-size:8pt;font-weight:800;padding:6mm 2mm 1.5mm;background:linear-gradient(transparent,#000b)}}
.nota{{font-size:9.5pt;color:#6f675e;font-style:italic}}
"""

def doc(titulo_cab, paginas):
    out = []
    for i, p in enumerate(paginas):
        if p.startswith('<!--capa-->'):
            out.append(p)
        else:
            out.append(f'<section class="pg"><div class="cab"><span>AMIGURUMIS NATALINOS DE LUXO</span><span>{E(titulo_cab)}</span></div>{p}<div class="num">{i+1}</div></section>')
    return f'<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(out)}</body></html>'

def capa(img, tag, titulo, sub):
    return f'''<!--capa--><section class="pg capa"><div class="capa-img"><img src="{IMG}{img}.webp"></div>
    <div class="capa-txt"><span class="tag">{tag}</span><h1>{titulo}</h1><p class="sub">{sub}</p></div>
    <div class="rod">EDIÇÃO NATAL 2026 · AMIGURUMIS NATALINOS DE LUXO</div></section>'''

# ------------------------------------------------------------------ conteúdo
ABREV = [
 ('Anel mágico','am','Enrole o fio duas vezes no dedo, puxe uma laçada e trabalhe os pontos dentro do anel. No fim, puxe a ponta solta para fechar o centro.'),
 ('Correntinha','corr','Faça uma laçada e puxe pela alça que está na agulha.'),
 ('Ponto baixíssimo','pbx','Insira a agulha no ponto, faça uma laçada e puxe direto por todas as alças. Usado para fechar carreiras e unir.'),
 ('Ponto baixo','pb','Insira a agulha, laçada, puxe (2 alças na agulha), laçada e puxe pelas 2. É o ponto de quase todo amigurumi.'),
 ('Ponto meio alto','pma','Laçada, insira a agulha, laçada e puxe (3 alças), laçada e puxe pelas 3 de uma vez.'),
 ('Ponto alto','pa','Laçada, insira a agulha, laçada e puxe (3 alças), laçada e puxe por 2, laçada e puxe pelas 2 restantes.'),
 ('Ponto alto duplo','pad','Duas laçadas antes de inserir a agulha; depois feche de 2 em 2 alças até sobrar uma.'),
 ('Aumento','aum','Faça 2 pontos baixos no mesmo ponto da carreira anterior. Aumenta 1 ponto.'),
 ('Diminuição','dim','Una 2 pontos em 1: puxe uma alça em cada ponto e feche as 3 alças juntas. Diminui 1 ponto.'),
 ('Diminuição invisível','dim inv','Pegue só a alça da frente de 2 pontos seguidos, laçada, puxe pelas 2 e feche como ponto baixo. Deixa a peça lisa, sem furinhos.'),
 ('Carreira','carr','Uma volta completa. No amigurumi as carreiras seguem em espiral, sem fechar.'),
 ('Laçada','lç','Passe o fio por cima da agulha, de trás para a frente.'),
 ('Alça da frente','af','Trabalhe só na alça do ponto mais perto de você. Cria uma linha decorativa ou uma base para babados.'),
 ('Alça de trás','at','Trabalhe só na alça mais distante. Usado para fazer a base reta de pés, chapéus e casinhas.'),
 ('Marcador de ponto','marc','Prenda no primeiro ponto da carreira para não perder a contagem na espiral.'),
 ('Arremate','arr','Corte o fio deixando uma ponta, puxe pela última alça e esconda dentro da peça.'),
 ('Repetir','*…* ×6','Repita o que está entre asteriscos o número de vezes indicado.'),
 ('Total de pontos','(18)','O número entre parênteses é quantos pontos a carreira deve ter no fim. Confira sempre!'),
 ('Ponto pipoca','ppc','5 pontos altos no mesmo ponto, unidos no topo. Dá relevo (bolinhas, frutinhas, botões).'),
 ('Picô','picô','3 correntinhas fechadas com ponto baixíssimo na primeira. Acabamento de borda delicado.'),
]
EXEMPLOS = [
 ('carr 1: 6 pb no am (6)','Faça 6 pontos baixos dentro do anel mágico. Total: 6 pontos.'),
 ('carr 2: aum em todos (12)','Faça um aumento em cada ponto da carreira anterior. Total: 12.'),
 ('carr 3: *1 pb, aum* ×6 (18)','Repita 6 vezes: 1 ponto baixo e 1 aumento. Total: 18.'),
 ('carr 4–8: pb em todos (18)','Da carreira 4 até a 8, faça 1 ponto baixo em cada ponto. Total: 18.'),
 ('carr 9: *1 pb, dim* ×6 (12)','Repita 6 vezes: 1 ponto baixo e 1 diminuição. Total: 12.'),
]
PALETAS = [
 ('Vermelho Clássico','Papai Noel, Mamãe Noel e guirlandas',['#9A2C3D','#F3E9D8','#1F3D2E','#C9A04F'],['Vermelho vinho','Cru','Verde pinheiro','Ouro velho']),
 ('Neve Nórdica','Bonecos de neve e amigos do inverno',['#FFFFFF','#D9E3EA','#8FA9BC','#B3263A'],['Branco','Gelo','Azul acinzentado','Vermelho']),
 ('Dourado de Luxo','Peças Estrela e centros de mesa',['#B8914A','#F3DFAE','#7A1F2B','#2B2422'],['Dourado','Champanhe','Bordô','Café']),
 ('Floresta Encantada','Duendes, árvores e enfeites',['#1F3D2E','#3F7D5C','#E7BF62','#F6F2EC'],['Verde escuro','Verde musgo','Mostarda','Marfim']),
 ('Doce Gengibre','Bonecos e casinhas de gengibre em crochê',['#A0673A','#F5E6D3','#C8102E','#FFFFFF'],['Caramelo','Bege','Vermelho','Branco']),
 ('Rosa Vintage','Anjos, bailarinas e presentes delicados',['#E8B4B8','#F7E7E3','#8C2F39','#D9C39A'],['Rosa antigo','Rosa claro','Vinho','Areia']),
]
ACAB = [
 ('Olhos na mesma carreira','Posicione os olhos de segurança na mesma carreira e à mesma distância do centro antes de fechar a peça. Simetria é o que mais separa “caseiro” de “loja”.'),
 ('Bochechas rosadas','Um toque de blush ou sombra rosa, aplicado com cotonete em movimentos circulares, dá vida ao rosto na hora.'),
 ('Sobrancelhas bordadas','Dois pontos retos com linha clara, um pouco acima dos olhos, mudam a expressão inteira.'),
 ('Laço de veludo','Troque o laço de linha por fita de veludo ou cetim. A peça muda de categoria.'),
 ('Toque dourado','Linha metálica em detalhes pequenos — estrela, guizo, botões, fivela — traz o efeito de luxo sem pesar.'),
 ('Enchimento firme','Encha aos pouquinhos e com firmeza, moldando com os dedos. Enchimento frouxo deixa a peça “murcha” e mostra os pontos.'),
 ('Fios escondidos','Arremate passando o fio por dentro da peça em várias direções antes de cortar. Nada de pontas aparecendo.'),
 ('Etiqueta kraft','Uma etiqueta com o nome da peça e a sua marca transforma o amigurumi em presente.'),
]
FOTOS = [
 ('Luz da janela','Fotografe de dia, perto de uma janela, sem flash. Luz natural é o que mais valoriza o crochê.'),
 ('Fundo simples','Um tecido claro, uma tábua de madeira ou uma manta. O amigurumi tem que ser o destaque.'),
 ('Na altura dos olhos','Abaixe o celular até a altura do rosto da peça: ela ganha personalidade.'),
 ('Um detalhe natalino','Uma pinha, um galhinho ou luzinhas desfocadas ao fundo contam a história.'),
 ('Foto de escala','Mostre a peça na mão ou ao lado de uma xícara para a cliente entender o tamanho.'),
 ('Coleção junta','Uma foto com várias peças lado a lado vende a ideia de “vitrine” e aumenta o pedido médio.'),
]
ONDE = [
 ('Status do WhatsApp','Poste 1 foto por dia a partir de novembro. Quem vê todo dia lembra de você na hora do presente.'),
 ('Instagram','Fotos da coleção no feed e o “bastidor” (a peça sendo feita) nos stories.'),
 ('Grupos do bairro e da escola','Uma foto bonita com preço e prazo de entrega. Sem textão.'),
 ('Feiras de Natal','Leve a coleção completa em vitrine: mesa cheia vende mais que peça solta.'),
]
MSGS = [
 ('Divulgação no status','🎄 Encomendas de Natal abertas!\n\nAmigurumis feitos à mão, um por um, com linha de algodão e acabamento de luxo. Perfeitos para presentear ou decorar.\n\nAs vagas vão até o dia [DATA]. Me chama aqui que eu te mando as opções! ✨'),
 ('Resposta para “quanto custa?”','Oi, [NOME]! 😊 O [PEÇA] sai por R$ [VALOR].\n\nEle é feito à mão, ponto por ponto, com linha de algodão e acabamento caprichado. Consigo entregar até [DATA].\n\nQuer que eu reserve o seu?'),
 ('Confirmação do pedido','Perfeito, [NOME]! Reservado ✨\n\nPara confirmar, o pagamento é via Pix:\n[CHAVE PIX]\n\nAssim que cair, eu já começo o seu e te mando foto do andamento. 🧶'),
 ('Entrega e agradecimento','Seu [PEÇA] ficou pronto! 🎁\n\nFoi feito com muito carinho. Se puder, me manda uma foto dele no lugarzinho dele, eu amo ver! E se gostar, me indica para uma amiga? 💛'),
]
CAL = [
 ('AGORA','Decida',['Escolher de 6 a 10 modelos para a sua vitrine no Índice Visual','Separar linhas, enchimento, olhos de segurança e agulha','Definir o destino de cada peça: presentear, decorar ou vender']),
 ('OUTUBRO','Crochete e eleve',['Crochetar as peças principais da coleção','Aplicar o Acabamento Boutique: olhos, bordados, laços e toques dourados','Fotografar cada peça assim que ficar pronta']),
 ('NOVEMBRO','Exiba',['Calcular o preço de cada peça na Calculadora de Preço Justo','Publicar as fotos no status, Instagram e grupos','Responder os pedidos com as mensagens prontas']),
 ('DEZEMBRO','Entregue e aproveite',['Embalar com etiqueta kraft e laço de veludo','Entregar as encomendas com antecedência','Decorar a sua casa e presentear quem você ama']),
]
COLECOES = [
 ('Papai Noel e Mamãe Noel','colecao-papai-noel',['galeria-papai-noel','modelo-01','modelo-04']),
 ('Renas e Duendes','colecao-renas-duendes',['modelo-basico-04']),
 ('Bonecos de Neve','colecao-bonecos-neve',[]),
 ('Doce Natal','colecao-doce-natal',['modelo-basico-06']),
 ('Amigos do Inverno','colecao-amigos-inverno',['modelo-05','modelo-12']),
 ('Enfeites para a Árvore','colecao-enfeites-arvore',['modelo-16','modelo-06','modelo-09']),
 ('Mini Presentes','colecao-mini-presentes',['galeria-mini-presentes']),
 ('Peças Estrela','colecao-pecas-estrela',['galeria-pecas-estrela']),
]

def checklist(itens):
    return ''.join(f'<div class="check"><span class="box"></span><span>{E(t)}</span></div>' for t in itens)

# ------------------------------------------------------------------ PDFs
def pdf_codigo():
    ex = ''.join(f'<tr><td><code>{E(a)}</code></td><td>{E(b)}</td></tr>' for a,b in EXEMPLOS)
    return doc('BÔNUS 1 · CÓDIGO AMIGURUMI™', [
        capa('bonus-codigo-amigurumi','BÔNUS 1','Código <em>Amigurumi</em>™','O guia de abreviações para ler qualquer receita de crochê sem travar no meio da carreira.'),
        f'''<p class="ceja">Como usar este guia</p><h2>Leia uma receita como quem lê uma frase.</h2>
        <p class="lead">Toda receita de amigurumi é escrita numa “língua” curta: abreviações, números e símbolos. Depois que você entende o código, nenhuma receita te trava.</p>
        <table><thead><tr><th style="width:28%">Ponto</th><th style="width:14%">Abrev.</th><th>Como fazer</th></tr></thead><tbody>{''.join(f'<tr><td><b>{E(a)}</b></td><td><code>{E(b)}</code></td><td>{E(c)}</td></tr>' for a,b,c in ABREV[:10])}</tbody></table>''',
        f'''<table><thead><tr><th style="width:28%">Ponto</th><th style="width:14%">Abrev.</th><th>Como fazer</th></tr></thead><tbody>{''.join(f'<tr><td><b>{E(a)}</b></td><td><code>{E(b)}</code></td><td>{E(c)}</td></tr>' for a,b,c in ABREV[10:])}</tbody></table>''',
        f'''<p class="ceja">Na prática</p><h2>Traduzindo uma receita, linha por linha.</h2>
        <p class="lead">Este é o começo de quase toda cabeça ou corpo de amigurumi. Leia a coluna da esquerda e confira a tradução.</p>
        <table><thead><tr><th style="width:42%">Está escrito</th><th>Significa</th></tr></thead><tbody>{ex}</tbody></table>
        <div class="card ouro" style="margin-top:8mm"><h3>3 regras de ouro</h3>
        <p><b>1.</b> Use sempre o marcador no primeiro ponto da carreira.</p>
        <p><b>2.</b> Conte os pontos no fim de cada carreira e compare com o número entre parênteses.</p>
        <p style="margin:0"><b>3.</b> Leia a legenda no início de cada receita: algumas autoras usam abreviações próprias.</p></div>''',
    ])

def pdf_acabamento():
    def pal(p):
        n,u,cs,nm = p
        return f'''<div class="card"><div class="cores">{''.join(f'<div style="background:{c};color:{"#2b2422" if c in ("#FFFFFF","#F3E9D8","#D9E3EA","#F3DFAE","#F6F2EC","#F5E6D3","#F7E7E3","#E8B4B8","#D9C39A","#E7BF62") else "#fff"}">{c}</div>' for c in cs)}</div>
        <h3>{n}</h3><p style="margin:0;font-size:10pt;color:#5e574f">Para: {u}<br><span class="nota">{" · ".join(nm)}</span></p></div>'''
    return doc('BÔNUS 2 · ACABAMENTO BOUTIQUE', [
        capa('bonus-acabamento-boutique','BÔNUS 2','Acabamento <em>Boutique</em> + Paletas Natalinas de Luxo','Combinações de cores e detalhes de acabamento que deixam seus amigurumis com cara de loja.'),
        f'''<p class="ceja">Paletas Natalinas de Luxo</p><h2>Cores que combinam entre si.</h2>
        <p class="lead">Uma coleção parece cara quando as peças conversam. Escolha uma paleta para cada coleção e use só as cores dela.</p>
        <div class="grid2">{''.join(pal(p) for p in PALETAS)}</div>''',
        f'''<p class="ceja">Detalhes que valorizam</p><h2 style="margin-bottom:4mm">8 toques que mudam a peça de categoria.</h2>
        <div class="grid2">{''.join(f'<div class="card"><h3><span class="badge">{i+1}.</span> {E(t)}</h3><p style="margin:0;color:#5e574f">{E(d)}</p></div>' for i,(t,d) in enumerate(ACAB))}</div>''',
    ])

def pdf_calc():
    ficha = ''.join('<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>' for _ in range(12))
    return doc('BÔNUS 3 · CALCULADORA DE PREÇO JUSTO', [
        capa('bonus-calculadora','BÔNUS 3','Calculadora de <em>Preço Justo</em>','Para nunca mais dar o seu trabalho de graça quando alguém pedir um amigurumi.'),
        f'''<p class="ceja">A fórmula</p><h2>Preço justo = custos + seu tempo + lucro.</h2>
        <p class="lead">A calculadora interativa está dentro do app (aba Bônus). Este guia mostra a conta por trás dela e traz uma ficha para você imprimir.</p>
        <div class="card"><h3>1. Materiais</h3><p style="margin:0">Linha, enchimento, olhos de segurança, fitas. Some só o que foi usado nesta peça (ex.: meio novelo = metade do preço do novelo).</p></div>
        <div class="card"><h3>2. Embalagem</h3><p style="margin:0">Caixa, saquinho, laço, etiqueta kraft.</p></div>
        <div class="card"><h3>3. Seu trabalho</h3><p style="margin:0">Horas gastas × valor da sua hora. Comece com um valor que você aceitaria receber por uma hora de qualquer outro trabalho.</p></div>
        <div class="card"><h3>4. Lucro</h3><p style="margin:0">Uma margem em cima de tudo (sugestão: 30%). É o que paga erros, linha que sobrou e o seu crescimento.</p></div>
        <p class="ceja" style="margin-top:5mm">Exemplo — Papai Noel de 20 cm</p>
        <table><tbody>
        <tr><td>Materiais</td><td style="text-align:right">R$ 18,50</td></tr><tr><td>Embalagem</td><td style="text-align:right">R$ 6,00</td></tr>
        <tr><td>Trabalho: 4 h × R$ 15,00</td><td style="text-align:right">R$ 60,00</td></tr><tr><td><b>Custo total</b></td><td style="text-align:right"><b>R$ 84,50</b></td></tr>
        <tr><td>Lucro (30%)</td><td style="text-align:right">R$ 25,35</td></tr></tbody></table>
        <div class="destaque" style="margin-top:5mm"><span style="font-size:9pt;letter-spacing:.16em;font-weight:800;color:#f3dca4">PREÇO SUGERIDO</span><b>R$ 109,85 → venda por R$ 109,90</b></div>''',
        f'''<p class="ceja">Para imprimir</p><h2>Ficha de precificação</h2>
        <table class="ficha"><thead><tr><th>Peça</th><th>Materiais</th><th>Embalagem</th><th>Horas × R$/h</th><th>Lucro %</th><th>Preço final</th></tr></thead><tbody>{ficha}</tbody></table>
        <p class="nota" style="margin-top:5mm">Dica: depois de vender as primeiras peças, reveja o valor da sua hora. Se todo mundo compra sem negociar, o preço provavelmente está baixo.</p>''',
    ])

def pdf_venda():
    return doc('BÔNUS 4 · VENDA SUA COLEÇÃO', [
        capa('bonus-venda-sua-colecao','BÔNUS 4','Guia <em>Venda sua Coleção</em> + Calendário da Temporada','Fotos com o celular, onde publicar, mensagens prontas para o WhatsApp e o que fazer em cada mês até dezembro.'),
        f'''<p class="ceja">Fotos com o celular</p><h2>6 regras para fotos que vendem.</h2>
        <div class="grid2">{''.join(f'<div class="card"><h3><span class="badge">{i+1}.</span> {E(t)}</h3><p style="margin:0;color:#5e574f">{E(d)}</p></div>' for i,(t,d) in enumerate(FOTOS))}</div>
        <p class="ceja" style="margin-top:6mm">Onde publicar</p>
        {''.join(f'<div class="card"><h3>{E(t)}</h3><p style="margin:0;color:#5e574f">{E(d)}</p></div>' for t,d in ONDE)}''',
        f'''<p class="ceja">Mensagens prontas</p><h2>Copie, troque os [colchetes] e envie.</h2>
        {''.join(f'<div class="card"><h3>{E(t)}</h3><div class="msg">{E(m)}</div></div>' for t,m in MSGS)}''',
        f'''<p class="ceja">Calendário da Temporada</p><h2>O que fazer em cada mês até o Natal.</h2>
        <div class="grid2">{''.join(f'<div class="card"><p class="ceja" style="margin:0">{m}</p><h3>{v}</h3>{checklist(t)}</div>' for m,v,t in CAL)}</div>
        <p class="nota">Cada crocheteira avança no seu ritmo. O que você conquistar depende do seu trabalho e de como decidir oferecer suas peças.</p>''',
    ])

def pdf_metodo():
    P = [('ESCOLHA','a sua coleção','passo-escolha','Percorra o Índice Visual e escolha de 6 a 10 modelos que combinam entre si. Pense na mesa pronta: um personagem principal, peças médias e pequenas.',['Escolher a paleta (Bônus 2) antes de comprar linha','Misturar tamanhos: 1–2 peças estrela, 3–4 médias, mini presentes','Anotar o destino de cada peça']),
         ('CROCHETE','suas peças','passo-crochete','Siga cada receita de crochê carreira por carreira. Comece pela peça mais simples para pegar ritmo.',['Usar marcador no primeiro ponto','Conferir o total de pontos de cada carreira','Consultar o Código Amigurumi™ ao travar numa abreviação']),
         ('ELEVE','o acabamento','passo-eleve','O acabamento é o que transforma “feito em casa” em “de loja”. Reserve tempo para ele.',['Olhos alinhados e enchimento firme','Bochechas, sobrancelhas e laço de veludo','Fios escondidos e etiqueta kraft']),
         ('EXIBA','a sua coleção','passo-exiba','Monte a sua vitrine: presenteie, decore ou fotografe e ofereça.',['Fotografar com luz da janela','Calcular o preço justo (Bônus 3)','Publicar com as mensagens prontas (Bônus 4)'])]
    def bl(lst, off):
        return ''.join(f'''<div class="card passo"><img src="{IMG}{img}.webp"><div><p class="ceja" style="margin:0">Passo {i+1+off}</p>
      <h3><span style="color:#7a1f2b">{v}</span> {r}</h3><p style="color:#5e574f">{E(t)}</p>{checklist(c)}</div></div>''' for i,(v,r,img,t,c) in enumerate(lst))
    return doc('GUIA DO MÉTODO VITRINE DE NATAL™', [
        capa('mockup-produto-completo','GUIA','Método <em>Vitrine de Natal</em>™','A ordem de quem enche a mesa de amigurumis, em 4 passos: escolha, crochete, eleve e exiba.'),
        f'''<p class="ceja">Por que um método</p><h2>Não te falta talento. Te falta uma ordem.</h2>
        <p class="lead">A diferença entre a mesa com 3 amigurumis e a mesa com 30 não é a técnica: é saber o que crochetar, em que ordem e para quando. Estes 4 passos são essa ordem.</p>{bl(P[:2],0)}''',
        bl(P[2:],2) + '<div class="card ouro"><h3>Próximo passo</h3><p style="margin:0">Abra o Calendário da Temporada no app e marque cada etapa conforme for concluindo.</p></div>',
    ])

def pdf_indice():
    pags = []
    for k in range(0, len(COLECOES), 2):
        bl = ''
        for nome, capa_img, fotos in COLECOES[k:k+2]:
            imgs = [capa_img] + fotos
            bl += f'''<div style="margin-bottom:8mm"><p class="ceja">Coleção</p><h2 style="font-size:18pt">{nome}</h2>
            <div class="grid3">{''.join(f'<div class="thumb"><img src="{IMG}{f}.webp"></div>' for f in imgs[:6])}</div></div>'''
        pags.append(bl)
    return doc('ÍNDICE VISUAL', [
        capa('mockup-indice-visual','ÍNDICE VISUAL','Índice <em>Visual</em> das coleções','As 8 coleções de receitas de amigurumi à vista, para escolher os modelos da sua vitrine em minutos.'),
        f'''<p class="ceja">As 8 coleções</p><h2>Escolha pela foto.</h2><p class="lead">Cada coleção reúne receitas de crochê de um tema. Marque as que você quer crochetar primeiro.</p>
        <div class="grid3" style="grid-template-columns:repeat(4,1fr)">{''.join(f'<div><div class="thumb"><img src="{IMG}{c}.webp"><span>{n}</span></div><div class="check" style="border:0"><span class="box"></span><span style="font-size:9pt">Quero fazer</span></div></div>' for n,c,_ in COLECOES)}</div>''',
        *pags,
    ])


def pdf_etiquetas():
    css = """<style>
    .folha{display:grid;gap:4mm}
    .tg{position:relative;border:1px dashed #b8a98f;border-radius:3mm;height:62mm;padding-top:11mm !important;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:6mm;overflow:hidden}
    .tg .furo{position:absolute;top:5mm;width:5mm;height:5mm;border-radius:50%;border:1.5px solid currentColor;opacity:.6}
    .tg b{font-family:F;font-weight:800;font-size:19pt;line-height:1.05}
    .tg i{font-family:F;font-style:italic;font-weight:700;font-size:13pt;display:block;margin-top:1.5mm}
    .tg small{font-size:8pt;letter-spacing:.18em;font-weight:800;margin-top:3mm;opacity:.85}
    .tg .ln{width:80%;border-bottom:1px solid currentColor;opacity:.5;height:7mm;text-align:left;font-size:9pt;font-weight:700}
    .t1{background:#f5e6d3;color:#7a1f2b}.t2{background:#fff;color:#1f3d2e}.t3{background:#9a2c3d;color:#fff}.t4{background:#1f3d2e;color:#f3dca4}
    .cart{border:1px dashed #b8a98f;border-radius:3mm;height:118mm;padding:12mm;display:flex;flex-direction:column;justify-content:center;text-align:center;background:#fff}
    .cart h3{font-size:22pt;color:#7a1f2b}.cart p{color:#5e574f;font-size:11pt;margin-top:4mm}
    .ades{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm}
    .ad{aspect-ratio:1/1;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;border:1px dashed #b8a98f}
    .ad b{font-family:F;font-weight:800;font-size:12pt;line-height:1.05}.ad span{font-size:6.5pt;font-weight:800;letter-spacing:.14em;margin-top:1mm}
    </style>"""
    estilos=['t1','t2','t3','t4']
    textos=[('Feliz','Natal','FEITO À MÃO'),('Feito','à mão','COM CARINHO'),('Com','carinho','PARA VOCÊ'),('Boas','festas','FEITO À MÃO'),
            ('Feliz','Natal','FEITO À MÃO'),('Feito','à mão','COM CARINHO')]
    tags=''.join(f'<div class="tg {estilos[i%4]}"><span class="furo"></span><b>{a}</b><i>{b}</i><small>{c}</small></div>' for i,(a,b,c) in enumerate(textos))
    para=''.join(f'<div class="tg {estilos[i%4]}"><span class="furo"></span><b style="font-size:15pt">Um presente</b><i>feito à mão</i><div class="ln">Para:</div><div class="ln">De:</div></div>' for i in range(6))
    cuid=''.join(f'<div class="tg t2" style="height:62mm"><span class="furo"></span><b style="font-size:13pt">Cuidados com o seu amigurumi</b><p style="font-size:8.5pt;color:#5e574f;margin-top:3mm;text-align:left">• Lavar à mão, com água fria e sabão neutro.<br>• Secar à sombra, deitado.<br>• Não deixar ao alcance de crianças menores de 3 anos (peças pequenas).<br>• Feito à mão: cada peça é única.</p></div>' for _ in range(6))
    cart=''.join(f'<div class="cart" style="border-color:#c9a45c"><p class="ceja">Obrigada!</p><h3>Este amigurumi foi feito à mão, ponto por ponto, só para você.</h3><p>Se gostou, me marca nas redes e me indica para uma amiga. Isso ajuda demais quem trabalha com crochê. 💛</p><div class="linha" style="margin-top:10mm"></div><p class="nota">Seu nome / @ da sua marca</p></div>' for _ in range(2))
    ad=''.join(f'<div class="ad {estilos[i%4]}"><b>{t}</b><span>{u}</span></div>' for i,(t,u) in enumerate([('Feito à mão','AMIGURUMI'),('Feliz Natal','COM CARINHO'),('Feito com amor','CROCHÊ'),('Boas festas','FEITO À MÃO')]*5))
    g2='<div class="folha" style="grid-template-columns:1fr 1fr 1fr">'
    return doc('ETIQUETAS & EMBALAGENS NATALINAS', [
        capa('mockup-oferta','EXTRA','Etiquetas & <em>Embalagens</em> Natalinas','Tags, cartões e adesivos para imprimir e entregar seus amigurumis com acabamento de loja.'),
        css+'<p class="ceja">Como imprimir</p><h2>Imprima, recorte e amarre.</h2><p class="lead">Use papel couché 180 g ou papel kraft. Imprima em “tamanho real” (100%), recorte nas linhas tracejadas e faça o furo para passar a fita ou o barbante.</p>'+g2+tags+'</div>',
        css+'<p class="ceja">Tags “Para / De”</p>'+g2+para+'</div>',
        css+'<p class="ceja">Tags de cuidados</p>'+g2+cuid+'</div>',
        css+'<p class="ceja">Cartão de agradecimento</p><div class="folha">'+cart+'</div>',
        css+'<p class="ceja">Adesivos redondos (5 cm)</p><p class="lead">Para fechar saquinhos e caixinhas. Imprima em papel adesivo.</p><div class="ades">'+ad+'</div>',
    ])

PDFS = {
  'extras/etiquetas-embalagens-natalinas.pdf': pdf_etiquetas,
  'guia-metodo-vitrine-de-natal.pdf': pdf_metodo,
  'indice-visual-colecoes.pdf': pdf_indice,
  'bonus-1-codigo-amigurumi.pdf': pdf_codigo,
  'bonus-2-acabamento-boutique-paletas.pdf': pdf_acabamento,
  'bonus-3-calculadora-preco-justo.pdf': pdf_calc,
  'bonus-4-venda-sua-colecao-calendario.pdf': pdf_venda,
}

async def main():
    async with async_playwright() as p:
        kw = {'args': ['--no-sandbox']}
        if os.path.exists('/usr/bin/google-chrome'): kw['executable_path'] = '/usr/bin/google-chrome'
        b = await p.chromium.launch(**kw)
        pg = await b.new_page()
        for nome, fn in PDFS.items():
            tmp = OUT / '_tmp.html'; tmp.write_text(fn(), encoding='utf-8')
            await pg.goto(tmp.as_uri()); await pg.wait_for_timeout(500)
            await pg.pdf(path=str(OUT / nome), format='A4', print_background=True, prefer_css_page_size=True)
            tmp.unlink(); print(nome, os.path.getsize(OUT / nome) // 1024, 'KB')
        await b.close()

if __name__ == '__main__':
    asyncio.run(main())
