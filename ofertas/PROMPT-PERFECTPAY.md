# Prompt para a extensão do Claude: configurar a esteira na PerfectPay

Antes de colar:
1. Baixe o pacote de imagens (`imagens-perfectpay.zip`) e descompacte numa pasta do computador.
2. Abra a PerfectPay já logado e cole o prompt abaixo na extensão.

```
Você vai configurar na PerfectPay (já estou logado, na página da plataforma) toda a
esteira do meu infoproduto de receitas de crochê "Amigurumis Natalinos de Luxo".
Trabalhe em ordem, um produto por vez, e no fim me entregue o relatório pedido no
item 7. Se a interface da PerfectPay tiver nomes diferentes dos que uso aqui,
procure a opção equivalente nos menus (Produtos, Planos/Ofertas, Checkout,
Order Bump, Upsell/Funil, Configurações) antes de concluir que não existe.

## 0. Regras
- Já autorizo: criar e salvar os 7 produtos abaixo, seus planos/preços, o checkout,
  os order bumps e o funil de upsell/downsell exatamente como descrito.
- NÃO mexa em: dados bancários, conta de saque, CPF/CNPJ da conta, senha, taxas,
  integrações já existentes, nem aceite termos novos. Se aparecer algo assim, pare
  e me pergunte.
- Imagens: quando um campo pedir upload, me diga o NOME DO ARQUIVO (lista no item 6)
  e espere eu anexar. Não use imagens da internet.
- Prova social só com dados reais: não crie notificações de compra, nomes de
  compradores ou depoimentos fictícios. Se a ferramenta de notificações gerar nomes
  inventados, deixe-a DESLIGADA.
- Antes de cada clique em "Salvar"/"Publicar", confira preço, nome e link de entrega.

## 1. Produtos (todos: produto digital, pagamento único, idioma português,
##    categoria Artesanato/Hobbies ou a mais próxima, garantia de 7 dias,
##    e-mail de suporte = o já cadastrado na conta)

P1 — FRONT-END
- Nome: Amigurumis Natalinos de Luxo — Receitas de Crochê
- Preço: R$ 19,90
- Descrição: Coleção digital de receitas de crochê (amigurumi) de Natal, passo a
  passo, carreira por carreira, com índice visual, método Vitrine de Natal,
  videoaulas e 4 bônus. Acesso imediato pelo celular. Não é produto físico e não
  são receitas culinárias.
- Imagem: 01-capa-amigurumis-natalinos-de-luxo.png
- Entrega / link de acesso: https://amigurumi-natal-luxo-br-app.vercel.app/

P2 — ORDER BUMP: 24 Gnomos Natalinos
- Preço: R$ 14,90 (de R$ 82,65)
- Descrição: 24 receitas de crochê de gnomos natalinos, rápidas de fazer e
  perfeitas para presentear em set.
- Imagem: 04-bump-gnomos.png
- Entrega: https://amigurumi-natal-luxo-br-app.vercel.app/?libera=gnomos

P3 — ORDER BUMP: Espirais Natalinas Penduráveis
- Preço: R$ 14,90 (de R$ 104,69)
- Descrição: Receitas de crochê de enfeites em espiral para pendurar na árvore:
  Papai Noel, bonecos de neve, pinguim, árvores, anjos e gnomo.
- Imagem: 05-bump-espirais.png
- Entrega: https://amigurumi-natal-luxo-br-app.vercel.app/?libera=espirais

P4 — ORDER BUMP: Etiquetas & Embalagens Natalinas
- Preço: R$ 9,90 (de R$ 49,90)
- Descrição: Tags, cartões de agradecimento e adesivos natalinos em PDF para
  imprimir e entregar os amigurumis com acabamento de loja.
- Imagem: 06-bump-etiquetas.png
- Entrega: https://amigurumi-natal-luxo-br-app.vercel.app/?libera=etiquetas

P5 — ORDER BUMP: Presépio & Anjinhos de Crochê
- Preço: R$ 12,90 (de R$ 64,00)
- Descrição: Receitas de crochê para montar o presépio completo: Sagrada Família,
  Reis Magos, pastor, animais e anjinhos.
- Imagem: 07-bump-presepio.png
- Entrega: https://amigurumi-natal-luxo-br-app.vercel.app/?libera=presepio

P6 — UPSELL: Amigurumis o Ano Inteiro
- Preço: R$ 47,00 (de R$ 197,00)
- Descrição: 12 coleções sazonais de receitas de crochê (Páscoa, Dia das Mães,
  festa junina, Dia dos Pais, chá de bebê, Dia das Crianças e mais) + calendário
  anual de vendas.
- Imagem: 08-upsell-ano-inteiro.png
- Entrega: https://amigurumi-natal-luxo-br-app.vercel.app/?libera=anointeiro

P7 — DOWNSELL: Amigurumis Essencial
- Preço: R$ 27,00 (de R$ 97,00)
- Descrição: 4 coleções de receitas de crochê para Páscoa, Dia das Mães, chá de
  bebê e Dia das Crianças.
- Imagem: 09-downsell-essencial.png
- Entrega: https://amigurumi-natal-luxo-br-app.vercel.app/?libera=essencial

## 2. Pagamento (em TODOS os produtos/planos)
- Habilite SOMENTE Pix e Cartão de crédito. Desative boleto, PicPay, Nubank,
  carteiras digitais e qualquer outra forma.
- Pix como forma PRINCIPAL e pré-selecionada no checkout.
- Se existir "desconto no Pix", aplique 2%.
- Cartão: parcelamento no padrão da plataforma, com juros pagos pelo comprador
  (não assuma juros por minha conta). Não altere taxas.

## 3. Checkout do P1 (Front-End)
- Fundo BRANCO, layout limpo, cor do botão: vermelho #B3263A (texto branco);
  cor de destaque: verde #2F6B4F.
- Banner do topo: desktop = 02-banner-checkout-desktop.png (1200×300);
  mobile = 03-banner-checkout-mobile.png (800×400). Se a plataforma pedir outro
  tamanho, me avise o tamanho exato antes de subir.
- NÃO coloque selo de garantia nem mockup no topo (o banner já faz o papel).
- Campos: só e-mail e telefone/WhatsApp. Desligue nome e CPF se a plataforma
  permitir. Se o CPF for obrigatório para o Pix, mantenha e me avise.
- Texto do botão (se editável): "Gerar Pix e receber o acesso".
- Cronômetro: só ative se, ao zerar, o desconto do Pix realmente deixar de valer.
  Se for apenas visual (reinicia a cada visita), deixe DESLIGADO. Se ativar: texto
  "Promoção no Pix encerra em:" e tempo 7:36 (nunca número redondo).
- Popup/oferta de saída: se existir, cupom de 3% com o texto
  "Espera! Você ganhou 3% de desconto" e botão "Quero meu desconto".
- Recuperação de carrinho/abandono: ative a automática da plataforma (e-mail e,
  se houver, WhatsApp/SMS) com a mensagem:
  "Oi! Vi que você começou a garantir os Amigurumis Natalinos de Luxo e não
  finalizou. Seu acesso às receitas de crochê de Natal ainda está reservado por
  R$ 19,90 — é só concluir o Pix por aqui: [link do checkout]"
- Página de obrigado / redirecionamento após compra aprovada:
  https://amigurumi-natal-luxo-br.vercel.app/upsell/

## 4. Order bumps no checkout do P1 (nesta ordem)
Se a plataforma tiver opção de o bump aparecer só depois que a pessoa digita o
e-mail, ative. Use para cada um:
- Selo/tag: RECOMENDADO
- Título: SIM! Adicione [nome do produto] por apenas R$ [preço]
- Texto (máx. 2 linhas): o benefício abaixo + "Disponível só nesta página."
1) P2 Gnomos — "Os queridinhos do Natal, rápidos de crochetar e perfeitos para
   presentear em set."
2) P3 Espirais — "Peças rápidas que vendem em packs para a árvore."
3) P4 Etiquetas — "Entregue seus amigurumis com acabamento de loja."
4) P5 Presépio — "O centro da mesa de Natal, feito por você."
Mostre o "de/por" (preço riscado) se o campo existir.

## 5. Upsell e downsell (funil pós-compra)
- Crie o funil: compra aprovada do P1 → página https://amigurumi-natal-luxo-br.vercel.app/upsell/
  (oferta P6, compra com 1 clique) → se recusar, mesma página mostra P7.
- Gere o link/script de "compra com 1 clique" do P6 e do P7 (aceitar) e me passe
  também o link de recusa, se a plataforma usar.
- Se a PerfectPay exigir o script de upsell colado na página, NÃO tente editar o
  meu site: só copie o código e me entregue no relatório.

## 6. Arquivos de imagem (vou anexar quando você pedir)
01-capa-amigurumis-natalinos-de-luxo.png · 02-banner-checkout-desktop.png ·
03-banner-checkout-mobile.png · 04-bump-gnomos.png · 05-bump-espirais.png ·
06-bump-etiquetas.png · 07-bump-presepio.png · 08-upsell-ano-inteiro.png ·
09-downsell-essencial.png

## 7. Relatório final (me entregue nesta forma)
- Tabela: Produto | ID na PerfectPay | Preço | Link do checkout | Link de entrega
  configurado | Formas de pagamento ativas
- Link/script de compra com 1 clique do upsell (P6) e do downsell (P7) + link de
  recusa.
- Lista do que NÃO foi possível configurar (ex.: CPF obrigatório, sem desconto no
  Pix, bump não dinâmico, tamanho de banner diferente) e o motivo.
- Faça 1 teste visual: abra o link do checkout do P1 no modo celular e confirme
  banner, Pix pré-selecionado, só Pix + cartão e os 4 bumps. Não finalize compra.
```

Depois que a extensão terminar, me mande o relatório: eu coloco o link do checkout
na página de vendas (`CHECKOUT`) e os links de 1 clique no `upsell/index.html`.
