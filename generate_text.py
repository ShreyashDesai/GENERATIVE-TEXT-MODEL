from transformers import pipeline

def main():
    print("\n=== TEXT GENERATION MODEL ===\n")
    
    # Load GPT-2 model
    generator = pipeline("text-generation", model="gpt2")

    # Ask user for topic
    prompt = input("Enter a topic or starting sentence: ")

    print("\nGenerating text...\n")

    # Generate text
    output = generator(prompt, max_length=150, num_return_sequences=1)[0]["generated_text"]

    # Print output
    print("=== GENERATED TEXT ===\n")
    print(output)

    # Save result
    with open("results/generated_text.txt", "w", encoding="utf-8") as f:
        f.write(output)

    print("\nSaved to: results/generated_text.txt")

if __name__ == "__main__":
    main()

