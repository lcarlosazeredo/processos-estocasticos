# 5. Martingales

## 1. Definições Fundamentais e Estrutura { #51 }

O conceito de Martingale formaliza a ideia de um "jogo justo", onde o conhecimento do passado não ajuda a prever a mudança futura média.

* **Filtração ($A_n$):** É uma sequência crescente de $\sigma$-álgebras ($A_0 \subset A_1 \subset \dots \subset A$). Representa o acúmulo de informação ao longo do tempo.
* **Martingale:** Um processo estocástico ($M_n : n \geq 0$) é um martingale com respeito a uma filtração ($A_n$) se satisfaz:
    1. **Integrabilidade:** $E[|M_n|] < \infty$ para todo $n$.
    2. **Adaptabilidade:** $M_n$ é $A_n$-mensurável.
    3. **Propriedade de Martingale:** $E[M_{n+1} \mid A_n] = M_n$ quase certamente.
    * **Consequência:** $E[M_n] = E[M_0]$ para todo $n$.

* **Submartingale:** Tem tendência de crescer (ou manter-se): $E[X_{n+1} \mid A_n] \geq X_n$.
* **Supermartingale:** Tem tendência de decrescer (ou manter-se): $E[X_{n+1} \mid A_n] \leq X_n$.

---

## 2. Exemplos Clássicos { #52 }

* **Soma de Variáveis i.i.d.:** Se $S_n = \sum_{i=1}^{n} \xi_i$ com $E[\xi_i] = \mu$, então $M_n = S_n - n\mu$ é um martingale.
* **Martingale Quadrático:** Se $E[\xi_i] = 0$ e $\text{Var}(\xi_i) = \sigma^2$, então $M_n = S_n^2 - n\sigma^2$ é um martingale.
* **Urna de Polya:** A proporção de bolas brancas $M_n = \frac{X_n}{n+2}$ é um martingale e converge para uma variável aleatória.
* **Funções Harmônicas:** Se $Ph = h$, então $M_n = h(X_n)$ é um martingale.

---

## 3. Tempos de Parada e Amostragem Opcional { #53 }

* **Tempo de Parada ($\tau$):** Variável aleatória onde o evento $\{\tau = n\} \in A_n$ (parar depende apenas do passado e presente).
* **Teorema da Amostragem Opcional:** Sob certas condições, parar um martingale num tempo aleatório preserva a esperança: $E[M_{\tau}] = E[M_0]$.
    * **Teorema de Doob:** Se $\tau$ não for limitado, exige-se que o processo seja Uniformemente Integrável (U.I.).

---

## 4. Convergência de Martingales { #54 }

Um dos resultados centrais da teoria é que martingales "comportados" estabilizam no longo prazo.

* **Teorema da Convergência:** Se $\sup_n E[|M_n|] < \infty$, então existe $M_{\infty}$ tal que $M_n \to M_{\infty}$ quase certamente.
* **Cadeias de Ramificação:** Se $\eta$ é a média de filhos, então $W_n = \frac{X_n}{\eta^n}$ é um martingale que converge para $W$.



---

## 5. Desigualdades Maximais e Concentração { #55 }

Ferramentas para controlar o comportamento do máximo de um processo.

* **Desigualdade Maximal de Doob:** Para um submartingale não negativo:
  
  $P(\max_{0 \leq k \leq n} M_k \geq \lambda) \leq \frac{E[M_n]}{\lambda}$

* **Desigualdade de Azuma-Hoeffding:** Para martingales com incrementos limitados ($|M_n - M_{n-1}| \leq c_n$):
  
  $P(M_n - M_0 \geq \lambda) \leq \exp\left(-\frac{\lambda^2}{2 \sum_{i=1}^{n} c_i^2}\right)$

* **Aplicação (Álbum de Figurinhas):** A desigualdade de Azuma prova que o número de pacotes necessários está altamente concentrado em torno da média.