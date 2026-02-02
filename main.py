'''
#mkdir meu-responde-ai (cria a pasta do projeto)
#c:\Users\lcarl\meu-responde-ai
#cd caminho/para/seu-projeto

.\venv\Scripts\activate(Entra no ambiente virtual)
mkdocs serve (Inicia o MkDocs)
Ctrl + C (Encerrar o MkDocs)
deactivate (Sai do ambiente virtual).

# prompt topicos:
Me retorne em formato markdown o resumo dos topicos presentes no livro.

##
Quais sao os tópicos? Me retorne em markdow, usando # e ## quando necessario. Quero apenas o titulo de cada capitulo




#prompt LM:
"Com base no Capítulo5, descreva o conteúdo presente no livro para que eu utilizarei num site que estou fazendo pra me guiar.


Seja detalhista com o conteúdo,dando exemplos quando conveniente
Formate todas as fórmulas matemáticas usando $ ... $.


Organize em tópicos curtos e use negrito para termos-chave."

#prompt gemini
"Resolva o seguinte exercício de Processos Estocásticos do livro [Nome do Livro]. Estruture a resposta em: Enunciado O que o problema quer? Passo a Passo da Resolução (detalhado) Resposta Final Use LaTeX para todas as fórmulas matemáticas."
'''


'''
#Conectando ao git:
mkdocs gh-deploy





---

## 🛠️ Sobre este Projeto
Este site foi construído utilizando:
* **MkDocs** com tema **Material**.
* **MathJax** para renderização de fórmulas matemáticas em LaTeX.
* **Gemini & NotebookLM** para curadoria de conteúdo e resoluções.
'''