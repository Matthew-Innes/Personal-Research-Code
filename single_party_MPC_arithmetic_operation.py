import crypten

def main():
    # Initialize Crypten
    crypten.init()

    # Define the numbers to add
    x = crypten.cryptensor([5.0])
    y = crypten.cryptensor([10.0])

    # Add the encrypted numbers
    encrypted_sum = x + y

    # Decrypt the sum
    decrypted_sum = encrypted_sum.get_plain_text()

    # Print out results
    print("Original numbers:")
    print("x:", x)
    print("y:", y)
    print("Encrypted sum:", encrypted_sum)
    print("Decrypted sum:", decrypted_sum)

if __name__ == "__main__":
    main()
