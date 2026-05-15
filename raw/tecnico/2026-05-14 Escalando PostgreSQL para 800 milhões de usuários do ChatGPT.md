---
title: "Escalando PostgreSQL para 800 milhões de usuários do ChatGPT"
tipo: "source"
dominio: "tecnico"
tipo_fonte: "blog-post"
url: "https://openai.com/pt-BR/index/scaling-postgresql/?ref=dailydev"
autor:
publicado: 2026-05-13
capturado: 2026-05-14
tags:
---
Durante anos, o PostgreSQL tem sido um dos sistemas de dados mais críticos e essenciais para o funcionamento de produtos fundamentais como o ChatGPT e a API da OpenAI. Com o rápido crescimento da nossa base de usuários, a demanda sobre nossos bancos de dados também aumentou exponencialmente. No último ano, nossa carga do PostgreSQL cresceu mais de 10 vezes, e continua a aumentar rapidamente.

Nossos esforços para aprimorar nossa infraestrutura de produção e sustentar esse crescimento revelaram uma nova descoberta: o PostgreSQL pode ser dimensionado para suportar de forma confiável cargas de trabalho com grande volume de leitura muito maiores do que muitos imaginavam ser possível. O sistema (inicialmente criado por uma equipe de cientistas da Universidade da Califórnia, Berkeley) nos permitiu suportar um tráfego global massivo com uma única [instância primária do servidor Azure PostgreSQL Flexible ⁠](https://learn.microsoft.com/en-us/azure/postgresql/overview) e quase 50 réplicas de leitura distribuídas por várias regiões do mundo. Esta é a história de como escalamos o PostgreSQL na OpenAI para suportar milhões de consultas por segundo para 800 milhões de usuários por meio de otimizações rigorosas e engenharia sólida; também abordaremos os principais aprendizados que tivemos ao longo do caminho.

## Fissuras no nosso design inicial

Após o lançamento do ChatGPT, o tráfego cresceu em um ritmo sem precedentes. Para dar suporte a isso, implementamos rapidamente otimizações extensivas tanto na camada de aplicação quanto na camada de banco de dados PostgreSQL, escalamos verticalmente aumentando o tamanho da instância e escalamos horizontalmente adicionando mais réplicas de leitura. Essa arquitetura nos serviu bem por muito tempo. Com as melhorias contínuas, continua a oferecer amplo espaço para o crescimento futuro.

Pode parecer surpreendente que uma arquitetura com um único núcleo primário consiga atender às demandas de escala da OpenAI; no entanto, fazer isso funcionar na prática não é simples. Já vimos vários erros de status (SEVs) causados por sobrecarga do Postgres, e eles geralmente seguem o mesmo padrão: um problema upstream causa um pico repentino na carga do banco de dados, como falhas generalizadas de cache devido a uma falha na camada de cache, uma onda de junções complexas e dispendiosas saturando a CPU ou uma tempestade de escrita devido ao lançamento de um novo recurso. À medida que a utilização de recursos aumenta, a latência das consultas também aumenta e as solicitações começam a expirar. As novas tentativas amplificam ainda mais a carga, desencadeando um ciclo vicioso com potencial para degradar todos os serviços do ChatGPT e da API.

![Diagrama de carga de escala](https://images.ctfassets.net/kftzwdyauwt9/5nYb6pypN6lSij8qF4AeLs/8e5676eaa6b4156134e25911709abf1f/OAI_The_Vicious_Cycle_Under_Load__Dark_Desktop_.svg?w=3840&q=80)

Diagrama de carga de escala

Embora o PostgreSQL seja escalável para nossas cargas de trabalho com grande volume de leitura, ainda encontramos desafios durante períodos de alto tráfego de escrita. Isso se deve em grande parte à implementação do controle de concorrência multiversão (MVCC) do PostgreSQL, que o torna menos eficiente para cargas de trabalho com grande volume de escrita. Por exemplo, quando uma consulta atualiza uma tupla ou mesmo um único campo, a linha inteira é copiada para criar uma nova versão. Sob cargas de escrita elevadas, isso resulta em uma amplificação de escrita significativa. Isso também aumenta a amplificação de leitura, já que as consultas precisam examinar várias versões de tuplas (tuplas mortas) para recuperar a mais recente. O MVCC introduz desafios adicionais, como o inchaço de tabelas e índices, o aumento da sobrecarga de manutenção de índices e o ajuste complexo do autovacuum. (Você pode encontrar uma análise aprofundada dessas questões em um blog que escrevi com o Prof. Andy Pavlo da Universidade Carnegie Mellon, intitulado [*"A parte do PostgreSQL que mais odiamos"* ⁠](https://www.cs.cmu.edu/~pavlo/blog/2023/04/the-part-of-postgresql-we-hate-the-most.html), [citado ⁠](https://en.wikipedia.org/wiki/PostgreSQL#cite_note-37) na página da Wikipédia sobre o PostgreSQL.)

## Escalando o PostgreSQL para milhões de QPS

Para mitigar essas limitações e reduzir a pressão de escrita, migramos, e continuamos a migrar, para o particionamento (ou seja, para um modelo fragmentado). cargas de trabalho que podem ser particionadas horizontalmente), cargas de trabalho com uso intensivo de gravação em sistemas fragmentados, como o Azure Cosmos DB, otimizando a lógica do aplicativo para minimizar gravações desnecessárias. Também não permitimos mais a adição de novas tabelas à implementação atual do PostgreSQL. As novas cargas de trabalho são direcionadas por padrão para os sistemas fragmentados.

Mesmo com a evolução da nossa infraestrutura, o PostgreSQL permaneceu sem particionamento, com uma única instância primária atendendo a todas as gravações. A principal justificativa é que o particionamento das cargas de trabalho de aplicativos existentes seria extremamente complexo e demorado, exigindo alterações em centenas de endpoints de aplicativos e podendo levar meses ou até anos. Como nossas cargas de trabalho são predominantemente de leitura e implementamos otimizações extensivas, a arquitetura atual ainda oferece ampla margem para suportar o crescimento contínuo do tráfego. Embora não descartemos a possibilidade de fragmentar o PostgreSQL no futuro, isso não é uma prioridade a curto prazo, dada a margem de manobra suficiente que temos para o crescimento atual e futuro.

Nas seções seguintes, vamos analisar os desafios que enfrentamos e as extensas otimizações que implementamos para resolvê-los e evitar futuras interrupções, levando o PostgreSQL ao seu limite e escalando-o para milhões de consultas por segundo (QPS).

#### Reduzir a carga no primário

*Desafio: Com apenas um gravador, uma configuração com um único servidor primário não consegue escalar as gravações. Picos de escrita intensos podem sobrecarregar rapidamente o servidor principal e afetar serviços como o ChatGPT e nossa API.*

Solução: Minimizamos ao máximo a carga no servidor primário — tanto de leitura quanto de gravação — para garantir que ele tenha capacidade suficiente para lidar com picos de gravação. O tráfego de leitura é descarregado para réplicas sempre que possível. No entanto, algumas consultas de leitura devem permanecer no servidor primário porque fazem parte de transações de gravação. Para esses casos, nosso foco é garantir que sejam eficientes e evitar consultas lentas. Para tráfego de gravação, migramos cargas de trabalho fragmentadas e com grande volume de gravação para sistemas fragmentados, como o Azure Cosmos DB. Cargas de trabalho mais difíceis de fragmentar, mas que ainda geram um alto volume de gravações, levam mais tempo para serem migradas, e esse processo ainda está em andamento. Também otimizamos agressivamente nossos aplicativos para reduzir a carga de gravação; por exemplo, corrigimos bugs nos aplicativos que causavam gravações redundantes e introduzimos gravações assíncronas, quando apropriado, para suavizar picos de tráfego. Além disso, ao preencher campos de tabelas com dados já preenchidos, impomos limites de taxa rigorosos para evitar pressão excessiva de escrita.

#### Otimização de consultas

*Desafio: Identificamos diversas consultas dispendiosas no PostgreSQL. No passado, picos repentinos no volume dessas consultas consumiam grandes quantidades de CPU, tornando as solicitações do ChatGPT e da API mais lentas.*

Solução: Algumas consultas dispendiosas, como aquelas que unem muitas tabelas, podem degradar significativamente ou até mesmo derrubar todo o serviço. Precisamos otimizar continuamente as consultas do PostgreSQL para garantir sua eficiência e evitar antipadrões comuns de Processamento de Transações Online (OLTP). Por exemplo, certa vez identificamos uma consulta extremamente custosa que unia 12 tabelas, onde picos nessa consulta foram responsáveis por alertas de vulnerabilidade grave (SEVs) anteriores. Devemos evitar junções complexas entre várias tabelas sempre que possível. Se forem necessárias junções, aprendemos a considerar a possibilidade de dividir a consulta e mover a lógica complexa de junção para a camada de aplicação. Muitas dessas consultas problemáticas são geradas por frameworks de Mapeamento Objeto-Relacional (ORMs), portanto, é importante revisar cuidadosamente o SQL que eles produzem e garantir que ele se comporte conforme o esperado. Também é comum encontrar consultas ociosas de longa duração no PostgreSQL. Configurar tempos limite como idle\_in\_transaction\_session\_timeout é essencial para evitar que eles bloqueiem o autovacuum.

#### Mitigação de ponto único de falha

*Desafio: Se uma réplica de leitura falhar, o tráfego ainda poderá ser encaminhado para outras réplicas. No entanto, depender de um único redator significa ter um único ponto de falha — se ele falhar, todo o serviço será afetado.*

Solução: A maioria das solicitações críticas envolve apenas consultas de leitura. Para mitigar o ponto único de falha no servidor primário, transferimos essas leituras do servidor de gravação para as réplicas, garantindo que essas solicitações possam continuar sendo atendidas mesmo se o servidor primário ficar inativo. Embora as operações de escrita ainda falhem, o impacto é reduzido; não é mais um erro SEV0, já que as leituras permanecem disponíveis.

Para mitigar falhas no servidor primário, executamos o servidor primário em modo de Alta Disponibilidade (HA) com um servidor de espera ativa, uma réplica continuamente sincronizada que está sempre pronta para assumir o atendimento do tráfego. Se o servidor principal falhar ou precisar ser desativado para manutenção, podemos acionar rapidamente o servidor de reserva para minimizar o tempo de inatividade. A equipe do Azure PostgreSQL realizou um trabalho significativo para garantir que esses failovers permaneçam seguros e confiáveis, mesmo sob cargas muito altas. Para lidar com falhas nas réplicas de leitura, implantamos várias réplicas em cada região com capacidade suficiente, garantindo que a falha de uma única réplica não cause uma interrupção regional.

#### Isolamento da carga de trabalho

*Desafio: Frequentemente nos deparamos com situações em que determinadas solicitações consomem uma quantidade desproporcional de recursos em instâncias do PostgreSQL. Isso pode levar à degradação do desempenho de outras cargas de trabalho executadas nas mesmas instâncias. Por exemplo, o lançamento de uma nova funcionalidade pode introduzir consultas ineficientes que consomem grande parte da CPU do PostgreSQL, tornando mais lentas as solicitações de outras funcionalidades críticas.*

Solution: To mitigate the “noisy neighbor” problem, we isolate workloads onto dedicated instances to ensure that sudden spikes in resource-intensive requests don’t impact other traffic. Specifically, we split requests into low-priority and high-priority tiers and route them to separate instances. This way, even if a low-priority workload becomes resource-intensive, it won’t degrade the performance of high-priority requests. We apply the same strategy across different products and services as well, so that activity from one product does not affect the performance or reliability of another.

#### Connection pooling

*Challenge: Each instance has a maximum connection limit (5,000 in Azure PostgreSQL). It’s easy to run out of connections or accumulate too many idle ones. We’ve previously had incidents caused by connection storms that exhausted all available connections.*

Solution: We deployed PgBouncer as a proxy layer to pool database connections. Running it in statement or transaction pooling mode allows us to efficiently reuse connections, greatly reducing the number of active client connections. This also cuts connection setup latency: in our benchmarks, the average connection time dropped from 50 milliseconds (ms) to 5 ms. Inter-region connections and requests can be expensive, so we co-locate the proxy, clients, and replicas in the same region to minimize network overhead and connection use time. Moreover, PgBouncer must be configured carefully. Settings like idle timeouts are critical to prevent connection exhaustion.

Cada réplica de leitura possui sua própria implantação do Kubernetes executando vários pods do PgBouncer. Executamos várias implantações do Kubernetes por trás do mesmo serviço do Kubernetes, que distribui o tráfego entre os pods.

#### Caching

*Challenge: A sudden spike in cache misses can trigger a surge of reads on the PostgreSQL database, saturating CPU and slowing user requests.*

Solution: To reduce read pressure on PostgreSQL, we use a caching layer to serve most of the read traffic. However, when cache hit rates drop unexpectedly, the burst of cache misses can push a large volume of requests directly to PostgreSQL. This sudden increase in database reads consumes significant resources, slowing down the service. To prevent overload during cache-miss storms, we implement a cache locking (and leasing) mechanism so that only a single reader that misses on a particular key fetches the data from PostgreSQL. When multiple requests miss on the same cache key, only one request acquires the lock and proceeds to retrieve the data and repopulate the cache. All other requests wait for the cache to be updated rather than all hitting PostgreSQL at once. This significantly reduces redundant database reads and protects the system from cascading load spikes.

#### Scaling read replicas

*Challenge: The primary streams Write Ahead Log (WAL) data to every read replica. As the number of replicas increases, the primary must ship WAL to more instances, increasing pressure on both network bandwidth and CPU. This causes higher and more unstable replica lag, which makes the system harder to scale reliably.*

Solution: We operate nearly 50 read replicas across multiple geographic regions to minimize latency. However, with the current architecture, the primary must stream WAL to every replica. Although it currently scales well with very large instance types and high-network bandwidth, we can’t keep adding replicas indefinitely without eventually overloading the primary. To address this, we’re collaborating with the Azure PostgreSQL team on [cascading replication ⁠](https://www.postgresql.org/docs/current/warm-standby.html#CASCADING-REPLICATION), where intermediate replicas relay WAL to downstream replicas. This approach allows us to scale to potentially over a hundred replicas without overwhelming the primary. However, it also introduces additional operational complexity, particularly around failover management. The feature is still in testing; we’ll ensure it’s robust and can fail over safely before rolling it out to production.

#### Rate limit

*Challenge: A sudden traffic spike on specific endpoints, a surge of expensive queries, or a retry storm can quickly exhaust critical resources such as CPU, I/O, and connections, which causes widespread service degradation.*

Solution: We implemented rate-limiting across multiple layers—application, connection pooler, proxy, and query—to prevent sudden traffic spikes from overwhelming database instances and triggering cascading failures. It’s also crucial to avoid overly short retry intervals, which can trigger retry storms. We also enhanced the ORM layer to support rate limiting and when necessary, fully block specific query digests. This targeted form of load shedding enables rapid recovery from sudden surges of expensive queries.

#### Schema Management

*Challenge: Even a small schema change, such as altering a column type, can trigger* [*a full table rewrite* ⁠](https://www.crunchydata.com/blog/when-does-alter-table-require-a-rewrite)*. We therefore apply schema changes cautiously—limiting them to lightweight operations and avoiding any that rewrite entire tables.*

Solution: Only lightweight schema changes are permitted, such as adding or removing certain columns that do not trigger a full table rewrite. We enforce a strict 5-second timeout on schema changes. Creating and dropping indexes concurrently is allowed. Schema changes are restricted to existing tables. If a new feature requires additional tables, they must be in alternative sharded systems such as Azure CosmosDB rather than PostgreSQL. When backfilling a table field, we apply strict rate limits to prevent write spikes. Although this process can sometimes take over a week, it ensures stability and avoids any production impact.

## Results and the road ahead

This effort demonstrates that with the right design and optimizations, Azure PostgreSQL can be scaled to handle the largest production workloads. PostgreSQL handles millions of QPS for read-heavy workloads, powering OpenAI’s most critical products like ChatGPT and the API platform. We added nearly 50 read replicas, while keeping replication lag near zero, maintained low-latency reads across geo-distributed regions, and built sufficient capacity headroom to support future growth.

This scaling works while still minimizing latency and improving reliability. We consistently deliver low double-digit millisecond p99 client-side latency and five-nines availability in production. And over the past 12 months, we’ve had only one SEV-0 PostgreSQL incident (it occurred during the [viral launch ⁠](https://newsletter.pragmaticengineer.com/p/chatgpt-images) of ChatGPT ImageGen, when write traffic suddenly surged by more than 10x as over 100 million new users signed up within a week.)

While we’re happy with how far PostgreSQL has taken us, we continue to push its limits to ensure we have sufficient runway for future growth. We’ve already migrated the shardable write-heavy workloads to our sharded systems like CosmosDB. The remaining write-heavy workloads are more challenging to shard—we’re actively migrating those as well to further offload writes from the PostgreSQL primary. We’re also working with Azure to enable cascading replication so we can safely scale to significantly more read replicas.

Looking ahead, we’ll continue to explore additional approaches to further scale, including sharded PostgreSQL or alternative distributed systems, as our infrastructure demands continue to grow.

- [2026](https://openai.com/pt-BR/news/?tags=2026)

## Autoria

Bohan Zhang

## Agradecimentos

Um agradecimento especial a Jon Lee, Sicheng Liu, Chaomin Yu e Chenglong Hao, que contribuíram para esta publicação, e a toda a equipe que ajudou a escalar o PostgreSQL. Gostaríamos também de agradecer à equipe do Azure PostgreSQL pela sólida parceria.

## Continuar lendo[Construindo um sandbox seguro e eficaz para viabilizar o Codex no Windows](https://openai.com/index/building-codex-windows-sandbox/)[Como a OpenAI oferece IA de voz de baixa latência em escala](https://openai.com/pt-BR/index/delivering-low-latency-voice-ai-at-scale/)