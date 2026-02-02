# 2. Processos de Poisson e Aplicações

## 1. O Processo de Poisson: Definição e Hipóteses { #21 }

O processo de Poisson é o modelo fundamental para contar ocorrências de eventos pontuais e aleatórios ao longo do tempo (ex: chamadas num call center, falhas de equipamento, chegada de particules).

* **Processo de Contagem ($N_t$):** É uma função "escada" onde $N_t$ representa o número de ocorrências no intervalo $(0,t]$. As hipóteses fundamentais que definem o processo são:
    1. **Incrementos Estacionários (H1):** A probabilidade de ocorrerem $k$ eventos num intervalo depende apenas do comprimento do intervalo, não de onde ele começa.
    2. **Incrementos Independentes (H2):** O número de ocorrências em intervalos de tempo disjuntos são variáveis aleatórias independentes.
    3. **Ocorrências Isoladas (H3):** A probabilidade de dois ou mais eventos ocorrerem num intervalo minúsculo $h$ é desprezível comparada à probabilidade de ocorrer apenas um:
       
       $\lim_{h \to 0} \frac{P(N_h \geq 2)}{h} = 0$

* **Distribuição de Poisson:** A partir dessas hipóteses, demonstra-se que o número de eventos até o tempo $t$ segue uma distribuição de Poisson com média $\lambda t$, onde $\lambda$ é a taxa do processo:
  
  $P(N_t = k) = \frac{e^{-\lambda t}(\lambda t)^k}{k!}, \quad k=0,1,2,\dots$



---

## 2. A Distribuição Exponencial e Tempos de Chegada { #22 }

Esta seção conecta a contagem discreta ($N_t$) com o tempo contínuo entre os eventos.

* **Tempo até o primeiro evento ($T_1$):** A probabilidade de não haver eventos até $t$ ($N_t=0$) é $e^{-\lambda t}$. Isso implica que o tempo de espera tem distribuição Exponencial:
  
  $f(t) = \lambda e^{-\lambda t} \quad \text{e} \quad F(t) = 1 - e^{-\lambda t}$

* **Propriedade da Falta de Memória:** A exponencial é a única distribuição contínua que satisfaz:
  
  $P(T > t+s \mid T > t) = P(T > s)$
  
  **Significado:** O fato de nada ter acontecido até o tempo $t$ não altera a probabilidade do evento ocorrer nos próximos $s$ minutos. O sistema não "envelhece".

* **Mínimo de Exponenciais:** Se $T_1, \dots, T_n$ são independentes com taxas $\lambda_i$, o mínimo deles é também exponencial com taxa igual à soma ($\sum \lambda_i$).

* **Distribuição Gama:** O tempo até o $n$-ésimo evento ($S_n = T_1 + \dots + T_n$) segue uma distribuição Gama com parâmetros $n$ e $\lambda$.

---

## 3. Construção Alternativa e Propriedades Avançadas { #23 }

O livro revisita o processo de Poisson construindo-o a partir dos tempos de chegada, em vez das hipóteses infinitesimais.

* **Construção via Interchegadas:** Pode-se definir $N_t$ através de uma sequência de variáveis i.i.d. $T_n \sim \text{Exp}(\lambda)$.
  
  $N_t = \max\{n \geq 0 : S_n \leq t\}$
  
  Onde $S_n$ são os instantes dos eventos.

* **Superposição:** A soma de dois processos de Poisson independentes com taxas $\lambda_1$ e $\lambda_2$ é um novo processo de Poisson com taxa $\lambda_1 + \lambda_2$.

* **Decomposição (Thinning):** Se cada evento de um processo de Poisson (taxa $\lambda$) é classificado como "Tipo 1" (probabilidade $p$) ou "Tipo 2" (probabilidade $1-p$), os processos resultantes são processos de Poisson independentes com taxas $\lambda p$ e $\lambda(1-p)$.

* **Estatísticas de Ordem (Distribuição Condicional):** Dado que sabemos que ocorreram $n$ eventos até o tempo $t$ ($N_t=n$), os instantes exatos dessas ocorrências ($S_1, \dots, S_n$) têm a mesma distribuição que $n$ variáveis aleatórias $\text{Uniforme}(0,t)$ ordenadas.
    * **Implicação:** Os eventos se espalham "aleatoriamente" no intervalo, sem aglomeração preferencial.

---

## 4. Variações e Aplicações do Modelo { #24 }

O capítulo expande o modelo básico para situações mais complexas.

* **Processo de Poisson Composto:** Usado quando cada evento tem um "peso" ou "valor" associado (ex: valor de um sinistro de seguro, tamanho de um pacote de dados).
  
  $X_t = \sum_{i=1}^{N_t} Y_i$
  
  Onde $N_t$ é Poisson e $Y_i$ são i.i.d. e independentes de $N$.
    * **Média:** $E[X_t] = E[N_t] E[Y_1] = \lambda t E[Y_1]$.
    * **Variância:** $\text{Var}(X_t) = \lambda t E[Y_1^2]$.

* **Processo de Poisson Não-Homogêneo:** A taxa de ocorrência $\lambda$ não é constante, mas uma função do tempo $\lambda(t)$. O número de eventos em $(t, t+s]$ segue uma Poisson com média:
  
  $\int_{t}^{t+s} \lambda(u) du$

* **Processo Pontual em $\mathbb{R}^d$:** Generalização espacial. O número de pontos numa região $A$ segue uma Poisson proporcional ao volume/área de $A$. Regiões disjuntas têm contagens independentes.

* **Fila $M/G/\infty$:** Um sistema com infinitos servidores (sem espera).
    * **Chegadas:** Poisson ($\lambda$).
    * **Atendimento:** Distribuição Geral $G$.
    * **Resultado:** O número de clientes sendo atendidos no tempo $t$ ($X_t$) e o número de clientes que já saíram ($Y_t$) são variáveis aleatórias independentes, ambas com distribuição de Poisson.