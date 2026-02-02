# Exercícios Resolvidos: Processos de Renovação

Esta página contém resoluções detalhadas dos principais tópicos abordados no Capítulo 4.

---

## 1. Instantes de Renovação e Contagem { #ex41 }

**Enunciado:** Os tempos entre as falhas de um motor seguem uma distribuição Uniforme no intervalo $[4, 6]$ meses. Calcule o tempo médio até a 10ª falha e a taxa de renovação a longo prazo.

**Resolução:**
1. **Identificar a média ($\mu$):**
   Para $T \sim U(4, 6)$, a média é $\mu = \frac{4 + 6}{2} = 5$ meses.
2. **Tempo até a 10ª renovação ($S_{10}$):**
   $E[S_{10}] = 10 \cdot \mu = 10 \cdot 5 = 50$ meses.
3. **Taxa de Renovação a longo prazo:**
   Pela Lei Forte dos Grandes Números para renovação:
   $\frac{N_t}{t} \to \frac{1}{\mu} = \frac{1}{5} = 0,2$ falhas por mês.

---

## 2. Paradoxo da Inspeção e Vida Residual { #ex42 }

**Enunciado:** Lâmpadas têm tempo de vida distribuído de forma Exponencial com média de 100 horas. Se um inspetor chega ao laboratório em um tempo $t$ muito grande, qual o tempo médio de vida total da lâmpada que ele encontrará instalada ($E[C_{\infty}]$)?

**Resolução:**
1. **Dados da distribuição original:**
   $\mu = 100$. Para a distribuição Exponencial, $E[T^2] = 2\mu^2 = 2(100)^2 = 20.000$.
2. **Aplicar a fórmula do Paradoxo da Inspeção:**
   A vida total limite é dada por $E[C_{\infty}] = \frac{E[T^2]}{E[T]}$.
   $E[C_{\infty}] = \frac{20.000}{100} = 200$ horas.

**Interpretação:** O inspetor encontrará uma lâmpada que dura, em média, o dobro do tempo das lâmpadas comuns, pois intervalos maiores têm mais chance de "cobrir" o instante da inspeção.



---

## 3. Distribuição da Idade ($A_t$) e Vida Residual ($B_t$) { #ex43 }

**Enunciado:** Considere um processo de renovação onde os tempos entre eventos são uniformes entre $0$ e $2$. Determine a densidade de probabilidade da vida residual limite ($B_{\infty}$).

**Resolução:**
1. **Dados:** $f(x) = \frac{1}{2}$ para $0 \leq x \leq 2$. $\mu = 1$.
2. **Fórmula da densidade limite:**
   $g_{B_{\infty}}(x) = \frac{1-F(x)}{\mu}$.
3. **Calcular $1-F(x)$:**
   $F(x) = \frac{x}{2} \implies 1-F(x) = 1 - \frac{x}{2}$ para $0 \leq x \leq 2$.
4. **Substituir:**
   $g_{B_{\infty}}(x) = \frac{1 - x/2}{1} = 1 - \frac{x}{2}$.

**Resultado:** A densidade da vida residual decai linearmente de $1$ até $0$ no intervalo $[0, 2]$.

---

## 4. Função de Renovação e Equação de Renovação { #ex44 }

**Enunciado:** Se a função de renovação é dada por $U(t) = 1 + 2t$, qual a média $\mu$ dos tempos entre renovações?

**Resolução:**
1. Pelo Teorema Elementar da Renovação:
   $\lim_{t \to \infty} \frac{U(t)}{t} = \frac{1}{\mu}$.
2. Derivando a função dada ou observando o coeficiente angular:
   $\frac{1}{\mu} = 2 \implies \mu = 0,5$.

**Resultado:** O tempo médio entre as renovações é $0,5$ unidades de tempo.