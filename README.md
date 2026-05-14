# Wiki Pessoal

Base de conhecimento pessoal mantida com LLM, seguindo o padrão de [llm-wiki.md (Karpathy)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Como usar

Abra esta pasta em dois lugares ao mesmo tempo:

1. **Claude Code** (ou agente equivalente) — apontando para esta pasta. O agente lê `CLAUDE.md` automaticamente e segue o schema.
2. **Obsidian** — abra esta pasta como vault. Use o **graph view** pra ver a forma da wiki crescer. Os `[[links]]` funcionam direto.

## Fluxos básicos

### Ingerir uma fonte (arquivo)

```
Coloque o arquivo em raw/<dominio>/
Diga ao Claude: "ingest raw/tecnico/artigo-x.pdf"
```

### Ingerir conteúdo conversacional (colar no chat)

```
Cole o texto/link no chat.
Diga: "ingest isso no domínio <dominio>"
```

### Fazer uma pergunta

```
"O que eu já registrei sobre <tópico>?"
"Como conecto X e Y dentro da minha wiki?"
"Resuma o que eu sei sobre <conceito>"
```

Se a resposta for boa, peça pra arquivar como página de síntese.

### Lint (auditoria periódica)

A cada algumas semanas:

```
"Faz lint da wiki, por favor"
```

### Adicionar novo domínio

```
"Quero começar um domínio novo de <assunto>"
```

O Claude cria a estrutura sozinho.

## Estrutura

- **6 domínios atuais:** `tecnico/`, `pessoal/`, `espiritual/`, `estudos/`, `empresarial/`, `rafacho.dev/`
- **Camada `_meta/`** — índice global, log, conexões cross-domain, glossário, perguntas abertas
- **`raw/`** — fontes brutas (imutáveis, espelhando os domínios)
- **`CLAUDE.md`** — o cérebro: schema que o agente lê em toda sessão

Cada domínio tem internamente: `concepts/`, `entities/`, `sources/`, `notes/`, `synthesis/`.

## Versionamento

Inicialize um repo git aqui. Tudo é markdown — histórico de Git já dá histórico de versões da wiki inteira de graça.

```bash
git init
git add .
git commit -m "wiki inicial"
```

## Notas pessoais

- Mantenha o ritmo. Mesmo ingerir 1 fonte por semana já compõe ao longo dos meses.
- A `synthesis/` é onde mora o valor real. Volte nela. Edite. Discorde de você mesmo.
- O `_meta/connections.md` é onde a mágica acontece — conexões inesperadas entre técnica e teologia, pessoal e negócio. Vale a pena ler de tempos em tempos.
