---
title: "VRAG (Visual Retrieval-Augmented Generation)"
tipo: concept
dominio: tecnico
tags: [RAG, VLM, multimodal, VRAG, agentes, visao-computacional]
criado: 2026-05-18
atualizado: 2026-05-18
fontes: [tecnico/notes/2026-05-18-vrag-alibaba]
---

# VRAG (Visual Retrieval-Augmented Generation)

Extensão do [[rag]] para dados visuais. Proposto pela [[alibaba-nlp]] no repositório `Alibaba-NLP/VRAG`. Em vez de recuperar e processar apenas texto, o VRAG usa [[vlm|VLMs (Vision-Language Models)]] para "olhar" diretamente para imagens, diagramas e vídeos como parte do processo de recuperação e geração.

---

## Diferença central em relação ao RAG tradicional

O RAG tradicional perde informação visual ao converter tudo para texto (via OCR ou descrições). O VRAG preserva a dimensão visual: os modelos enxergam as imagens diretamente.

---

## Componentes principais

- **Busca multimodal:** embeddings visuais + textuais combinados na recuperação.
- **VLM como gerador:** o modelo que gera a resposta entende imagens nativamente.
- **Raciocínio iterativo (agêntico):** busca ampla inicial → análise visual → refinamento fino. Não é uma passagem única — é um loop de percepção e decisão.
- **VRAG-RL:** variante treinada com Reinforcement Learning para otimizar *quando*, *o que* e *como* recuperar. O RL treina a política de busca, não apenas a geração.

---

## Casos de uso

- Responder perguntas sobre gráficos e infográficos
- Análise de PDFs com layout complexo (tabelas, diagramas)
- Consultas sobre imagens técnicas (plantas, esquemas, screenshots)
- Raciocínio sobre frames de vídeo

---

## Variante avançada

[[vimrag]] — usa um Grafo de Memória Multimodal para contextos visuais massivos; organiza o raciocínio como grafo dirigido em vez de lista linear de chunks.

---

## Ver também

- [[rag]] — o padrão base que o VRAG estende
- [[vlm]] — os modelos visuais que tornam o VRAG possível
- [[alibaba-nlp]] — organização autora do repositório
