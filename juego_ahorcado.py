import os
import random
import sys
import unidecode


#remueve acentos
def remove_accents(text):
	outputString = unidecode.unidecode(text)
	return outputString

#limpia la pmatalla
def screen_clear():
    return os.system('clear')

#lee archivo y devyelve una lista de palabras
def find_words_in_file():
    all_words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            all_words.append(line.strip())
    return all_words

#encuentra la letra en la palabra, y retorna una lista de la palabra con la letra encobtrada
def find_letter_in_word(list_choice_word, copy_list_choice_word, input_user):
    found_letter = False   
    for i in range(0,len(list_choice_word)):
        if remove_accents(list_choice_word[i].lower()) == remove_accents(input_user.lower()): #Sensitive Case y acentos
            copy_list_choice_word[i] = list_choice_word[i] 
            found_letter = True

    word_game = {
        "list_word": copy_list_choice_word,
        "found": found_letter
    }
    return word_game

#imprime la letra con formato ahorcado
def put_word_line(list_word):
    print("  ")
    for i in range(0,len(list_word)):
        if list_word[i] == False:
            sys.stdout.write("_ ")
        else:
            sys.stdout.write(list_word[i]+" ")

def ahorcado(input_user, list_choice_word, copy_list_choice_word):
    list_word = find_letter_in_word(list_choice_word, copy_list_choice_word, input_user)
    put_word_line(list_word['list_word'])
    return list_word

#retorna una lista copia  de posiciones de la palabra original con una pista ejemplo; C a s a: False False s Falsa 
def initial_compare_word(list_choice_word, copy_list_choice_word):
    for i in range(0,len(list_choice_word)):
        copy_list_choice_word.append(False)

    #encontrar una pista
    index_pista = list_choice_word.index(random.choice(list_choice_word))
    copy_list_choice_word[index_pista] = list_choice_word[index_pista]

    return copy_list_choice_word

def draw_ahorcado(count_fail, intentos):
    if count_fail==1:
        print("Dibujar Base ")
    elif count_fail == 2:
        print("Dibujar Cabeza ")
    elif count_fail == 3:
        print(" Dibujar Cuerpo ")
    elif count_fail == 4:
        print("Dibujar brazo izq")
    elif count_fail == 5:
        print("Dibujar brazo derch")
    elif count_fail == 6:
        print("Dibujar pierna izq ")
    elif count_fail == 7:
        print("Dibujar pierna derch ")
    elif count_fail == 8:
        print("Dibujar cuerda(DEAD) ")


def ingresar_letra():
    print(" \n Adivina la Palabra")
    copy_list_choice_word = []
    get_words = find_words_in_file()
    choice_word = (random.choice(get_words)) #"embarcación" 
    list_choice_word = list(choice_word) #convierte la palabra en una lista
    #print(list_choice_word)
    copy_list_choice_word = initial_compare_word(list_choice_word, copy_list_choice_word)
    put_word_line(copy_list_choice_word)
    count_fail = 0
    intentos = 8
  
    while copy_list_choice_word != list_choice_word and count_fail < intentos: 
        try:
            if count_fail > 0:
                print(" \n\n "+" has fallado "+str(count_fail)+" veces (te quedan "+str(intentos-count_fail) + " intentos)")
                
            letra = input(" \n \n Ingresa una letra: ")
            if (not letra.isalpha()):
                raise ValueError("Debes ingresar una letra")
            else:
                screen_clear()
                return_ahorcado = ahorcado(letra, list_choice_word, copy_list_choice_word)
                copy_list_choice_word = return_ahorcado['list_word']

                if (copy_list_choice_word == list_choice_word):
                     print(" \n \n GANASTE!! La palabra es: "+choice_word + "\n\n")  
                elif (return_ahorcado["found"] == False):
                    count_fail += 1  
                    print(" \n \n ")
                    draw_ahorcado(count_fail,intentos)
                    if (count_fail >= 8):
                        print(" \n \n ")
                        print(" PERDISTE!!! demasiados intentos")
                        print("La palabra era: "+choice_word)
                        
                        print(" \n \n ")

                    
        except ValueError as ve:
            print(ve)



def run():
    ingresar_letra()
    #ingresar_letra()

if __name__ == '__main__':
    run()