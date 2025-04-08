# README - Brute Force Tokenizer

Hey there! This is my little Python project for a brute force tokenizer. I built it to turn text into token IDs and back again, nothing fancy, just something that works. Let me break it down for you.

## What's the Problem?
So, the task was to make a program that takes some text (like "Hello world") and converts it into a list of numbers (token IDs), then turns those numbers back into the original text. It’s super basic—no clever tricks or shortcuts. Just something that gets the job done.

## How I Solved It
I decided to go with a character-based approach. Here’s how I put it together:

1. **Vocabulary**: I made a dictionary of characters—like letters (a-z, A-Z), numbers (0-9), and some punctuation (space, comma, period, etc.). Each one gets a number starting from 0. If the program sees a character that’s not already in the vocabulary, it doesn’t just give up—it dynamically adds that character to the vocabulary and assigns it the next available token ID. Everything gets tracked.

2. **Encoding**: When you type something, it looks at each character. If it’s already in the vocab, it grabs the ID. If it’s new, it adds it to the vocab on the spot and then uses the new ID. This way, even unexpected characters are handled gracefully and consistently.

3. **Decoding**: Takes that list of numbers and turns it back into text by looking up what character each number matches. Since every character encountered during encoding is stored, decoding is reliable.

4. **Running It**: The program asks you for text, shows the numbers, and then shows the text again to prove it works. Type "exit" to stop.

That’s it! Pretty simple, right?

## Why Character-Based Instead of Word-Based?
Okay, so the requirement just said "convert text into token IDs," and I could’ve split the text into words instead—like "Hello" gets one number, "world" gets another. But I went with characters instead, and here’s why:

- **Keeps It Exact**: With words, you’ve got to deal with spaces and punctuation, and when you put it back together, it might not look exactly the same (like "Hello,world" vs "Hello , world"). Characters don’t mess with that—every single letter or symbol stays in place.

- **Simpler for Brute Force**: Word-based needs me to figure out a whole dictionary of words upfront, and what if the user types something new? I’d have to keep adding stuff. Characters are just a fixed set (like A-Z and a few extras), so it’s less hassle. And now, with dynamic vocab, it adds new ones automatically.

- **Matches the Ask**: The task didn’t say anything about fancy word stuff like GPT does—it just wanted text to tokens and back. Characters felt like the most straightforward way to nail that.

So yeah, character-based keeps it dead simple and works every time, which fits the "brute force" vibe I was going for.

## New Hindi Language Support 🇮🇳
Guess what? It now supports **Hindi characters too**! That means you can tokenize and decode Hindi sentences like:

> नमस्ते दुनिया  
> Token IDs: [106, 107, 108, ...]  
> Decoded text: नमस्ते दुनिया

You can even mix Hindi and English together, like:

> Hello नमस्ते!  
> Token IDs: [7, 4, 11, 11, 14, 200, 201, 202, ...]  
> Decoded text: Hello नमस्ते!

This works because we expanded the base character set to include common **Devanagari (Hindi)** characters along with English, symbols, and digits. So now it's fully multilingual—without changing a single line of core logic!

## How to Use It
1. Run the Python file (tokenizer.py or whatever you call it).
2. It’ll say "Enter text to tokenize".
3. Type something like "Hi there!" or "नमस्ते दुनिया" and hit Enter.
4. It’ll show you the token IDs (a list of numbers) and then the text it decodes back to.
5. Keep going or type "exit" to quit.

### Example
> Hello, world!  
Token IDs: [7, 4, 11, 11, 14, 54, 22, 14, 17, 11, 3, 56]  
Decoded text: Hello, world!

## What’s Next?
It’s pretty basic right now. Maybe I could add more characters (like emojis?) or let you save/load the vocab to a file. But for now, it does what it’s supposed to—and better than before!

Happy coding!

(Some random dev who likes simple stuff)