# Amigurumis Natalinos de Luxo — Página de vendas (BR 2026)

Página de vendas estática, em português, pronta para hospedar (GitHub Pages, Vercel, Netlify ou qualquer hospedagem).

## Estrutura

```
index.html      → a página de vendas (HTML + CSS + JS num único arquivo)
app/            → o mini app de entregáveis (área da aluna, sem login)
upsell/         → página de upsell + downsell (depois do checkout)
ofertas/        → textos dos order bumps/upsell e capas para o checkout
imagens/        → todas as imagens usadas na página (.webp)
fonte/          → arquivos-fonte usados para gerar o index.html
```

## Antes de publicar

No `index.html` (ou em `fonte/` e depois gere de novo):

- **Checkout:** troque `#SEU-LINK-DE-CHECKOUT` pelo link do seu checkout (`CHECKOUT` em `fonte/build.py`).
- **VSL:** cole a URL de incorporação do vídeo em `VSL_URL` (`fonte/app.js`). Vazio = só a imagem.
- **Pixel / UTMs:** cole os scripts no comentário `PIXEL / SCRIPTS DE RASTREAMENTO`, no `<head>`.
- **Rodapé:** e-mail de contato e links de Termos e Política de privacidade.
- **Depoimentos:** a seção tem 8 espaços esperando os prints reais (procure `DEPOIMENTO` no HTML).

## Gerar o index.html a partir da fonte

```bash
python3 fonte/build.py
```

## Mini app de entregáveis (`app/`)

É o link que a cliente recebe depois da compra (ex.: `seudominio.com/app/`).
Não tem senha: na primeira visita ela digita o nome (ou pula) e já entra.
Tudo o que ela marca (método, calendário, favoritas, contador, calculadora) fica salvo no próprio celular.

**O que já funciona:**
- 8 coleções com fotos, filtro de favoritas e "já comecei"
- Índice Visual com filtro e foto ampliada
- Método Vitrine de Natal™ e Calendário da Temporada com progresso
- Contador de carreiras (vários projetos, vibração, tela sempre acesa)
- Bônus interativos: Código Amigurumi™ (com busca), paletas, calculadora de preço, mensagens prontas com botão de WhatsApp
- 6 PDFs prontos em `app/pdfs/` (guia do método, índice visual e os 4 bônus)
- Instalável na tela inicial, fontes locais e funciona com internet fraca

**O que você precisa preencher** (bloco `CONFIG` no começo do script de `app/index.html`):
- `colecoes` → link do PDF de receitas de cada uma das 8 coleções
- `bau` → PDFs do Baú de Natal
- `aulas` → link de cada videoaula (YouTube, Vimeo ou .mp4)
- `suporteWhatsApp` / `suporteEmail`

Link vazio aparece para a aluna como **"Em breve"**.

Para gerar os PDFs de novo depois de mudar o texto: `python3 fonte/pdfs/gerar_pdfs.py`

## Order bumps, upsell e produtos bloqueados

Tudo explicado em `ofertas/ORDER-BUMPS-E-UPSELL.md`: textos prontos para o checkout, capas,
links de liberação (`/app/?libera=gnomos`) e códigos. No app, os extras aparecem com cadeado
na Início, na Coleção, nos Bônus e na tela "Desbloqueie mais".
