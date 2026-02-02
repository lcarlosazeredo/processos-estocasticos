# 3. Cadeias de Markov em Tempo Contínuo

## 1. O Modelo: Definições e Propriedades Básicas { #31 }

Diferente do tempo discreto, aqui o processo $(X_t : t \geq 0)$ evolui continuamente. A transição entre estados pode ocorrer em qualquer instante $t$.

* **Propriedade de Markov:** O futuro do processo depende apenas do estado presente e não do passado. Formalmente, para quaisquer $0 \leq s_1 < \dots < s_k < s < t$:
  
  $P(X_{s+t} = j \mid X_s = i, X_{s_k} = i_k, \dots) = P(X_t = j \mid X_0 = i) =: P_{i,j}(t)$

* **Homogeneidade:** Assume-se que a probabilidade de transição $P_{i,j}(t)$ depende apenas do intervalo de tempo $t$, e não do momento absoluto em que a transição ocorre.

* **Equações de Chapman-Kolmogorov:** A probabilidade de ir de $i$ para $j$ no tempo $t+s$ pode ser decomposta passando por um estado intermediário $k$ no tempo $t$:
  
  $P(t+s) = P(t)P(s)$
  
  Onde $P(t)$ é a matriz de probabilidades de transição.

---

## 2. Construção e Características Infinitesimais { #32 }

Esta seção explica como o processo se comporta em intervalos de tempo muito pequenos ($h \to 0$), definindo a "velocidade" das mudanças.

* **Taxas de Salto ($q(i,j)$):** Representa a taxa com que o processo salta do estado $i$ para o estado $j$.
  
  $\lim_{h \downarrow 0} \frac{P_{i,j}(h)}{h} = q(i,j), \text{ para } i \neq j$

* **Taxa Total de Saída ($\lambda_i$):** É a taxa total com que o processo deixa o estado $i$.
  
  $\lambda_i = \sum_{j \neq i} q(i,j)$

* **Matriz Geradora ($Q$):** É a matriz fundamental para descrever a dinâmica em tempo contínuo (análoga à matriz $P$ do tempo discreto, mas contendo taxas, não probabilidades).
    * **Entradas fora da diagonal:** $Q_{i,j} = q(i,j) \geq 0$.
    * **Entradas na diagonal:** $Q_{i,i} = -\lambda_i$.
    * **Soma das linhas:** A soma de cada linha é zero: $\sum_{j} Q_{i,j} = 0$.

---

## 3. A Cadeia Imersa e Tempos de Espera { #33 }

Uma forma intuitiva de construir e simular esses processos é separar "onde" ele salta de "quando" ele salta.

* **Tempos de Espera (Holding Times):** O tempo que o processo permanece no estado $i$ antes de mudar segue uma distribuição Exponencial com parâmetro $\lambda_i$.
* **Cadeia Imersa (Embedded Chain):** É uma cadeia de Markov em tempo discreto ($\tilde{Z}_n$) que descreve apenas a sequência de estados visitados, ignorando o tempo. A probabilidade de transição da cadeia imersa é:
  
  $\tilde{p}(i,j) = \frac{q(i,j)}{\lambda_i}, \text{ para } i \neq j$

* **Condição de Regularidade:** Para garantir que o processo seja bem definido em todo $t \geq 0$, não podem ocorrer infinitos saltos em tempo finito (explosões).

---

## 4. Equações de Kolmogorov { #34 }

Estas são as equações diferenciais que relacionam a matriz geradora $Q$ com as probabilidades de transição $P(t)$.

* **Equação Retrospectiva (Backward):** Deriva-se condicionando no primeiro salto a partir do estado inicial:
  
  $P'(t) = QP(t)$

* **Equação Prospectiva (Forward):** Deriva-se condicionando no último salto antes do tempo $t$:
  
  $P'(t) = P(t)Q$

* **Solução Formal:** Para espaços de estados finitos, a solução é dada pela exponencial matricial:
  
  $P(t) = e^{tQ} = \sum_{n=0}^{\infty} \frac{(tQ)^n}{n!}$

---

## 5. Comportamento Assintótico (Longo Prazo) { #35 }

Analisa o que acontece quando $t \to \infty$.

* **Distribuição Estacionária ($\pi$):** Verificado resolvendo o sistema linear:
  
  $\pi Q = 0 \text{ sujeito a } \sum \pi(i) = 1$
  
  **Interpretação:** O fluxo total de probabilidade saindo de cada estado deve ser igual ao fluxo total entrando nele.

* **Teorema do Limite:** Se a cadeia for irredutível e positiva recorrente, a probabilidade de estar no estado $j$ converge para $\pi(j)$, independentemente do estado inicial:
  
  $\lim_{t \to \infty} P_{i,j}(t) = \pi(j)$

* **Relação com Tempos de Retorno:** $\pi(i) = \frac{1}{\lambda_i E_i[T_i]}$, onde $E_i[T_i]$ é o tempo médio de retorno ao estado $i$.

---

## 6. Reversibilidade { #36 }

* **Equações de Balanceamento Detalhado:** Uma distribuição $\pi$ é reversível se o fluxo entre quaisquer dois estados $i$ e $j$ é equilibrado:
  
  $\pi(i)q(i,j) = \pi(j)q(j,i)$

!!! tip "Dica"
    Se uma distribuição satisfaz essa condição, ela é automaticamente estacionária. Isso é muito útil em filas e redes.

---

## 7. Cadeias de Nascimentos e Mortes { #37 }

Um caso especial onde as transições só ocorrem para estados vizinhos ($i \to i+1$ ou $i \to i-1$).



* **Taxas:**
    * $\beta_i$: Taxa de nascimento (ida de $i$ para $i+1$).
    * $\mu_i$: Taxa de morte (ida de $i$ para $i-1$).
* **Solução Estacionária:** Existe uma fórmula fechada para $\pi$:
  
  $\pi(n) = \pi(0) \prod_{k=1}^{n} \frac{\beta_{k-1}}{\mu_k}$

---

## 8. Aplicações: Filas Markovianas { #38 }

O capítulo aplica a teoria de Nascimentos e Mortes para modelar sistemas de filas.

* **Fila M/M/1:** Chegadas Poisson ($\beta$), atendimento Exponencial ($\mu$), 1 servidor.
    * Estável se $\beta < \mu$.
    * Distribuição do número de clientes é Geométrica.
* **Fila M/M/$\infty$:** Infinitos servidores (sem espera). O número de clientes no sistema segue uma distribuição de Poisson.
* **Teorema de Burke:** Para uma fila M/M/k estável em equilíbrio, o processo de saídas (clientes deixando o sistema) é um Processo de Poisson com a mesma taxa das chegadas.