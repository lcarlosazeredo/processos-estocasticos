# 1. Cadeias de Markov: Fundamentos e Estruturas

Este capítulo estabelece a "linguagem" dos processos estocásticos, definindo o que torna um processo Markoviano e como analisar seu comportamento de longo prazo.

---

## 1. Fundamentos e Definições Básicas { #11 }

### Propriedade de Markov
A característica definidora é que o futuro do processo depende apenas do estado presente e não do histórico passado. Matematicamente, para um processo $(X_n)_{n \geq 0}$:

$$P(X_{n+1} = j \mid X_0 = i_0, \dots, X_n = i) = P(X_{n+1} = j \mid X_n = i)$$

* **Homogeneidade:** Assume-se geralmente que as probabilidades de transição não mudam com o tempo $n$.
* **Matriz de Transição ($P$):** Definimos as entradas como $P_{ij} = p(i,j) = P(X_1 = j \mid X_0 = i)$. A soma das linhas deve ser sempre 1: $\sum_{j \in S} p(i,j) = 1$.
* **Equações de Chapman-Kolmogorov:** Usadas para calcular a transição em $n$ passos. Em termos matriciais: $P^{(n)} = P^n$. A distribuição no tempo $n$ é dada por $\pi_n = \pi_0 P^n$.

---

## 2. Estrutura e Classificação de Estados { #12 }

### Topologia da Cadeia
* **Grafo Dirigido:** Representação visual onde os nós são os estados e existe uma aresta $i \to j$ se $P_{ij} > 0$.
* **Comunicação ($i \leftrightarrow j$):** Dois estados se comunicam se for possível ir de $i$ para $j$ e vice-versa em algum número de passos.
* **Irredutibilidade:** A cadeia é irredutível se possui apenas uma classe (todos os estados se comunicam).



### Periodicidade
O período $d(i)$ é o máximo divisor comum ($mdc$) dos tempos de retorno possíveis ao estado $i$:

$$d(i) = mdc\{n \geq 1 : P_{ii}^{(n)} > 0\}$$

* Se $d(i) = 1$, o estado é **aperiódico**.
* Se $P_{ii} > 0$ (possui um "laço" no grafo), o estado é automaticamente aperiódico.

---

## 3. Análise de Espaços de Estados Finitos { #13 }

### Distribuição Estacionária ($\pi$)
Vetor de probabilidades que permanece inalterado pela dinâmica da cadeia. Resolve-se o sistema:

$$\pi = \pi P \quad \text{sujeito a} \quad \sum \pi(i) = 1$$

### Análise de Transientes (Matriz Fundamental)
Para cadeias redutíveis, usamos a forma canônica: $P = \begin{pmatrix} P_{\text{fechada}} & 0 \\ R & Q \end{pmatrix}$.
A **Matriz Fundamental** é dada por:

$$M = (I - Q)^{-1}$$

* A entrada $M_{ij}$ dá o número esperado de visitas ao estado $j$ começando em $i$.
* A some da linha $i$ de $M$ fornece o tempo esperado até a absorção.

---

## 4. Propriedade Forte de Markov

### Tempo de Parada ($\tau$)
Uma variável aleatória onde a decisão de parar no tempo $n$ depende apenas da história até $n$ ($X_0, \dots, X_n$).

!!! info "Definição"
    A cadeia "reinicia" probabilisticamente a partir de um tempo de parada finito, comportando-se como se tivesse começado em $X_\tau$.

---

## 5. Espaços Enumeráveis e Tipos de Recorrência { #14 }

* **Estado Recorrente:** Retorno certo ($P(\tau_i < \infty) = 1$). Critério: $\sum_{n} P_{ii}^{(n)} = \infty$.
* **Estado Transiente:** Probabilidade positiva de nunca mais voltar. Critério: $\sum_{n} P_{ii}^{(n)} < \infty$.
* **Recorrência Positiva:** Tempo médio de retorno finito ($E[\tau_i] < \infty$). Existe $\pi(i) = 1/E_i[\tau_i]$.
* **Recorrência Nula:** Retorno certo, mas tempo médio infinito ($E[\tau_i] = \infty$). Não existe $\pi$.

---

## 6. Reversibilidade { #15 }

### Balanceamento Detalhado
Uma distribuição $\pi$ é reversível se o fluxo é igual em ambas as direções:

$$\pi(i)P_{ij} = \pi(j)P_{ji}, \quad \forall i,j \in S$$

!!! tip "Dica"
    Se $\pi$ satisfaz essa condição, ela é automaticamente estacionária ($\pi = \pi P$).

---

## 7. Aplicações Específicas

* **Ruína do Jogador:** Passeio aleatório com barreiras absorventes. Probabilidade de ruína começando em $i$ (jogo justo): $1 - (i/N)$.
* **Cadeias de Ramificação:** Se a média de filhos $\mu > 1$, a probabilidade de extinção é a menor raiz positiva de $s = \phi(s)$.
* **MCMC (Metropolis-Hastings):** Gera amostras de $\pi$ complexas usando a probabilidade de aceitação:
  $\alpha(i,j) = \min\left(1, \frac{\pi(j)q(j,i)}{\pi(i)q(i,j)}\right)$