# Order bumps, upsell e downsell — Amigurumis Natalinos de Luxo

Textos prontos para colar no checkout (Kiwify, Hotmart, Eduzz, Perfect Pay…).
As capas estão em `ofertas/capas/` (800×800, PNG).

Os bumps 1 e 2 seguem a mesma ideia e estrutura do checkout oficial (que roda com 2 bumps a R$27).
Como o Front-End agora custa **R$19,90**, todos os bumps foram reprecificados para ficar abaixo do produto principal.
Os bumps 3 e 4 são novos.

---

## Estrutura de cada bump (igual à oficial)

```
[selo]      🎄 OFERTA ÚNICA · SÓ NESTA PÁGINA
[título]    SIM! Adicione as <Produto> por apenas R$XX
[subtítulo] <benefício em uma linha>
[texto]     <descrição curta + "Disponível só nesta página.">
[preço]     De R$XX  →  R$XX   (-XX%)   Você economiza R$XX
```

---

## Bump 1 — Espirais Natalinas Penduráveis · R$14,90  *(do original)*

- **Selo:** 🎄 OFERTA ÚNICA · SÓ NESTA PÁGINA
- **Título:** SIM! Adicione as **Espirais Natalinas Penduráveis** por apenas R$14,90
- **Subtítulo:** Peças rápidas que vendem em packs para a árvore
- **Texto:** Enfeites de amigurumi em espiral para pendurar na árvore: Papai Noel, bonecos de neve, pinguim, arvorezinhas, anjos, gnomo e mais. Rápidos de crochetar, vendem muito bem em packs e ficam lindos pendurados juntos. Disponível só nesta página.
- **Preço:** De R$104,69 → **R$14,90** (-86%) · Você economiza R$89,79
- **Capa:** `ofertas/capas/espirais.png`

> ⚠️ No original, as receitas desse bump estão **em inglês** e a página avisa isso
> ("use o Código Amigurumi™ para ler sem problema"). Se o seu material também estiver em inglês,
> acrescente essa frase ao texto. Não venda como "em português" se não for.

## Bump 2 — 24 Gnomos Natalinos · R$14,90  *(do original)*

- **Selo:** 🎁 OFERTA ÚNICA · SÓ NESTA PÁGINA
- **Título:** SIM! Adicione os **24 Gnomos Natalinos** por apenas R$14,90
- **Subtítulo:** Os queridinhos do Natal, rápidos de crochetar e perfeitos para presentear em set
- **Texto:** 24 modelos de gnomos natalinos em crochê, com gorro comprido e barba fofinha. São peças pequenas e rápidas, que aproveitam sobras de linha e ficam lindas em grupo: na mesa, pendurados na árvore ou em kits de presente. Disponível só nesta página.
- **Preço:** De R$82,65 → **R$14,90** (-82%) · Você economiza R$67,75
- **Capa:** `ofertas/capas/gnomos.png`

## Bump 3 — Presépio & Anjinhos de Crochê · R$12,90  *(novo)*

- **Selo:** ⭐ OFERTA ÚNICA · SÓ NESTA PÁGINA
- **Título:** SIM! Adicione o **Presépio & Anjinhos de Crochê** por apenas R$12,90
- **Subtítulo:** O centro da mesa de Natal, feito por você
- **Texto:** Receitas de amigurumi para montar o presépio completo: Sagrada Família, Reis Magos, pastor, animais da manjedoura e anjinhos. Uma peça de muito valor afetivo, que as famílias guardam por anos e encomendam com antecedência. Disponível só nesta página.
- **Preço:** De R$64,00 → **R$12,90** (-80%) · Você economiza R$51,10
- **Capa:** `ofertas/capas/presepio.png`

## Bump 4 — Etiquetas & Embalagens Natalinas · R$9,90  *(novo — arquivo já pronto)*

- **Selo:** 🎀 OFERTA ÚNICA · SÓ NESTA PÁGINA
- **Título:** SIM! Adicione as **Etiquetas & Embalagens Natalinas** por apenas R$9,90
- **Subtítulo:** Entregue seus amigurumis com acabamento de loja
- **Texto:** Tags, cartões de agradecimento e adesivos natalinos para imprimir em casa. É o detalhe que transforma o seu amigurumi em presente — e faz a cliente lembrar do seu nome. Disponível só nesta página.
- **Preço:** De R$49,90 → **R$9,90** (-80%) · Você economiza R$40,00
- **Capa:** `ofertas/capas/etiquetas.png`
- **Arquivo:** `app/pdfs/extras/etiquetas-embalagens-natalinas.pdf` (já gerado)

**Sugestão de ordem no checkout:** Gnomos → Espirais → Etiquetas → Presépio.
Os dois do original primeiro (já validados); depois o mais barato, que tem a decisão mais fácil.

---

## Upsell (página `upsell/`) — Amigurumis o Ano Inteiro · R$47

O checkout oficial não mostra o upsell antes da compra, então este foi criado do zero, no mesmo visual.

- **Promessa:** continuar vendendo depois do Natal, com uma coleção para cada data do ano.
- **Entrega:** 12 coleções sazonais + calendário anual de vendas, liberadas no mesmo app.
- **Preço:** De R$197 → **R$47**
- **Recusou →** **Downsell** na mesma página: versão Essencial (Páscoa, Dia das Mães, Chá de bebê, Dia das Crianças) · De R$97 → **R$27**
- **Recusou de novo →** vai para o app.

Configure os links no bloco `UPSELL` no fim de `upsell/index.html`
(use o link de **compra com 1 clique** da sua plataforma).

---

## Como o app libera os extras

Cada extra aparece **bloqueado** no app (com cadeado e botão "Desbloquear").
Configure no bloco `CONFIG.extras` de `app/index.html`:

| Produto | `checkout` | `codigo` padrão | Link de acesso que libera |
|---|---|---|---|
| Espirais | link de compra avulsa | `ESPIRAL27` | `https://amigurumi-natal-luxo-br-app.vercel.app/?libera=espirais` |
| Gnomos | link de compra avulsa | `GNOMOS27` | `https://amigurumi-natal-luxo-br-app.vercel.app/?libera=gnomos` |
| Presépio | link de compra avulsa | `PRESEPIO19` | `https://amigurumi-natal-luxo-br-app.vercel.app/?libera=presepio` |
| Etiquetas | link de compra avulsa | `ETIQUETAS17` | `https://amigurumi-natal-luxo-br-app.vercel.app/?libera=etiquetas` |
| Ano Inteiro | link do upsell | `ANOINTEIRO` | `https://amigurumi-natal-luxo-br-app.vercel.app/?libera=anointeiro` |

Na plataforma, cadastre como **link de entrega** de cada bump o endereço com `?libera=`.
Quem comprar o bump e abrir esse link já entra com o conteúdo liberado.
Também dá para mandar o **código** no e-mail: a cliente digita em "Já comprei".

> Lembrete: sem login, quem tiver o link ou o código consegue liberar.
> Troque os códigos padrão antes de publicar. Para escalar com segurança, o ideal é migrar para uma área de membros com login.
