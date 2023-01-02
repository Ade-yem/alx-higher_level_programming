#!/usr/bin/python3
"""

a function that prints a text with 2 new lines after each of these characters: ., ? and :

"""

def text_indentation(text):
    """
    a function that prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
    text (string): the string to be printed

    """
    if type(text) is not str:
        raise TypeError("text must be a string")
#    tex = text[:]
 #   for d in ".,?:":
  #      text_list = tex.split(d)
   #     tex = ""
    #    for i in text_list:
     #       i = i.strip(" ")
      #      tex = i+ d if tex == "" else tex + "\n\n" + i + d

#    print(tex[:-3], end="")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1
         
        while c < len(text):
            print(text[c], end="")
            if text[c] == "\n" or text[c] in ".?:":
                if text[c] in ".?:":
                    print("\n")
                    c += 1
                    while c < len(text) and text[c] == ' ':
                        c += 1
                        continue
                    c += 1
                     

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
