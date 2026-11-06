"""Gera as imagens do checkout em ofertas/checkout/:
- produto-principal.png  (800x800)  capa do produto Front-End
- banner-desktop.png     (1200x300) banner de 3 passos, fundo branco
- banner-mobile.png      (800x400)  banner de 3 passos, fundo branco
Uso: python3 fonte/ofertas/gerar_checkout.py
"""
import asyncio, pathlib, os
from playwright.async_api import async_playwright

RAIZ = pathlib.Path(__file__).resolve().parents[2]
FON = (RAIZ / 'app' / 'fontes').as_uri() + '/'
IMG = (RAIZ / 'imagens').as_uri() + '/'
OUT = RAIZ / 'ofertas' / 'checkout'; OUT.mkdir(parents=True, exist_ok=True)

FONTES = f"""
@font-face{{font-family:F;src:url({FON}Fraunces_800ExtraBold.woff2);font-weight:800}}
@font-face{{font-family:F;src:url({FON}Fraunces_700Bold_Italic.woff2);font-weight:700;font-style:italic}}
@font-face{{font-family:N;src:url({FON}NunitoSans_800ExtraBold.woff2);font-weight:800}}
@font-face{{font-family:N;src:url({FON}NunitoSans_700Bold.woff2);font-weight:700}}
@font-face{{font-family:N;src:url({FON}NunitoSans_600SemiBold.woff2);font-weight:600}}
*{{box-sizing:border-box;margin:0}} body{{overflow:hidden}}
"""

CAPA = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{FONTES}
body{{width:800px;height:800px}}
.c{{width:800px;height:800px;position:relative;font-family:N;color:#fbf7f0;
  background:url({IMG}hero-vitrine-natal.webp) center 18%/100% auto no-repeat,#3d0d15}}
.c::before{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,#3d0d1500 30%,#3d0d15cc 58%,#2a0810 78%)}}
.m{{position:absolute;inset:22px;border:3px solid #c9a45c;border-radius:30px}}
.m::after{{content:"";position:absolute;inset:9px;border:1px solid #c9a45c88;border-radius:22px}}
.sel{{position:absolute;top:52px;right:52px;width:138px;height:138px;border-radius:50%;background:linear-gradient(150deg,#fbf0d2,#d6b064);
  color:#7a1f2b;display:grid;place-items:center;text-align:center;font-family:F;font-weight:800;line-height:1;box-shadow:0 14px 30px -8px #000;transform:rotate(8deg)}}
.sel b{{font-family:N;font-weight:800;font-size:34px;display:block}} .sel span{{font-family:N;font-size:13px;letter-spacing:.12em}}
.tit{{position:absolute;left:56px;right:56px;bottom:84px;text-align:center}}
.tit small{{display:block;font-size:16px;letter-spacing:.3em;font-weight:800;color:#d9c39a;margin-bottom:12px}}
.tit h1{{font-family:F;font-weight:800;font-size:68px;line-height:1;color:#fffaf1;text-shadow:0 4px 18px #0009}}
.tit h1 em{{font-style:italic;font-weight:700;background:linear-gradient(100deg,#c9a45c,#f6e6b8 40%,#d6b064 70%);-webkit-background-clip:text;color:transparent}}
.tit p{{margin-top:16px;font-size:22px;font-weight:600;color:#fbf7f0e6}}
.rod{{position:absolute;left:0;right:0;bottom:46px;text-align:center;font-size:14px;letter-spacing:.22em;font-weight:800;color:#d9c39a}}
</style></head><body><div class="c"><div class="m"></div>
<div class="sel"><div><b>+4</b><span>BÔNUS</span></div></div>
<div class="tit"><small>COLEÇÃO COMPLETA</small><h1>Amigurumis Natalinos <em>de Luxo</em></h1>
<p>Receitas de crochê passo a passo, carreira por carreira</p></div>
<div class="rod">ACESSO NO CELULAR · APP + PDF</div></div></body></html>"""

ICONES = {
 'pix': '<svg viewBox="0 0 48 48"><path d="M24 4 44 24 24 44 4 24Z" fill="none" stroke="currentColor" stroke-width="4" stroke-linejoin="round"/><path d="M15 24h18M24 15v18" stroke="currentColor" stroke-width="4" stroke-linecap="round"/></svg>',
 'mail': '<svg viewBox="0 0 48 48"><rect x="5" y="10" width="38" height="28" rx="5" fill="none" stroke="currentColor" stroke-width="4"/><path d="m7 13 17 13 17-13" fill="none" stroke="currentColor" stroke-width="4" stroke-linejoin="round"/></svg>',
 'agulha': '<svg viewBox="0 0 48 48"><circle cx="18" cy="30" r="12" fill="none" stroke="currentColor" stroke-width="4"/><path d="M10 26q8 4 16 0M10 33q8 4 16 0" stroke="currentColor" stroke-width="3" fill="none"/><path d="M28 20 43 5" stroke="currentColor" stroke-width="4" stroke-linecap="round"/><path d="M43 5q3 3 0 5" stroke="currentColor" stroke-width="3" fill="none"/></svg>',
}
PASSOS = [('pix', 'Pague no Pix', 'Leva 1 minuto'), ('mail', 'Receba o acesso', 'Na hora, no seu e-mail'), ('agulha', 'Comece a crochetar', 'Ainda hoje')]

def banner(w, h, mobile):
    passos = ''.join(f'''<div class="p"><div class="n">{i+1}</div><div class="ic">{ICONES[k]}</div>
      <div class="t"><b>{t}</b><span>{s}</span></div></div>{'<div class="seta">›</div>' if i < 2 else ''}'''
      for i, (k, t, s) in enumerate(PASSOS))
    tam = dict(h2=40 if mobile else 33, b=24 if mobile else 22, s=17 if mobile else 16, ic=46 if mobile else 44)
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{FONTES}
body{{width:{w}px;height:{h}px}}
.c{{width:{w}px;height:{h}px;background:#fff;font-family:N;color:#2b2422;display:flex;flex-direction:column;justify-content:center;
  padding:{'26px 28px' if mobile else '22px 48px'};border-bottom:6px solid #b3263a;position:relative}}
.c::before{{content:"";position:absolute;left:0;right:0;top:0;height:6px;background:repeating-linear-gradient(90deg,#b3263a 0 26px,#fff 26px 40px,#2f6b4f 40px 66px,#fff 66px 80px)}}
h2{{font-family:F;font-weight:800;font-size:{tam['h2']}px;line-height:1.08;text-align:center;color:#3d0d15}}
h2 em{{font-style:italic;font-weight:700;color:#b3263a}}
.ps{{display:flex;align-items:center;justify-content:center;gap:{'10px' if mobile else '18px'};margin-top:{'26px' if mobile else '30px'};
  {'flex-direction:column;align-items:stretch' if mobile else ''}}}
.p{{display:flex;align-items:center;gap:14px;background:#fbf7f0;border:2px solid #ead9b8;border-radius:16px;padding:{'10px 16px' if mobile else '20px 20px'};{'' if mobile else 'flex:1'}}}
.n{{flex:none;width:34px;height:34px;border-radius:50%;background:#b3263a;color:#fff;font-weight:800;font-size:19px;display:grid;place-items:center}}
.ic{{flex:none;width:{tam['ic']}px;height:{tam['ic']}px;color:#2f6b4f}} .ic svg{{width:100%;height:100%}}
.t{{white-space:nowrap}} .t b{{display:block;font-size:{tam['b']}px;font-weight:800;line-height:1.1}} .t span{{font-size:{tam['s']}px;font-weight:600;color:#6b5f58}}
.seta{{font-size:40px;font-weight:800;color:#c9a45c;line-height:1;{'display:none' if mobile else ''}}}
</style></head><body><div class="c"><h2>Você está a 3 passos de crochetar <em>seus amigurumis de Natal</em></h2>
<div class="ps">{passos}</div></div></body></html>"""

ITENS = [('produto-principal', CAPA, 800, 800), ('banner-desktop', banner(1200, 300, False), 1200, 300),
         ('banner-mobile', banner(800, 400, True), 800, 400)]

async def main():
    async with async_playwright() as p:
        kw = {'args': ['--no-sandbox']}
        if os.path.exists('/usr/bin/google-chrome'): kw['executable_path'] = '/usr/bin/google-chrome'
        b = await p.chromium.launch(**kw)
        for nome, html, w, h in ITENS:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            tmp = OUT / '_t.html'; tmp.write_text(html, encoding='utf-8')
            await pg.goto(tmp.as_uri()); await pg.wait_for_timeout(500)
            await pg.screenshot(path=str(OUT / f'{nome}.png')); tmp.unlink(); await pg.close()
            print(nome)
        await b.close()

if __name__ == '__main__':
    asyncio.run(main())
