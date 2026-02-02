# Exercícios Resolvidos: Cadeias de Markov em Tempo Contínuo

Esta página contém resoluções detalhadas dos tópicos abordados no Capítulo 3, focando em matrizes de intensidade e modelos de filas.

---

## 1. Construção da Matriz Geradora ($Q$) { #ex31 }

**Enunciado:** Um sistema pode estar em três estados: Funcionando (1), Alerta (2) e Falha (3). As taxas de transição são: de 1 para 2 é $0.5/\text{h}$, de 2 para 1 é $0.2/\text{h}$, de 2 para 3 é $0.8/\text{h}$ e de 3 para 1 é $1.0/\text{h}$. Monte a matriz geradora $Q$.

**Resolução:**
Lembrando que as entradas fora da diagonal são as taxas $q_{ij}$ e as entradas da diagonal são $q_{ii} = -\sum_{j \neq i} q_{ij}$.

1. **Taxas de saída:**
   * Do estado 1: $\lambda_1 = q_{12} = 0.5 \implies q_{11} = -0.5$.
   * Do estado 2: $\lambda_2 = q_{21} + q_{23} = 0.2 + 0.8 = 1.0 \implies q_{22} = -1.0$.
   * Do estado 3: $\lambda_3 = q_{31} = 1.0 \implies q_{33} = -1.0$.

**Resultado:**
$Q = \begin{pmatrix} -0.5 & 0.5 & 0 \\ 0.2 & -1.0 & 0.8 \\ 1.0 & 0 & -1.0 \end{pmatrix}$



---

## 2. Distribuição Estacionária ($\pi$) em Tempo Contínuo { #ex32 }

**Enunciado:** Calcule a distribuição estacionária para a matriz geradora:
$Q = \begin{pmatrix} -2 & 2 \\ 3 & -3 \end{pmatrix}$

**Resolução:**
Resolvemos o sistema $\pi Q = 0$ com $\pi_1 + \pi_2 = 1$.
1. $-2\pi_1 + 3\pi_2 = 0 \implies 3\pi_2 = 2\pi_1 \implies \pi_1 = 1.5\pi_2$.
2. $1.5\pi_2 + \pi_2 = 1 \implies 2.5\pi_2 = 1 \implies \pi_2 = 0.4$.
3. $\pi_1 = 1 - 0.4 = 0.6$.

**Resultado:** $\pi = (0.6, 0.4)$.

---

## 3. Filas M/M/1: Equilíbrio e Performance { #ex33 }

**Enunciado:** Clientes chegam a um guichê (M/M/1) com taxa $\beta = 4/\text{h}$ e são atendidos com taxa $\mu = 5/\text{h}$. Calcule a probabilidade de o guichê estar vazio e o número médio de clientes no sistema.

**Resolução:**
1. **Fator de utilização ($\rho$):**
   $\rho = \beta/\mu = 4/5 = 0.8$.
2. **Probabilidade de estar vazio ($\pi_0$):**
   $\pi_0 = 1 - \rho = 1 - 0.8 = 0.2 \text{ (ou 20%)}$.
3. **Número médio de clientes ($L$):**
   $L = \rho / (1 - \rho) = 0.8 / 0.2 = 4$ clientes.



---

## 4. Cadeia Imersa e Probabilidades de Salto { #ex34 }

**Enunciado:** Dada a matriz $Q$ do Exercício 1, qual a probabilidade de o sistema, ao sair do estado de Alerta (2), ir para o estado de Falha (3)?

**Resolução:**
Na cadeia imersa, as probabilidades de transição são dadas por $\tilde{p}_{ij} = q_{ij} / \lambda_i$.
1. Taxa total de saída do estado 2: $\lambda_2 = 1.0$.
2. Taxa de 2 para 3: $q_{23} = 0.8$.
3. $\tilde{p}_{23} = 0.8 / 1.0 = 0.8$.

**Resultado:** A probabilidade é de $80\%$.