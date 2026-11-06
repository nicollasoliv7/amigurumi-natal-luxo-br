"""Gera as capas (800x800) dos order bumps e do upsell em ofertas/capas/ e app/extras/.
Uso: python3 fonte/ofertas/gerar_capas.py
"""
import asyncio, pathlib, os, shutil
from playwright.async_api import async_playwright

RAIZ = pathlib.Path(__file__).resolve().parents[2]
FON = (RAIZ / 'app' / 'fontes').as_uri() + '/'
OUT = RAIZ / 'ofertas' / 'capas'; OUT.mkdir(parents=True, exist_ok=True)
APP = RAIZ / 'app' / 'extras'; APP.mkdir(parents=True, exist_ok=True)

CSS = f"""
@font-face{{font-family:F;src:url({FON}Fraunces_800ExtraBold.woff2);font-weight:800}}
@font-face{{font-family:F;src:url({FON}Fraunces_700Bold_Italic.woff2);font-weight:700;font-style:italic}}
@font-face{{font-family:N;src:url({FON}NunitoSans_800ExtraBold.woff2);font-weight:800}}
@font-face{{font-family:N;src:url({FON}NunitoSans_600SemiBold.woff2);font-weight:600}}
*{{box-sizing:border-box;margin:0}}
body{{width:800px;height:800px;overflow:hidden}}
.c{{width:800px;height:800px;position:relative;padding:34px;font-family:N;color:#fbf7f0;
  background:radial-gradient(70% 55% at 50% 58%,#3c6c5299,transparent 72%),linear-gradient(180deg,#1f3d2e,#0f2118)}}
.c.vinho{{background:radial-gradient(70% 55% at 50% 58%,#c9445a66,transparent 72%),linear-gradient(180deg,#7a1f2b,#3d0d15)}}
.m{{position:absolute;inset:22px;border:3px solid #c9a45c;border-radius:30px}}
.m::after{{content:"";position:absolute;inset:9px;border:1px solid #c9a45c88;border-radius:22px}}
.top{{position:relative;text-align:center;margin-top:30px;font-size:17px;letter-spacing:.28em;font-weight:800;color:#d9c39a}}
.sel{{position:absolute;top:58px;right:58px;width:132px;height:132px;border-radius:50%;background:linear-gradient(150deg,#fbf0d2,#d6b064);
  color:#7a1f2b;display:grid;place-items:center;text-align:center;font-family:F;font-weight:800;line-height:1;box-shadow:0 14px 30px -8px #000;transform:rotate(8deg);z-index:3}}
.sel b{{font-family:N;font-weight:800;font-size:40px;display:block}} .sel span{{font-family:N;font-size:14px;letter-spacing:.12em}}
.ilu{{position:absolute;left:0;right:0;top:120px;height:400px;display:flex;align-items:center;justify-content:center}}
.tit{{position:absolute;left:60px;right:60px;bottom:96px;text-align:center}}
.tit h1{{font-family:F;font-weight:800;font-size:66px;line-height:1.02;color:#fffaf1;text-shadow:0 4px 18px #0007}}
.tit h1 em{{font-style:italic;font-weight:700;background:linear-gradient(100deg,#c9a45c,#f6e6b8 40%,#d6b064 70%);-webkit-background-clip:text;color:transparent}}
.tit p{{margin-top:14px;font-size:22px;font-weight:600;color:#fbf7f0d9}}
.rod{{position:absolute;left:0;right:0;bottom:52px;text-align:center;font-size:14px;letter-spacing:.22em;font-weight:800;color:#d9c39a}}
.luz{{position:absolute;border-radius:50%;filter:blur(1px)}}
"""
LUZES = ''.join(f'<i class="luz" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px;background:radial-gradient(circle,{c}cc,{c}22 50%,transparent 70%)"></i>'
                for x, y, s, c in [(60,140,70,'#e7bf62'),(690,300,60,'#b3263a'),(110,470,46,'#fff1cf'),(650,520,80,'#e7bf62'),(380,120,34,'#fff1cf'),(200,300,30,'#3f7d5c')])

def gnomo(x, s, hat, beard='#f3ece2', rot=0):
    return f'''<g transform="translate({x} 0) scale({s}) rotate({rot} 0 300)">
      <path d="M-62 300 Q0 120 70 0 Q55 140 62 300Z" fill="{hat}"/><path d="M-62 300 Q0 120 70 0" fill="none" stroke="#0002" stroke-width="6"/>
      <circle cx="70" cy="0" r="14" fill="#fff"/>
      <rect x="-74" y="286" width="148" height="30" rx="15" fill="#fff"/>
      <path d="M-70 320 Q-80 420 0 470 Q80 420 70 320 Z" fill="{beard}"/>
      <path d="M-40 340 Q0 380 40 340 M-50 380 Q0 420 50 380" stroke="#d8cbb8" stroke-width="5" fill="none"/>
      <ellipse cx="0" cy="326" rx="26" ry="22" fill="#e7a98a"/>
      <path d="M-58 440 L-70 520 L70 520 L58 440Z" fill="{hat}" opacity=".85"/></g>'''

ILU = {
 'espirais': '''<svg width="560" height="400" viewBox="0 0 560 400">
   <path d="M0 18 Q280 70 560 18" stroke="#d9c39a" stroke-width="3" fill="none"/>''' + ''.join(f'''
   <g transform="translate({x} 0)"><line x1="0" y1="{30+d}" x2="0" y2="{70+d}" stroke="#d9c39a" stroke-width="3"/>
   <circle cx="0" cy="{98+d}" r="30" fill="{h}"/><circle cx="-9" cy="{96+d}" r="3.5" fill="#2b2422"/><circle cx="9" cy="{96+d}" r="3.5" fill="#2b2422"/>
   ''' + ''.join(f'<ellipse cx="0" cy="{140+d+k*26}" rx="{34-k*3}" ry="11" fill="{c}" transform="rotate({-14 if k%2 else 14} 0 {140+d+k*26})"/>' for k, c in enumerate([a,b,a,b,a,b,a,b])) +
   f'<circle cx="0" cy="{358+d}" r="9" fill="{a}"/></g>'
   for x, d, h, a, b in [(90,0,'#e7c7a5','#b3263a','#fff'),(200,22,'#fff','#2f6b4f','#fff'),(310,6,'#e7c7a5','#b3263a','#2f6b4f'),(420,26,'#2b2422','#fff','#b3263a'),(500,4,'#fff','#c9a04f','#fff')]) + '</svg>',
 'gnomos': f'''<svg width="560" height="390" viewBox="-300 -40 600 580">{gnomo(-180,0.62,'#2f6b4f',rot=-6)}{gnomo(180,0.62,'#c9a04f',rot=6)}{gnomo(0,0.8,'#b3263a')}</svg>''',
 'presepio': '''<svg width="560" height="400" viewBox="0 0 560 400">
   <path d="M280 20 l14 40 42 0 -34 24 13 40 -35 -25 -35 25 13 -40 -34 -24 42 0Z" fill="#f3dca4"/>
   <path d="M280 60 L280 0" stroke="#f3dca466" stroke-width="2"/>
   <path d="M120 200 L280 120 L440 200" fill="none" stroke="#c9a45c" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
   <rect x="150" y="196" width="260" height="170" fill="#ffffff10" stroke="#c9a45c" stroke-width="6" rx="8"/>
   <g transform="translate(220 260)"><circle r="22" fill="#e7c7a5"/><path d="M-34 110 Q-30 20 0 18 Q30 20 34 110Z" fill="#3f5f9c"/><path d="M-24 -6 Q0 -40 24 -6 L28 40 L-28 40Z" fill="#3f5f9c" opacity=".7"/></g>
   <g transform="translate(340 260)"><circle r="22" fill="#d9a77e"/><path d="M-34 110 Q-30 20 0 18 Q30 20 34 110Z" fill="#8a5a3a"/><rect x="-18" y="-14" width="36" height="14" rx="6" fill="#6b4a2e"/></g>
   <g transform="translate(280 330)"><ellipse rx="40" ry="16" fill="#c9a45c"/><circle cy="-12" r="13" fill="#f0d0b0"/></g>
   <g transform="translate(70 120)"><circle r="18" fill="#f0d0b0"/><path d="M-26 90 Q-20 16 0 14 Q20 16 26 90Z" fill="#fff"/><path d="M-10 30 Q-60 0 -50 60Z M10 30 Q60 0 50 60Z" fill="#f3dca4"/><ellipse cy="-24" rx="16" ry="5" fill="none" stroke="#f3dca4" stroke-width="3"/></g>
   <g transform="translate(490 120)"><circle r="18" fill="#f0d0b0"/><path d="M-26 90 Q-20 16 0 14 Q20 16 26 90Z" fill="#fff"/><path d="M-10 30 Q-60 0 -50 60Z M10 30 Q60 0 50 60Z" fill="#f3dca4"/><ellipse cy="-24" rx="16" ry="5" fill="none" stroke="#f3dca4" stroke-width="3"/></g></svg>''',
 'etiquetas': '''<svg width="560" height="400" viewBox="0 0 560 400">''' + ''.join(f'''
   <g transform="translate({x} {y}) rotate({r})"><path d="M0 0 L150 0 L150 210 L75 250 L0 210Z" fill="{bg}" stroke="#c9a45c" stroke-width="4"/>
   <circle cx="75" cy="30" r="10" fill="#1f3d2e" stroke="#c9a45c" stroke-width="3"/>
   <text x="75" y="105" text-anchor="middle" font-family="F" font-weight="800" font-size="24" fill="{tx}">{t1}</text>
   <text x="75" y="135" text-anchor="middle" font-family="F" font-style="italic" font-weight="700" font-size="20" fill="{tx}">{t2}</text>
   <path d="M30 160 h90" stroke="{tx}" stroke-width="1.5" stroke-dasharray="4 5"/></g>'''
   for x, y, r, bg, tx, t1, t2 in [(40,110,-12,'#f5e6d3','#7a1f2b','Feito','à mão'),(205,60,0,'#fff','#1f3d2e','Feliz','Natal'),(370,110,12,'#b3263a','#fff','Com','carinho')]) + '''
   <path d="M120 70 Q200 0 280 60 Q360 0 440 70" stroke="#d9c39a" stroke-width="3" fill="none" stroke-dasharray="2 6"/></svg>''',
 'anointeiro': '<svg width="540" height="340" viewBox="0 -10 640 400">' + ''.join(
   f'<g transform="translate({60+(i%4)*160} {40+(i//4)*125})"><circle r="46" fill="{c}" stroke="#c9a45c" stroke-width="3"/><text y="7" text-anchor="middle" font-family="N" font-weight="800" font-size="19" fill="{t}">{m}</text></g>'
   for i, (m, c, t) in enumerate([('JAN','#ffffff1a','#fbf7f0'),('FEV','#ffffff1a','#fbf7f0'),('PÁSCOA','#f3dca4','#7a1f2b'),('ABR','#ffffff1a','#fbf7f0'),
                                   ('MÃES','#e8b4b8','#7a1f2b'),('JUNINA','#e7bf62','#3b2b0e'),('PAIS','#8fa9bc','#1f2a3a'),('BEBÊ','#f7e7e3','#7a1f2b'),
                                   ('PRIMAV.','#3f7d5c','#fff'),('CRIANÇA','#c9a04f','#fff'),('HALLOW.','#d97b2b','#fff'),('NATAL','#b3263a','#fff')])) + '</svg>',
}
ILU['essencial'] = '<svg width="540" height="300" viewBox="0 0 640 260">' + ''.join(
   f'<g transform="translate({80+i*160} 130)"><circle r="66" fill="{c}" stroke="#c9a45c" stroke-width="4"/><text y="8" text-anchor="middle" font-family="N" font-weight="800" font-size="21" fill="{t}">{m}</text></g>'
   for i, (m, c, t) in enumerate([('PÁSCOA','#f3dca4','#7a1f2b'),('MÃES','#e8b4b8','#7a1f2b'),('BEBÊ','#f7e7e3','#7a1f2b'),('CRIANÇA','#c9a04f','#fff')])) + '</svg>'

CAPAS = {
 'espirais': ('', 'ORDER BUMP', 'Espirais <em>Natalinas</em>', 'Enfeites de amigurumi para pendurar na árvore', '-86%'),
 'gnomos':   ('', 'ORDER BUMP', '24 <em>Gnomos</em> Natalinos', 'Receitas de amigurumi rápidas para presentear em set', '-82%'),
 'presepio': ('vinho', 'ORDER BUMP', 'Presépio & <em>Anjinhos</em>', 'Receitas de amigurumi para montar o presépio completo', '-80%'),
 'etiquetas':('vinho', 'ORDER BUMP', 'Etiquetas & <em>Embalagens</em>', 'Tags natalinas para imprimir e presentear com acabamento de loja', '-80%'),
 'anointeiro':('', 'OFERTA ÚNICA', 'Amigurumis o <em>Ano Inteiro</em>', 'Coleções de amigurumi para vender em todas as datas do ano', '12'),
 'essencial':('vinho', 'OFERTA ÚNICA', 'Amigurumis <em>Essencial</em>', 'As 4 datas que mais vendem amigurumi depois do Natal', '4'),
}

def html(k):
    cls, _, tit, sub, sel = CAPAS[k]
    selo = f'<div class="sel"><div><b>{sel}</b><span>{"COLEÇÕES" if k in ("anointeiro","essencial") else "HOJE"}</span></div></div>'
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
    <div class="c {cls}">{LUZES}<div class="m"></div>{selo}<div class="top">AMIGURUMIS NATALINOS DE LUXO</div>
    <div class="ilu">{ILU[k]}</div><div class="tit"><h1>{tit}</h1><p>{sub}</p></div><div class="rod">{"PDF PARA IMPRIMIR" if k=="etiquetas" else "RECEITAS DE CROCHÊ · PASSO A PASSO"}</div></div></body></html>'''

async def main():
    async with async_playwright() as p:
        kw = {'args': ['--no-sandbox']}
        if os.path.exists('/usr/bin/google-chrome'): kw['executable_path'] = '/usr/bin/google-chrome'
        b = await p.chromium.launch(**kw); pg = await b.new_page(viewport={'width': 800, 'height': 800})
        for k in CAPAS:
            tmp = OUT / '_t.html'; tmp.write_text(html(k), encoding='utf-8')
            await pg.goto(tmp.as_uri()); await pg.wait_for_timeout(400)
            png = OUT / f'{k}.png'; await pg.screenshot(path=str(png)); tmp.unlink()
            from PIL import Image
            Image.open(png).convert('RGB').save(APP / f'{k}.webp', 'WEBP', quality=86)
            print(k)
        await b.close()

if __name__ == '__main__':
    asyncio.run(main())
