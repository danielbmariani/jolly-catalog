# Jolly Roger — catálogo e app

App Android de descoberta de filmes e séries com curadoria de **crítica
especializada** (festivais, listas de críticos reconhecidos, cânones de todos
os tempos e recomendações novas todos os dias) — nada de notas de usuário ou
agregadores. Os cards só mostram o que está **realmente disponível** para
assistir, e o clique abre o título direto no app do streaming.

Este repositório publica, todo dia de manhã:

- **Os catálogos** (`*.json`): listas, prêmios, cânones, recomendações de
  críticos e disponibilidade verificada. O app baixa daqui automaticamente a
  cada abertura — as recomendações se renovam sem atualizar o app.
- **O APK** (na aba [Releases](../../releases)): versão de distribuição, sem
  nenhuma chave ou servidor embutido.

## Instalar

1. Baixe o `jolly-roger.apk` da release mais recente e instale (permita
   "instalar de fontes desconhecidas").
2. Abra **Ajustes** (barra de baixo) e configure:
   - **TMDb API Key**: crie uma gratuita em
     [themoviedb.org/settings/api](https://www.themoviedb.org/settings/api)
     (2 minutos — é ela que traz pôsteres e metadados).
   - **País do streaming**: `BR`, `FR`, `GB`… A disponibilidade e os links
     de "assistir" passam a valer para o seu país.
3. Pronto. As abas: **Tudo** (mistura de tudo), **Novidades** (o que críticos
   reconhecidos recomendaram recentemente), **Séries**, **Animação**,
   **Prêmios** (festivais), **Críticos** (listas de fim de ano),
   **Clássicos** (cânones de todos os tempos) e **Estúdios**.

## Opcional: servidor em casa

O app funciona completo sem servidor nenhum. Um servidor caseiro acrescenta
duas coisas:

### 1. Catálogo próprio (em vez deste repositório)

O `catalog-server.py` deste repo é um servidor de arquivos mínimo (Python 3
puro, sem dependências): ele serve uma pasta com os `*.json` na sua rede.

```bash
# na máquina que ficará ligada:
python3 catalog-server.py   # serve ./assets na porta 8099
```

No app: **Ajustes → Catalog server URL** → `http://IP-DA-MÁQUINA:8099`.

### 2. Downloads (qBittorrent)

Se você roda um [qBittorrent](https://www.qbittorrent.org/) com a Web UI
ativa (porta padrão 8080), preencha nos Ajustes:

- **qBittorrent URL**: `http://IP-DA-MÁQUINA:8080`
- **Download path**: pasta de destino na máquina do qBittorrent

A aba **Downloads** e o botão de baixar nos detalhes passam a funcionar.
Sem isso, a aba simplesmente fica vazia — o resto do app não depende dela.

## Privacidade e dados

- O APK publicado não contém chaves, senhas, endereços ou qualquer dado
  pessoal — você fornece a sua própria chave TMDb.
- Os catálogos são metadados públicos de filmes (títulos, ids TMDB/IMDb,
  listas de crítica, provedores de streaming).
- A disponibilidade verificada neste repositório vale para o **Brasil**; em
  outros países o app ignora esses vereditos e consulta ao vivo.
