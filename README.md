# Amigurumis Natalinos de Luxo — Página de vendas (BR 2026)

Página de vendas estática, em português, pronta para hospedar (GitHub Pages, Vercel, Netlify ou qualquer hospedagem).

## Estrutura

```
index.html      → a página de vendas (HTML + CSS + JS num único arquivo)
app/            → o mini app de entregáveis (área da aluna, sem login)
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
O progresso dela (passos do método, calendário, coleções favoritas, calculadora) fica salvo no próprio celular.

**Para liberar os arquivos**, abra `app/index.html` e edite só o bloco `CONFIG` no começo do script:

- `colecoes` → link do PDF de cada uma das 8 coleções de receitas
- `indiceVisualPdf`, `metodoPdf`, `bau`, `bonusPdf` → links dos demais PDFs
- `aulas` → link de cada videoaula (YouTube, Vimeo ou .mp4)
- `suporteWhatsApp` / `suporteEmail` → contato de suporte

Link vazio aparece para a aluna como **"Em breve"**.
Os bônus Código Amigurumi™, Paletas, Calculadora de Preço Justo e Mensagens prontas já funcionam dentro do app.

Coloque o link do app na página de obrigado e no e-mail de acesso da sua plataforma de pagamento.
