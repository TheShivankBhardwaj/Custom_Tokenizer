def build_vocabulary():
    # English letters, numbers, symbols + common Hindi (Devanagari) characters
    chars = (
        "abcdefghijklmnopabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        "!@#$%^&*()_+-=[]{}|;:',.<>?/ "
        "ँंःऄअआइईउऊऋॠऌॡएऐओऔकखगघङचछजझञ"
        "टठडढणतथदधनपफबभमयरलवशषसहऺऻ़ऽािीु"
        "ूृॄॢॣेैोौ्॒॑॓॔ॕॖॗॠॡॢॣ०१२३४५६७८९"
    )
    vocab = {char: idx for idx, char in enumerate(chars)}
    inverted_vocab = {idx: char for idx, char in enumerate(chars)}
    return vocab, inverted_vocab

def encode_text(text, vocab, inverted_vocab):
    token_ids = []
    for char in text:
        if char not in vocab:
            new_id = len(vocab)
            vocab[char] = new_id
            inverted_vocab[new_id] = char
        token_ids.append(vocab[char])
    return token_ids

def decode_text(token_ids, inverted_vocab):
    chars = []
    for token_id in token_ids:
        char = inverted_vocab.get(token_id, ' ') 
        chars.append(char)
    return ''.join(chars)

def main():
    vocab, inverted_vocab = build_vocabulary()

    print("Enter text to tokenize (or type 'exit' to quit):")
    while True:
        user_input = input("> ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        token_ids = encode_text(user_input, vocab, inverted_vocab)
        print("Token IDs:", token_ids)

        decoded_text = decode_text(token_ids, inverted_vocab)
        print("Decoded text:", decoded_text)

        print("\nEnter more text (or 'exit' to quit):")

if __name__ == "__main__":
    main()
