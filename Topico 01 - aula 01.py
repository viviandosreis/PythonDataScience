#!/usr/bin/env python
# coding: utf-8

# In[6]:


print("Olá mundo!")


# # Bem vindos ao curso de Python para Data Science 
# # Tópico 01 - Aula 01
# 
# **Texto em negrito**
# 
# *Texto itálico*
# 
# _Texto itálico_
# 
# Lista:
# * Item 01
# * Item 02
# * Item 03
#     * Subitem 03
#     
# 1. Item 01
#     1. Subitem 01
#     2. Subitem 02

# In[17]:


import numpy
#isso é um comnetário

idade = 25
idade = idade + 1
nome = "Henrique"
veiculo = "ford"
aluno2 = "luiz"
idade = 2+20*2 #primeiro 20*2 depois soma 2

print("Nome: " + nome)
print(idade)


# In[23]:


#divisão inteira:
10//3

#potencia
8**2

#resto da divisão:
63%4

#casas decimais são separdas por ponto e não por virgula
altura = 1.80

#a virgula é utilizada para separar números a serem atribuidos
idade, altura = 25,1.80
print(idade)
print(altura)

#Quiz: qual o reesultado? R.: 3
7*3**2%4


# In[26]:


#incremento
idade = 25
idade += 1 #idade = idade + 1
print(idade,nome)


# In[28]:


#input - lendo informações do teclado
nome = input("Qual o seu nome?")
print("O seu nome é ",nome)


# In[51]:


#tipo
type(42)

#numeros complexos
type(1+42j)

type(42_00)

#boolean
condição = True
condição = False

float(idade)

#alterando o tipo do dado
idade = float(idade)
type(idade)

bool(1) #true
bool(0) #false
bool("") #false
bool("vivian") #true


# In[104]:


#para texto pode usar "" ou ''
print('meu nome é Vivian')
s = 'meu nome é Vivian'

#quinto caracter
s[4] #'n'

#fatiamento - inclui o limite menor e exclui o maior
s[4:8] #'nome'

#fatiamento de trás para frente
s[4:-2] #'nome é Vivi'

#fatiamento do inicio do texto
s[:-2] #'meu nome é Vivi'

#fatiamento até o ultimo caracter
s[4:] #'nome é Vivian'

#fatiamento parcelado
s[4:15:2] #'nm  ii'


# In[108]:


#string é imutável

#atribuindo string
s = 'meu nome é Vivian'
s = s + ' dos Reis' #meu nome é Vivian dos Reis
print(s)

#tamanho da string
len(s) #26

#procurar: -1 = não consta; diferente de -1 = consta
s.find('Vivian') #11

#substituir
s.replace('Vivian','Maria')

#separar string em pedaços
s.split() #['meu', 'nome', 'é', 'Vivian', 'dos', 'Reis']

#convertendo string - maiuscula
s.upper().find("VIVIAN") #11

#convertendo string - minuscula
s.lower() #'meu nome é vivian dos reis'

#inserir numero dentro da string
s = "minha idade é {} e minha altura é {}".format(42,1.80)
s #'minha idade é 42 e minha altura é 1.8'

#informando os indices
s = "minha idade é {1} e minha altura é {0}".format(42,1.80)
s #'minha idade é 1.8 e minha altura é 42'

#informando os indices e formatando os valores
s = "minha idade é {0} e minha altura é {1:10.3f}".format(42,1.80) #10: espaço;.3f: float
s #'minha idade é 42 e minha altura é      1.800'

#alinhando a esquerda
s = "minha idade é {0} e minha altura é {1:<10.3f}".format(42,1.80)
s #'minha idade é 42 e minha altura é 1.800     '

#alinhando a direita
s = "minha idade é {0} e minha altura é {1:>10.3f}".format(42,1.80)

#centralizado
s = "minha idade é {0} e minha altura é {1:^10.3f}".format(42,1.80)

#tempo médio
get_ipython().run_line_magic('timeit', 's = "minha idade é {0} e minha altura é {1:<10.3f}".format(idade,altura)')
#843 ns ± 1.84 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)


# In[112]:


#python é case senstive
idade =15
Idade = 20
print(idade,Idade)


# In[138]:


#estrutura de repetição if/else
if(idade > 10):
    print("Seu velho")
if(idade <= 10):
    print("Novo ainda")
#Seu velho

if(idade > 90):
    print("Você é muito velho")
else:
    print("Novo ainda")
#Novo ainda

#elif
idade = 95
if(idade > 90):
    print("Você é muito velho")
else:
    if(idade > 10):
        print("um pouco velho")

#outra forma de escrever a função acima:

if(idade > 90):
    print("Você é muito velho")
elif(idade > 10):
    print("um pouco velho")
    
#igual
idade = 18
if(idade == 18):
    print("Você já pode ser preso")

#diferente
idade += 1
if(idade != 18):
    print("Você não tem 18 anos")


# In[142]:


#função ternária
idade = 18
texto = "Já pode ser preso" if (idade >= 18) else "Tá tranquilo"
print(texto)
#Já pode ser preso


# In[147]:


#AND e OR
if(idade < 18 and altura < 2):
    print(texto)
    
if(idade < 18 or altura < 2):
    print(texto)
    #Já pode ser preso


# In[149]:


#WHILE
contador = 10

while(contador > 0):
    contador -= 1
    print("Olá")
#Olá
#Olá
#Olá
#Olá
#Olá
#Olá
#Olá
#Olá
#Olá
#Olá


# In[151]:


#WHILE ELSE
contador = 10

while(contador > 0):
    contador -= 1
    print("Olá")
else:
    print("Mundo")
#Olá
#Olá
#Olá
#Olá
#Olá
#Olá
#Olá
#Olá
#Olá
#Olá
#Mundo


# In[153]:


#WHILE BREAK
contador = 10

while(contador > 0):
    contador -= 1
    print("Olá")
    if(contador == 5):
        break
print("Mundo")

#Olá
#Olá
#Olá
#Olá
#Olá
#Mundo


# In[156]:


#FOR
lista = [2,5,7,9]
for i in lista:
    print(i)
#2
#5
#7
#9

#FOR ELSE
for i in lista:
    print(i)
else:
    print("Acabou")
#2
#5
#7
#9
#Acabou


# 

# In[ ]:




