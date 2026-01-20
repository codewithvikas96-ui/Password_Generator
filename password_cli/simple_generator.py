import string
import secrets

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    pools = []
    password = []

    if use_lower:
        pool = string.ascii_lowercase
        pools.append(pool)
        password.append(secrets.choice(pool))

    if use_upper:
        pool = string.ascii_uppercase
        pools.append(pool)
        password.append(secrets.choice(pool))

    if use_digits:
        pool = string.digits
        pools.append(pool)
        password.append(secrets.choice(pool))

    if use_symbols:
        pool = string.punctuation
        pools.append(pool)
        password.append(secrets.choice(pool))

    all_chars = ''.join(pools)

    while len(password) < length:
        password.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password)
    return ''.join(password)


def main():
    print("=" * 10 + " Random Password Generator " + "=" * 10)
    length = int(input("Length (must be >= 8): "))
    upper_case = input("Include Uppercase (y/n): ").lower().startswith('y')
    lower_case = input("Include Lowercase (y/n): ").lower().startswith('y')
    symbols = input("Include Symbols (y/n): ").lower().startswith('y')
    digits = input("Include Digits (y/n): ").lower().startswith('y')

    if length < 8:
        print("Length must be >= 8")
        return

    while True:
        password = generate_password(length, upper_case, lower_case, digits, symbols)
        print(f"Your password: {password}")

        next_round = input("Generate same pass with different chars (y/n)? ").lower()
        if next_round.startswith('n'):
            break


if __name__ == '__main__':
    main()
