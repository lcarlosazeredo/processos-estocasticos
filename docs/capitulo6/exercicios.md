# Exercícios Resolvidos: Movimento Browniano

Esta página contém resoluções detalhadas dos principais tópicos abordados no Capítulo 6.

---

## 1. Propriedades de Escala e Variância { #ex61 }

**Enunciado:** Seja $(W_t)$ um Movimento Browniano padrão. Calcule a variância e a covariância para os instantes $t=2$ e $t=5$.

**Resolução:**
1. **Variância:** Para o Movimento Browniano, $W_t \sim N(0, t)$.
   * $Var(W_2) = 2$
   * $Var(W_5) = 5$
2. **Covariância:** A propriedade fundamental é que $Cov(W_s, W_t) = \min(s, t)$.
   * $Cov(W_2, W_5) = \min(2, 5) = 2$

---

## 2. Princípio da Reflexão e Máximo do Processo { #ex62 }

**Enunciado:** Qual a probabilidade de um Movimento Browniano padrão atingir o nível $b=2$ em algum momento antes do tempo $t=4$?

**Resolução:**
1. Seja $S_t = \max_{0 \leq s \leq t} W_s$. Queremos calcular $P(S_4 \geq 2)$.
2. Pelo Princípio da Reflexão: $P(S_t \geq b) = 2P(W_t \geq b)$.
   * $P(S_4 \geq 2) = 2P(W_4 \geq 2)$
3. Como $W_4 \sim N(0, 4)$, podemos normalizar para $Z \sim N(0, 1)$ usando $Z = W_4 / \sqrt{4} = W_4 / 2$:
   * $2P(W_4 / 2 \geq 2 / 2) = 2P(Z \geq 1)$
4. Consultando a tabela da normal padrão ($P(Z \geq 1) \approx 0.1587$):
   * $P \approx 2 \cdot 0.1587 = 0.3174 \text{ (ou 31,74%)}$



---

## 3. Movimento Browniano Geométrico (MBG) { #ex63 }

**Enunciado:** O preço de uma ação segue um MBG com $\mu = 0.1$ e $\sigma = 0.2$. Se o preço inicial é $Y_0 = 100$, qual o preço esperado após 1 ano ($t=1$)?

**Resolução:**
1. A fórmula do preço esperado para o MBG é $E[Y_t] = Y_0 e^{\mu t}$.
   * $E[Y_1] = 100 \cdot e^{0.1 \cdot 1} = 100 \cdot e^{0.1}$
2. Calculando o valor ($e^{0.1} \approx 1.1052$):
   * $E[Y_1] \approx 100 \cdot 1.1052 = 110,52$

**Nota:** Observe que a tendência do logaritmo (drift do $X_t$) é $\mu - \sigma^2/2$, mas a esperança do preço cresce puramente com $\mu$.

---

## 4. Variação Quadrática e Regra de Itô { #ex64 }

**Enunciado:** Mostre que para um Movimento Browniano padrão, a variação quadrática esperada no intervalo $[0, t]$ é igual a $t$.

**Resolução:**
1. A variação quadrática é definida pelo limite da soma dos incrementos ao quadrado: $\sum (W_{t_{i+1}} - W_{t_i})^2$.
2. A esperança de cada incremento ao quadrado é $E[(W_{t_{i+1}} - W_{t_i})^2] = Var(W_{t_{i+1}} - W_{t_i})$.
3. Pela propriedade dos incrementos: $Var(W_{t_{i+1}} - W_{t_i}) = t_{i+1} - t_i$.
4. Somando todos os intervalos da partição:
   $\sum (t_{i+1} - t_i) = t$

**Conclusão:** No limite, a variação quadrática converge para $t$ quase certamente, o que justifica a regra $(dW_t)^2 = dt$ no Cálculo de Itô.