# Exercícios Resolvidos: Processos de Poisson

Esta página contém resoluções detalhadas dos principais tópicos abordados no Capítulo 2.

---

## 1. Probabilidades de Contagem e Incrementos { #ex21 }

**Enunciado:** Em um servidor de e-mails, as mensagens chegam segundo um processo de Poisson com taxa $\lambda = 10$ e-mails por hora. Qual a probabilidade de que cheguem exatamente 3 e-mails nos primeiros 20 minutos e nenhum e-mail nos 10 minutos seguintes?

**Resolução:**
1. **Definir as taxas para cada intervalo:**
   * O primeiro intervalo é de 20 minutos ($t_1 = 1/3$ hora). A média é $\alpha_1 = \lambda \cdot t_1 = 10 \cdot (1/3) = 10/3$.
   * O segundo intervalo é de 10 minutos ($t_2 = 1/6$ hora). A média é $\alpha_2 = \lambda \cdot t_2 = 10 \cdot (1/6) = 10/6 = 5/3$.
2. **Calcular as probabilidades independentes:**
   * Probabilidade de 3 e-mails no primeiro intervalo:
     $P(N_{1/3} = 3) = \frac{e^{-10/3} \cdot (10/3)^3}{3!}$
   * Probabilidade de 0 e-mails no segundo intervalo:
     $P(N_{1/2} - N_{1/3} = 0) = e^{-5/3}$
3. **Resultado Final (Multiplicação devido aos incrementos independentes):**
   $P = \left( \frac{e^{-10/3} \cdot 1000/27}{6} \right) \cdot e^{-5/3} = \frac{1000}{162} \cdot e^{-5} \approx 0.0415 \text{ (ou 4.15%)}$

---

## 2. Decomposição e Superposição (Thinning) { #ex22 }

**Enunciado:** Um call center recebe chamadas técnicas ($\lambda_T = 4/\text{hora}$) e chamadas comerciais ($\lambda_C = 6/\text{hora}$). Sabe-se que $20\%$ das chamadas técnicas são classificadas como "urgentes". Qual a probabilidade de o centro receber mais de 2 chamadas urgentes em um turno de 2 horas?

**Resolução:**
1. **Identificar a taxa das chamadas urgentes:**
   A taxa técnica é $\lambda_T = 4$. A taxa de urgentes é $\lambda_U = \lambda_T \cdot p = 4 \cdot 0,2 = 0,8$ chamadas por hora.
2. **Ajustar para o intervalo de 2 horas ($t=2$):**
   A média no turno é $E[N_U(2)] = 0,8 \cdot 2 = 1,6$.
3. **Calcular $P(N_U > 2)$ usando o complementar:**
   $P(N_U > 2) = 1 - [P(N_U = 0) + P(N_U = 1) + P(N_U = 2)]$
   $P = 1 - [e^{-1,6} + e^{-1,6} \cdot 1,6 + \frac{e^{-1,6} \cdot (1,6)^2}{2}]$
   $P = 1 - e^{-1,6} \cdot (1 + 1,6 + 1,28) = 1 - 3,88 \cdot e^{-1,6} \approx 0,2166 \text{ (ou 21,66%)}$



---

## 3. Tempos de Interchegada e Distribuição Gama { #ex23 }

**Enunciado:** Falhas em uma rede ocorrem com taxa $\lambda = 0,5$ falhas/dia. Qual o tempo esperado para que ocorra a 4ª falha e qual a probabilidade de ela ocorrer antes de completar 6 dias?

**Resolução:**
1. **Tempo Esperado:**
   O tempo até a $n$-ésima renovação $S_n$ segue uma distribuição Gama com média $n/\lambda$.
   $E[S_4] = 4 / 0,5 = 8 \text{ dias}$
2. **Probabilidade $P(S_4 \leq 6)$:**
   Pela relação fundamental entre o processo de contagem e os tempos de chegada:
   $\{S_4 \leq 6\} \iff \{N_6 \geq 4\}$
3. **Calcular via Poisson ($\alpha = 0,5 \cdot 6 = 3$):**
   $P(N_6 \geq 4) = 1 - \sum_{k=0}^{3} \frac{e^{-3} \cdot 3^k}{k!}$
   $P = 1 - e^{-3} \cdot (1 + 3 + 4.5 + 4.5) = 1 - 13 \cdot e^{-3} \approx 0,3528 \text{ (ou 35,28%)}$

---

## 4. Processo de Poisson Composto { #ex24 }

**Enunciado:** O número de clientes que entram em uma loja segue um processo de Poisson com $\lambda = 5/\text{hora}$. Cada cliente gasta um valor $Y_i$ que é independente e segue uma distribuição com média $\$20$ e desvio padrão $\$10$. Calcule a média e a variância do faturamento total após 8 horas.

**Resolução:**
1. **Dados do problema:**
   $\lambda = 5$, $t = 8$, $E[Y] = 20$, $Var(Y) = 10^2 = 100$.
   O número médio de clientes é $E[N_8] = 5 \cdot 8 = 40$.
2. **Média do Faturamento ($X_t$):**
   $E[X_8] = E[N_8] \cdot E[Y] = 40 \cdot 20 = \$800$
3. **Variância do Faturamento:**
   $Var(X_8) = \lambda t \cdot E[Y^2]$
   Primeiro, calculamos $E[Y^2] = Var(Y) + (E[Y])^2 = 100 + 400 = 500$.
   $Var(X_8) = (5 \cdot 8) \cdot 500 = 40 \cdot 500 = 20.000$