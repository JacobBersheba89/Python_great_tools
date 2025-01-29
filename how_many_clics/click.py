import mouse

click_count = 0  # Počítadlo kliknutí

def on_click(event):
    global click_count
    click_count += 1
    print(f"Počet kliknutí: {click_count}")

# Připojení listeneru
mouse.on_click(on_click)

print("Sleduji kliknutí! Klikni kdekoliv a sleduj terminál.")

# Nekonečná smyčka, aby program běžel
mouse.wait()
