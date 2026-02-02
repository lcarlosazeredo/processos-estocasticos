# 6. Movimento Browniano e Introdução ao Cálculo Estocástico

Este capítulo explora o Movimento Browniano, o processo estocástico fundamental para a modelagem de fenômenos contínuos e a base do cálculo de Itô.

---

## 1. Definição e Caracterização { #61 }

O Movimento Browniano é apresentado como o limite contínuo do Passeio Aleatório Simples.

* **Definição Formal:** Um processo $(W_t : t \geq 0)$ é um Movimento Browniano Padrão se:
    1. **Início:** $W_0 = 0$.
    2. **Incrementos Independentes e Gaussianos:** Para quaisquer $0 = t_0 < t_1 < \dots < t_n$, os incrementos $W_{t_{i+1}} - W_{t_i}$ são independentes e $W_t - W_s \sim N(0, t-s)$.
    3. **Trajetórias Contínuas:** A função $t \mapsto W_t(\omega)$ é contínua quase certamente.



* **Movimento Browniano com Tendência (Drift):** Definido como $X_t = \sigma W_t + \mu t + x$, onde $\mu$ é a tendência, $\sigma^2$ o coeficiente de difusão e $x$ a posição inicial.
* **Teorema de Donsker:** O movimento browniano pode ser visto como o limite de um passeio aleatório reescalado: $W_t^{(n)} \approx S_{nt} / \sqrt{n}$.

---

## 2. A Construção de Lévy { #62 }

Trata da existência matemática do processo através de interpolação em intervalos diádicos.

* **Método de Interpolação:** Define-se $W$ em $D_n = \{k/2^n\}$. A distribuição de $W_t$ dado $W_{t_1}$ e $W_{t_2}$ é Gaussiana, permitindo a "interpolação browniana".
* **Convergência Uniforme:** O Lema 6.2.2 garante que essas aproximações convergem uniformemente, assegurando a continuidade das trajetórias.

---

## 3. Propriedades Fundamentais { #63 }

* **Invariância Escalar:** Se $W_t$ é um movimento browniano, $c^{-1} W_{c^2 t}$ também é um movimento browniano padrão para $c > 0$.
* **Lei 0-1 de Blumenthal:** Eventos que dependem apenas do comportamento infinitesimal perto de $t=0$ têm probabilidade 0 ou 1.
* **Comportamento no Infinito:** Com probabilidade 1, $\limsup_{t \to \infty} W_t = +\infty$ e $\liminf_{t \to \infty} W_t = -\infty$.

---

## 4. Propriedade de Markov e Reflexão { #64 }

* **Propriedade Forte de Markov:** O reinício probabilístico vale para Tempos de Parada $(\tau)$ finitos.
* **Princípio da Reflexão:** Se o processo atinge um nível $b$, a trajetória futura pode ser refletida. Isso permite calcular a distribuição do máximo $S_t = \sup_{s \leq t} W_s$:
  
  $P(S_t \geq b) = P(|W_t| \geq b) = 2P(W_t \geq b)$



---

## 5. Movimento Browniano Geométrico e Finanças { #65 }

Base do modelo Black-Scholes.

* **Definição:** $Y_t = Y_0 e^{(\mu - \sigma^2/2)t + \sigma W_t}$.
* **Vantagens:** Garante preços sempre positivos e modela retornos percentuais independentes.
* **Salto-Difusão de Merton:** Adiciona um Processo de Poisson Composto para modelar choques bruscos.

---

## 6. Propriedades das Trajetórias (Cálculo) { #66 }

* **Não Diferenciabilidade:** Com probabilidade 1, $W_t$ não possui derivada em nenhum ponto.
* **Variação Quadrática:** A soma dos quadrados dos incrementos converge para $t$:
  
  $\lim_{n \to \infty} \sum (W_{t_{i+1}} - W_{t_i})^2 = t \cdot \sigma^2$
  
  Esta é a base da regra de Itô: $(dW_t)^2 = dt$.

---

## 7. Introdução à Integral de Itô { #67 }

* **Motivação:** Dar sentido a Equações Diferenciais Estocásticas (SDEs):
  
  $dX_t = \mu(t, X_t) dt + \sigma(t, X_t) dW_t$

* **Forma Integral:** $X_t = X_0 + \int_0^t \mu(s, X_s) ds + \int_0^t \sigma(s, X_s) dW_s$. O segundo termo é a **Integral de Itô**, construída como um limite de somas discretas adaptadas à filtração.