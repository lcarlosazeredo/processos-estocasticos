# 4. Processos de Renovação

## 1. Definições Fundamentais e Construção { #41 }

A base do modelo é a substituição da propriedade de "falta de memória" (exponencial) por uma estrutura onde o processo "recomeça" probabilisticamente a cada evento.

* **Tempos entre Renovações ($T_n$):** Sequência de variáveis aleatórias i.i.d. não negativas com função de distribuição $F$. Assumimos $P(T_1 = 0) < 1$ para evitar degeneração.
    * **Interpretação:** $T_n$ é o tempo de vida do $n$-ésimo componente ou o tempo entre ocorrências.
    * **Média:** $\mu = E[T_1] \in (0, \infty]$.
* **Instantes das Renovações ($S_n$):** Tempo absoluto da $n$-ésima renovação:
  
  $S_0 = 0 \quad \text{e} \quad S_n = \sum_{i=1}^{n} T_i, \quad n \geq 1$

* **Processo de Contagem ($N_t$):** Número de renovações até o tempo $t$:
  
  $N_t = \max\{n \geq 0 : S_n \leq t\}$
  
  **Relação Fundamental:** $\{N_t \geq n\} \iff \{S_n \leq t\}$.

---

## 2. Teoremas de Renovação (Longo Prazo) { #42 }

Estes teoremas descrevem a estabilidade do processo quando $t \to \infty$.

* **Lei Forte dos Grandes Números:** A taxa de renovações converge quase certamente:
  
  $\lim_{t \to \infty} \frac{N_t}{t} = \frac{1}{\mu} \quad \text{q.c.}$

* **Função de Renovação ($U(t)$):** Número esperado de renovações em $[0,t]$:
  
  $U(t) = 1 + E[N_t] = \sum_{n=0}^{\infty} F^{(n)}(t)$
  
  Onde $F^{(n)}$ é a convolução de $F$ consigo mesma $n$ vezes.

* **Teorema de Blackwell:** * **Caso Não-Aritmético:** $\lim_{t \to \infty} (U(t+r) - U(t)) = \frac{r}{\mu}$.
* **Teorema do Limite Central:** Se $\text{Var}(T_1) = \sigma^2 < \infty$, então $N_t$ é assintoticamente Normal.

---

## 3. A "Trindade": Idade, Vida Residual e Vida Total { #43 }

Em um instante $t$, o estado do componente é descrito por três variáveis interligadas:

1. **Idade ($A_t$):** Tempo transcorrido desde a última renovação: $A_t = t - S_{N_t}$.
2. **Tempo de Vida Residual ($B_t$):** Tempo até a próxima renovação: $B_t = S_{N_t+1} - t$.
3. **Tempo de Vida Total ($C_t$):** Comprimento do intervalo que contém $t$: $C_t = A_t + B_t = T_{N_t+1}$.



### O Paradoxo da Inspeção
A densidade limite de $C_t$ é enviesada pelo tamanho (*length-biased*):
  
$f_{C_{\infty}}(x) = \frac{x f(x)}{\mu}$
  
**Consequência:** O tempo médio de vida inspecionado em tempo aleatório é maior que o médio real ($E[C_{\infty}] > E[T]$).

---

## 4. Equação de Renovação { #44 }

Ferramenta analítica central para provar resultados assintóticos:
  
$\phi(t) = h(t) + \int_{0}^{t} \phi(t-s) dF(s)$
  
A solução única é dada pela convolução com a função de renovação $U$:
  
$\phi(t) = \int_{0}^{t} h(t-s) dU(s)$

---

## 5. Processos de Renovação com Atraso (Delayed) { #45 }

Ocorre quando o primeiro tempo $T_0$ tem distribuição $G \neq F$.

* **Processo Estacionário:** Se $G$ for a distribuição de equilíbrio:
  
  $G(x) = \frac{1}{\mu} \int_{0}^{x} (1 - F(s)) ds$
  
  Então o processo torna-se estacionário e $E[N_t] = \frac{t}{\mu}$.

---

## 6. Aplicações { #46 }

* **Fila M/G/1:** Os instantes em que a fila fica vazia formam um processo de renovação.
  
  $\text{Proporção Ocupada} = \frac{E[U_1]}{E[R_1] + E[U_1]} = \lambda \theta$
  
  Onde $R_1$ é o tempo ocioso e $U_1$ o tempo ocupado.

* **Contador Geiger Tipo II:** O número de registros de pulsos é modelado como um processo de renovação devido ao "tempo morto".