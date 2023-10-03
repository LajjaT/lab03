def main():
    # part 1

    pets = ['Spot', 'Boots', 'Mrs. Fluffington', 'Lenny', 'Bowser', 'Gina'] #list of pet names
    count = 0 #declare and initialize variable for number of pet names
    pet_name_lengths = [] #list of lengths of pet names

    # TODO: YOUR CODE TO COUNT THE NUMBER OF PETS AND THE LENGTH OF PET NAMES GOES HERE
    for pet_names in pets: #loop through list of pet names
        count = count + 1 #add 1 for each pet name
        name_length = len(pet_names) #count characters in name (excluding '.' and ' ')
        pet_name_lengths.append(name_length) #add length of name to list of lengths of pet names

    #print statements
    print(f'There are {count} pets in the list.')
    print(f'The word lengths of each pet name are {pet_name_lengths}.')

    # part 2

    words = ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog'] #list of words
    word_ratios = [] #create list to store word vowel ratios

    # TODO: YOUR CODE TO COUNT THE NUMBER OF VOWELS AND CONSONANTS IN EACH WORD TO CALCULATE THE RATIOS
    for word in words: #for each word in list of words

        vowel_count = 0 #reset count for number of vowels in word
        consonant_count = 0 #reset count for number of consonants in word

        for letter in word: #check each letter in each word
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u': #if letter is a vowel
                vowel_count += 1 #add 1 to vowel count for the word
        
            else: #if letter is not a vowel
                consonant_count += 1 #add 1 to consonant count for the word
        
        vowel_to_consonants_ratio = vowel_count / consonant_count #calculate vowel to consonant ratio for the word

        word_ratios.append(vowel_to_consonants_ratio) #append calculated ratio to list
        
    #print statement
    print(f"The vowel to consonant ratios of each word are {word_ratios}.")

if __name__ == "__main__":
    main()