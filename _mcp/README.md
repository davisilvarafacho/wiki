# _mcp — MCP read-only da wiki (second brain)

MCP **somente-leitura** para a sua wiki pessoal (second brain), modelado em
torno do schema descrito no `CLAUDE.md` do repo `wiki` (padrão Karpathy:
domínios com `concepts/`, `entities/`, `sources/`, `notes/`, `synthesis/` +
camada `_meta/`).

Roda localmente via **stdio** — sem servidor exposto na rede, sem auth,
sem escrita. Qualquer cliente MCP (Claude Desktop, Claude Code, etc.) aciona
o processo Python diretamente.

## Tools disponíveis

| Tool | O que faz |
|---|---|
| `wiki_get_meta_index` | Lê `_meta/index.md` (catálogo global — ponto de partida) |
| `wiki_get_connections` | Lê `_meta/connections.md` (conexões cross-domain) |
| `wiki_get_glossary` | Lê `_meta/glossary.md` |
| `wiki_get_open_questions` | Lê `_meta/open-questions.md` |
| `wiki_recent_log` | Últimas N entradas de `_meta/log.md` |
| `wiki_list_domains` | Lista domínios existentes + prévia do `_index.md` de cada um |
| `wiki_list_domain` | Árvore de páginas de um domínio específico |
| `wiki_read_page` | Lê uma página (frontmatter parseado + corpo) |
| `wiki_search` | Busca por substring em título/tags/corpo, com filtro de domínio e tipo |
| `wiki_semantic_search` | Busca semântica (por significado) — requer índice pré-construído |

Todos os paths são validados contra path traversal — só é possível ler
arquivos dentro de `WIKI_PATH`.

## Instalação

Requer Python ≥3.11. Este código mora dentro do próprio repo `wiki`, na
pasta `_mcp/` — `WIKI_PATH` deve apontar para a **raiz do repo** (um nível
acima de `_mcp/`), não para essa pasta.

```bash
cd wiki/_mcp
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Testar com o MCP Inspector

```bash
WIKI_PATH=~/wiki npx @modelcontextprotocol/inspector \
  .venv/bin/python -m wiki_mcp.server
```

Abre uma UI local onde dá pra chamar cada tool manualmente e conferir o
retorno antes de plugar num cliente de verdade.

## Registrar no Claude Desktop

Edite `claude_desktop_config.json` (macOS: `~/Library/Application Support/Claude/`,
Linux/outros: local equivalente) e adicione:

```json
{
  "mcpServers": {
    "wiki-second-brain": {
      "command": "/caminho/absoluto/para/wiki/_mcp/.venv/bin/python",
      "args": ["-m", "wiki_mcp.server"],
      "env": {
        "WIKI_PATH": "/caminho/absoluto/para/wiki"
      }
    }
  }
}
```

Reinicie o Claude Desktop. O tool `wiki_get_meta_index` deve aparecer na
lista de tools disponíveis na conversa.

## Registrar no Claude Code

```bash
claude mcp add wiki-second-brain \
  --env WIKI_PATH=/caminho/absoluto/para/wiki \
  -- /caminho/absoluto/para/wiki/_mcp/.venv/bin/python -m wiki_mcp.server
```

## Busca semântica

Além do `wiki_search` (substring literal), há `wiki_semantic_search`, que
busca por **significado** — útil quando você lembra vagamente do que
pensou sobre algo mas não do termo exato usado na página.

Funciona com embeddings locais via [fastembed](https://github.com/qdrant/fastembed)
(ONNX, sem torch, roda em CPU), modelo
`paraphrase-multilingual-MiniLM-L12-v2` — bom pra português e leve o
suficiente pro tamanho atual da wiki (índice de ~600 chunks leva
~50s pra construir do zero).

### Construir o índice

```bash
source .venv/bin/activate
pip install -e .   # já inclui fastembed e numpy agora

WIKI_PATH=~/wiki INDEX_PATH=~/.wiki-mcp-index python -m wiki_mcp.index_build
```

Isso cria `~/.wiki-mcp-index/embeddings.npy` + `metadata.json`. Se você
não passar `INDEX_PATH`, o default já é `~/.wiki-mcp-index`.

### Reindexar

O índice **não** se atualiza sozinho — é um build offline. Sempre que você
fizer um `ingest` (Claude Code alterando páginas da wiki), rode o comando
acima de novo. Para automatizar, dá pra criar um hook de `post-commit` no
repo do `wiki` que dispara o `index_build`, ou simplesmente lembrar de
rodar manualmente depois de sessões de ingest.

### Como funciona por baixo

Cada página é dividida em chunks por seção (`## heading`); páginas sem
subseções viram um chunk único. Cada chunk vira um vetor de 384 dimensões.
Na hora da busca, a query também vira vetor e comparamos por similaridade
de cosseno contra todos os chunks — sem banco vetorial, é só `numpy`, o que
é suficiente pro volume atual. Se a wiki crescer para milhares de páginas,
vale migrar para algo como `sqlite-vec` ou `faiss`, mas a interface do tool
(`wiki_semantic_search`) não precisa mudar.

### `INDEX_PATH` no registro do cliente

Se você definir `INDEX_PATH` custom, lembre de passar a mesma env var no
registro do MCP (Claude Desktop / Claude Code), igual ao `WIKI_PATH`.



- **Somente leitura de propósito.** Não há tool de escrita — ingest e
  manutenção continuam pelo fluxo normal com Claude Code lendo `CLAUDE.md`
  diretamente no repo. Isso evita ter duas rotas de escrita divergentes
  (uma seguindo o schema completo do CLAUDE.md, outra simplificada no MCP).
- **`wiki_search` é busca por substring, `wiki_semantic_search` é por
  significado.** Os dois coexistem de propósito: substring é instantâneo e
  exato (bom pra achar um arquivo/entidade por nome); semântica é mais lenta
  pra indexar mas encontra o que você quis dizer, não só o que você digitou.
- **Domínios são detectados dinamicamente** (qualquer pasta com `_index.md`
  na raiz) — não há lista hardcoded, então novos domínios que você criar
  aparecem automaticamente sem precisar tocar no server.
