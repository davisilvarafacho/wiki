---
title: "VRAG: Como funciona o Visual RAG do Alibaba"
tipo: note
dominio: tecnico
tags: [RAG, VLM, multimodal, VRAG, ai-gerado]
criado: 2026-05-18
atualizado: 2026-05-18
referencia_externa: https://github.com/Alibaba-NLP/VRAG
gerado_por: "Qwen 3.6 Plus (resposta a: 'Como funciona o VRAG proposto pelo Alibaba?')"
---

# VRAG: Como funciona o Visual RAG do Alibaba

Nota derivada de conversa com Qwen 3.6 Plus sobre o repositório [[alibaba-nlp]] `Alibaba-NLP/VRAG`.

---

## O que é VRAG

**VRAG** (Visual Retrieval-Augmented Generation) não é apenas uma variação de sigla do [[rag]] tradicional. É uma arquitetura específica focada em **dados visuais** — imagens, diagramas, PDFs complexos e vídeos. O "V" significa **Visual**.

O RAG tradicional foca predominantemente em texto: recupera trechos de documentos e os entrega ao LLM para gerar uma resposta. O VRAG foi projetado para casos onde a informação não está apenas no texto, mas na estrutura visual, gráficos ou imagens.

---

## Como o VRAG funciona (diferenciais técnicos)

### Percepção visual direta

Em vez de depender apenas de OCR (transformar imagem em texto) e depois fazer RAG, o VRAG usa [[vlm|Modelos de Linguagem Visual (VLMs)]] — como Qwen2.5-VL ou Qwen3-VL — para "olhar" diretamente para as imagens recuperadas.

### Raciocínio iterativo (multi-turn)

O VRAG não tenta responder de uma vez. Age como um **agente**:

1. Faz uma busca inicial ampla (*coarse-grained*).
2. Analisa os resultados visuais.
3. Decide se precisa de mais informações ou de zoom em um detalhe específico (*fine-grained*).
4. Refina a busca ou a interpretação.

### VRAG-RL: Aprendizado por Reforço

O repositório destaca o **VRAG-RL**, que usa Reinforcement Learning para treinar o modelo a decidir:

- *Quando* buscar
- *O que* buscar
- *Como* interpretar a imagem

O RL otimiza o processo de raciocínio passo a passo, em vez de apenas o resultado final.

---

## Comparativo RAG tradicional vs. VRAG

| Característica | RAG Tradicional | VRAG |
| :--- | :--- | :--- |
| Foco de dados | Texto puro | Imagens, PDFs visuais, vídeos, diagramas |
| Motor de recuperação | Busca vetorial de texto | Busca multimodal (embeddings visuais + textuais) |
| Modelo gerador | LLM (texto) | [[vlm\|VLM]] (Vision-Language Model) |
| Processo | Recuperar → Gerar | Perceber → Raciocinar → Refinar → Gerar |
| Complexidade | Baixa/Média | Alta (envolve agentes e RL) |

---

## VimRAG: a evolução do VRAG

O mesmo repositório menciona o **[[vimrag]]**, versão ainda mais avançada que usa um "Grafo de Memória Multimodal" para lidar com contextos visuais massivos, organizando o raciocínio como um grafo dirigido.

---

## Quando usar

O VRAG é indicado quando o problema envolve responder perguntas com base em **gráficos, layouts complexos, fotos ou vídeos**. O RAG tradicional falha nesses casos porque perde a informação visual ao converter tudo para texto. O VRAG mantém a informação visual intacta e usa um agente inteligente para "navegar" por esses dados.
