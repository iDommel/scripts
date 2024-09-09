import random

def shuffle_list(input_list):
    # Make a copy of the list to avoid modifying the original list
    shuffled_list = input_list[:]
    random.shuffle(shuffled_list)
    return shuffled_list

# Example usage
my_list = ["Raul Ilie",
"Yaman Zaidan",
"Elian Badlisi",
"Ebba Östman",
"Mido Sebai",
"Amed Haji",
"Vasilena Georgieva",
"Elliot Nilsson",
"Lucas",
"Isaías Morales",
"Wiktoria Lewicka",
"Michelle Lam",
"Antwan Badlisi",
"Gustav Sandberg",
"Sherlin Choo",
"Maimuna Jammeh",
"Natalia Lopes",
"Fabio Garcia"]
shuffled = shuffle_list(my_list)
print("Original list:", my_list)
print("Shuffled list:", shuffled)
