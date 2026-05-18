---
title: "RAG (Retrieval-Augmented Generation)"
tipo: concept
dominio: tecnico
tags: [llm, rag, retrieval, embeddings, knowledge-base]
criado: 2026-05-14
atualizado: 2026-05-14
fontes: [tecnico/sources/2026-05-14-llm-wiki-karpathy]
---

# RAG (Retrieval-Augmented Generation)

Padrão de uso de LLMs onde o modelo, ao responder uma query, **recupera chunks relevantes** de uma coleção de documentos e os usa como contexto para gerar a resposta. O conhecimento não é acumulado — é re-derivado das fontes a cada consulta.

---

## Como funciona

1. Documentos são indexados (geralmente com embeddings vetoriais).
2. Para cada query, os chunks mais relevantes são recuperados por similaridade semântica.
3. O LLM recebe a query + os chunks recuperados e gera uma resposta.

---

## Limitações

- **Sem acumulação:** perguntas que exigem síntese de múltiplas fontes forçam redescoberta a cada query.
- **Fragmentação:** o modelo vê pedaços, não a visão integrada.
- **Sem contradições flagadas:** se duas fontes contradizem uma a outra, o sistema não registra isso de forma persistente.
- **Infraestrutura:** requer pipeline de embeddings, vector store, retrieval.

---

## Contraste com [[llm-wiki]]

| RAG | LLM Wiki |
|---|---|
| Re-deriva a cada query | Compila incrementalmente |
| Fragmentos sem contexto | Páginas integradas com cross-refs |
| Infraestrutura vetorial | Só arquivos markdown |
| Contradições re-descobertas | Contradições já sinalizadas |
| Não acumula | Compõe com cada ingest |

RAG é adequado para grandes corpora onde ingest completo é inviável. Para bases de conhecimento pessoais com curadoria ativa, [[llm-wiki]] tende a ser mais eficaz.

---

## Ferramentas comuns

- LangChain, LlamaIndex — frameworks de RAG
- Chroma, Pinecone, Weaviate — vector stores
- OpenAI Embeddings, sentence-transformers — geração de embeddings

> [!note] RAG e LLM Wiki não são mutuamente exclusivos. Em wikis grandes, pode-se usar [[qmd]] (busca BM25/vector local) dentro de um fluxo de LLM Wiki — o melhor dos dois mundos.

---

## Evolução: VRAG

O [[vrag]] (Visual RAG, Alibaba-NLP) estende o RAG para dados visuais: usa [[vlm|VLMs]] para perceber imagens diretamente (em vez de OCR → texto), adiciona raciocínio iterativo agêntico e treino com Reinforcement Learning (VRAG-RL). O processo deixa de ser "recuperar → gerar" e passa a ser "perceber → raciocinar → refinar → gerar".
