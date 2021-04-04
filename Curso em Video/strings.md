![](https://under-linux.org/attachment.php?attachmentid=13468&d=1401234724)
# Manipulação de Strings 
## Fatiamento
```python
>>> string = 'Manipulação de Strings'
```

Toda ***string*** considera-se possível seu fatiamento como a tablea abaixo demonstra:
|M|a|n|i|p|u|l|a|ç|ã|o||d|e||S|t|r|i|n|g|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|


Portanto cada elemento da ***string*** pode ser chamado individualmente como o código abaixo:
```python
>>> print(string[15]) #Trará o caractere 'S' maíusculo
'S'
```
## Métodos disponívels para Strings
* len(**string**): *Retornará o a quantidade de caracteres (iniciando pela posição[0])*
```python
>>> len(string) 
21
```
&nbsp;
* **string**.find('x'): *busca o caractere ou a sentença dentro da string, mostrando qual a primeira posição da busca*
```python
>>> string.find('la') #Retorna qua a sentença 'la' inicia-se na posição 6 dentro da string
6
```
&nbsp;
* **string**.count('x'): *busca quantas vezes o caractere ou a sentença se repete dentro da string
```python
>>> string.count('a') #Retorna qua o caractere 'a' se repete 2 vezes na string
2
```
&nbsp;
* **string**.capitalize(): *tornará toda a string minúscula para então alterar para maiúscula apenas o primeiro caractere da primeira palavra*
```python
>>> string.capitalize('a') #Retorna apenas o primeiro caractere da string em maiúsculo 
'Manipulação de string'
```
&nbsp;
* **string**.replace('x', 'y'): *substitui uma sentença por outra*
```python
>>> string.replace('String', 'Frase') #RSubstitui a sentença 'String' por 'Frase'  
'Manipulação de Frase'
```
&nbsp;
* **string**.strip( ): *remove espaços antes e após a sentença da string*
```python
>>> string.strip() #Imaginando que a string possua a senteça como '   Manipulação de String   ', o método split se encarrega de remover os espaços acidentais
'Manipulação de String'
```
&nbsp;
* **string**.split( ): *separa uma string em uma lista*
```python
>>> string.split() #Cada frase da string será separada em um elemento de uma lista
['Manipulação', 'de', 'String']
```
&nbsp;
* 'x'.join(**string**): *une uma cadeia separada em string de acordo com o separador escolhido*
```python
>>> '-'.join(string) #Cada frase da string será separada pelo caractere escolhido
'Manipulação-de-String'
```
&nbsp;