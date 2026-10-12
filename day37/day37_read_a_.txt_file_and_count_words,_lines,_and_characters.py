while True:
    file_name = input("Enter file name (or q to quit): ")

    if file_name.lower() == "q":
        print()
        print("Bye")
        print()
        break

    try:
        with open(file_name, "r") as file:
            text = file.read()

    except FileNotFoundError:
        print()
        print(f"File '{file_name}' not found.")
        print("Enter a valid file name.")
        print()
        continue

    # Count lines, words, and characters
    lines = text.splitlines()
    words = text.split()
    characters = len(text)

    # Count non-empty lines
    non_empty_lines = sum(1 for line in lines if line.strip())

    print()
    print("----------------------------------------")
    print(f"Lines: {len(lines)}")
    print(f"Words: {len(words)}")
    print(f"Characters: {characters}")
    print(f"Non-empty lines: {non_empty_lines}")

    # Find the longest word
    if words:
        longest_word = max(words, key=len)
        print(f"Longest word: {longest_word}")
    else:
        print("Longest word: No words found.")

    # Count word frequencies, ignoring case and punctuation
    word_counts = {}

    for word in words:
        word = word.lower().strip(".,!?;:\"'()[]{}")

        if word:
            word_counts[word] = word_counts.get(word, 0) + 1

    # Find the most common word
    if word_counts:
        most_common = max(word_counts, key=word_counts.get)
        print(f"Most common word: {most_common} ({word_counts[most_common]} times)")
    else:
        print("Most common word: No words found.")

    print("----------------------------------------")
    print()
