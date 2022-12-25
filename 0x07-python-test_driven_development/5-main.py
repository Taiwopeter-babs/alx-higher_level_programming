#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

#text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
#Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
"""Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres"""#)
"""text_indentation("\n             Hi, Taiwo.\t        \nDo you mind?\n       \rIf not please see this    : okay           ")"""
text = "And New York is the most beautiful city in the world? It is not far from it. No urban night is like the night there... Squares after squares of flame, set up and cut into the aether. Here is our poetry, for we have pulled down the stars to our will."
text_indentation(text)
