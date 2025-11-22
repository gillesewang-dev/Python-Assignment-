guests = ["Isaac Newton", "Nelson Mandela", "Oprah Winfrey"]

print("Good news! I found a bigger dinner table! ")

guests.insert(0, "Leonardo da vinci ")
guests.insert(len(guests)//2, "Marie Curie")
guests.append("Elon Musk")

for guest in guests:
    print(f"Hello {guest}, you are invited to dinner!")