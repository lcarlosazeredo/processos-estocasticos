# Exercícios Resolvidos: Martingales

Esta página contém resoluções detalhadas dos principais tópicos abordados no Capítulo 5.

---

## 1. Verificação da Propriedade de Martingale { #ex51 }

**Enunciado:** Seja $X_n$ um processo onde $X_{n+1}$ é igual a $2X_n$ com probabilidade $0.5$ e igual a $0$ com probabilidade $0.5$. Verifique se $X_n$ é um martingale em relação à sua própria filtração.

**Resolução:**
Para ser um martingale, deve satisfazer $E[X_{n+1} \mid X_0, \dots, X_n] = X_n$.
1. Calculamos a esperança condicional:
   $E[X_{n+1} \mid X_n] = (2X_n) \cdot 0.5 + (0) \cdot 0.5$
   $E[X_{n+1} \mid X_n] = X_n$
2. **Conclusão:** Como a esperança do próximo passo, dado o presente, é igual ao valor atual, o processo **é um martingale**.

---

## 2. Ruína do Jogador via Amostragem Opcional { #ex52 }

**Enunciado:** Um jogador começa com $\$k$ e aposta $\$1$ em cada rodada (ganha $\$1$ ou perde $\$1$ com prob. $0.5$). Ele para se atingir $\$N$ ou se chegar a $\$0$. Qual a probabilidade de ele sair vitorioso com $\$N$?

**Resolução:**
1. Seja $M_n$ o capital no tempo $n$. $M_n$ é um martingale e o tempo de parada $\tau$ (atingir $0$ ou $N$) é finito.
2. Pelo Teorema da Amostragem Opcional: $E[M_\tau] = E[M_0] = k$.
3. Seja $p$ a probabilidade de atingir $N$. Então:
   $E[M_\tau] = N \cdot p + 0 \cdot (1-p) = k$
   $Np = k \implies p = \frac{k}{N}$

**Resultado:** A probabilidade de vitória é $\frac{k}{N}$.



---

## 3. Martingale Quadrático e Tempo de Espera { #ex53 }

**Enunciado:** No problema anterior, qual o tempo médio esperado $E[\tau]$ para o jogo terminar?

**Resolução:**
1. Sabemos que $M_n^2 - n$ é um martingale (martingale quadrático para passos de variância $1$).
2. Pelo Teorema da Amostragem Opcional: $E[M_\tau^2 - \tau] = E[M_0^2 - 0] = k^2$.
3. $E[M_\tau^2] - E[\tau] = k^2$.
4. Calculamos $E[M_\tau^2]$ usando a probabilidade $p = k/N$ do exercício anterior:
   $E[M_\tau^2] = N^2 \cdot (k/N) + 0^2 \cdot (1 - k/N) = Nk$.
5. Substituindo: $Nk - E[\tau] = k^2 \implies E[\tau] = Nk - k^2 = k(N-k)$.

**Resultado:** O tempo médio é $k(N-k)$ rodadas.

---

## 4. Desigualdade de Azuma-Hoeffding { #ex54 }

**Enunciado:** Um martingale $M_n$ tem incrementos limitados por $|M_n - M_{n-1}| \leq 1$. Se $M_0 = 0$, estime a probabilidade de $M_{100}$ ser maior ou igual a $20$.

**Resolução:**
1. Usamos a fórmula: $P(M_n - M_0 \geq \lambda) \leq \exp\left(-\frac{\lambda^2}{2\sum c_i^2}\right)$.
2. Aqui, $n=100$, $\lambda=20$ e $c_i=1$ para todos os $i$.
3. $\sum_{i=1}^{100} c_i^2 = 100$.
4. $P(M_{100} \geq 20) \leq \exp\left(-\frac{20^2}{2 \cdot 100}\right) = \exp\left(-\frac{400}{200}\right) = e^{-2} \approx 0.1353$.

**Resultado:** A probabilidade é de no máximo $13.53\%$.