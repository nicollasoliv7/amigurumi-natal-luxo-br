# Amigurumis Natalinos de Luxo — Página de vendas (BR 2026)

Página de vendas estática, em português, pronta para hospedar (GitHub Pages, Vercel, Netlify ou qualquer hospedagem).

## Estrutura

```
index.html      → a página (HTML + CSS + JS num único arquivo)
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
