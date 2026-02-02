# Exercícios Resolvidos: Cadeias de Markov

Esta página contém resoluções detalhadas dos principais tópicos abordados no Capítulo 1.

---

## 1. Classificação de Estados e Irredutibilidade { #ex11 }

**Enunciado:** Considere uma cadeia de Markov com espaço de estados $S = \{1, 2, 3, 4\}$ e matriz de transição:

$P = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0.5 & 0 & 0.5 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0.5 & 0 & 0.5 \end{pmatrix}$

Classifique os estados quanto à comunicação e identifique se a cadeia é irredutível.

**Resolução:**
1. **Comunicação:** * Do estado $1$, podemos ir para $2$. Do estado $2$, podemos voltar para $1$. Logo, $1 \leftrightarrow 2$.
   * Do estado $2$, podemos ir para $3$. No entanto, o estado $3$ é absorvente ($P_{33} = 1$), então não podemos sair de $3$. Logo, $2 \to 3$ mas $3 \not\to 2$.
   * Do estado $4$, podemos ir para $2$. Como $2 \not\to 4$, a comunicação é apenas unidirecional.
2. **Classes:**
   * $\{3\}$ é uma classe fechada (recorrente).
   * $\{1, 2\}$ é uma classe aberta (transiente), pois há chance de sair para o estado $3$.
   * $\{4\}$ é transiente.
3. **Conclusão:** A cadeia **não é irredutível**, pois possui mais de uma classe de comunicação.



---

## 2. Distribuição Estacionária { #ex12 }

**Enunciado:** Encontre a distribuição estacionária $\pi$ para uma cadeia irredutível com matriz:

$P = \begin{pmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{pmatrix}$

**Resolução:**
Devemos resolver o sistema $\pi P = \pi$ sujeito a $\sum \pi_i = 1$.
Seja $\pi = (\pi_1, \pi_2)$:
1. $0.7\pi_1 + 0.4\pi_2 = \pi_1 \implies 0.4\pi_2 = 0.3\pi_1 \implies \pi_1 = \frac{4}{3}\pi_2$
2. $\pi_1 + \pi_2 = 1 \implies \frac{4}{3}\pi_2 + \pi_2 = 1 \implies \frac{7}{3}\pi_2 = 1$

**Resultado:**
$\pi_2 = \frac{3}{7}$ e $\pi_1 = \frac{4}{7}$.
A distribuição estacionária é $\pi = (\frac{4}{7}, \frac{3}{7})$.

---

## 3. Matriz Fundamental e Absorção { #ex13 }

**Enunciado:** Para uma cadeia com estados transientes $\{1, 2\}$ e estado absorvente $\{3\}$, com matriz de transição para os transientes $Q = \begin{pmatrix} 0.5 & 0.2 \\ 0.1 & 0.4 \end{pmatrix}$, calcule o número esperado de visitas a cada estado antes da absorção partindo do estado $1$.

**Resolução:**
1. **Calcular $I - Q$:**
   $I - Q = \begin{pmatrix} 0.5 & -0.2 \\ -0.1 & 0.6 \end{pmatrix}$
2. **Matriz Fundamental $M = (I - Q)^{-1}$:**
   $\text{det}(I - Q) = (0.5)(0.6) - (-0.2)(-0.1) = 0.30 - 0.02 = 0.28$
   $M = \frac{1}{0.28} \begin{pmatrix} 0.6 & 0.2 \\ 0.1 & 0.5 \end{pmatrix} \approx \begin{pmatrix} 2.14 & 0.71 \\ 0.35 & 1.78 \end{pmatrix}$

**Interpretação:**
Partindo do estado $1$, espera-se visitar o próprio estado $1$ cerca de $2.14$ vezes e o estado $2$ cerca de $0.71$ vezes antes de ser absorvido pelo estado $3$.

---

## 4. Periodicidade { #ex14 }

**Enunciado:** Determine o período do estado $0$ em uma cadeia com transições $0 \to 1 \to 2 \to 0$ e $0 \to 2$.

**Resolução:**
1. Possíveis caminhos de retorno ao estado $0$:
   * $0 \to 1 \to 2 \to 0$ (comprimento $3$)
   * $0 \to 2 \to 0$ (comprimento $2$)
2. O período $d(0)$ é o máximo divisor comum ($mdc$) dos comprimentos de todos os caminhos de retorno:
   $d(0) = mdc(2, 3) = 1$

**Resultado:** O estado é **aperiódico**.