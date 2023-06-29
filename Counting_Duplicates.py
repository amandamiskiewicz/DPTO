def duplicate_count(text):
    character_count = {}
    text = text.lower()

    for character in text:
        if character.isalnum():
            character_count[character] = character_count.get(character, 0) + 1

    duplicate_count = sum(1 for count in character_count.values() if count > 1)
    return duplicate_count