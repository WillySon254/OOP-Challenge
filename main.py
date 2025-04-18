from pet import Pet

def main():
    # Create pet with sample output
    print("Creating pet: Max")
    pet = Pet("Max")
    
    # Perform actions
    pet.eat()
    pet.play()
    pet.sleep()
    
    # Teach tricks (not shown in sample output but needed for result)
    pet.train("roll over")
    pet.train("play dead")
    
    # Show status
    pet.get_status()

if __name__ == "__main__":
    main()