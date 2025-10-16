import random
import time

# Список цитат (можно дополнять)
QUOTES = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "Your time is limited, don’t waste it living someone else’s life. – Steve Jobs",
    "If you want to achieve greatness stop asking for permission. – Anonymous",
    "Dream bigger. Do bigger. – Anonymous",
    "The harder you work for something, the greater you’ll feel when you achieve it. – Unknown"
]

def show_random_quote():
    """Выводит случайную цитату."""
    quote = random.choice(QUOTES)
    print("\n💬 Random Quote:\n")
    print(f"“{quote}”\n")

def main():
    print("✨ Welcome to Random Quotes Generator ✨")
    time.sleep(0.5)
    while True:
        show_random_quote()
        again = input("Generate another one? (y/n): ").strip().lower()
        if again != "y":
            print("\n👋 Thanks for using Random Quotes Generator!")
            break
        print()

if __name__ == "__main__":
    main()

## to Launch the file - python main.py/python3 main.py
