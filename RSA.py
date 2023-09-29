import random
import math

class RSA:
    def __init__(self, bitlength=8):
        """
        Initializes the RSA object with the specified bitlength for key generation.

        Args:
            bitlength (int, optional): The length of the prime numbers used to generate the keys. 
                Defaults to 8.
        """
        self.bitlength = bitlength

    @staticmethod
    def is_prime(num):
        """
        Check if a given number is prime.

        Args:
            num (int): The number to be checked for primality.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num <= 1:
            return False
        if num == 2 or num == 3:
            return True
        if num % 2 == 0:
            return False
        sqrt_num = math.isqrt(num) + 1
        for i in range(3, sqrt_num, 2):
            if num % i == 0:
                return False
        return True

    def generate_keypair(self):
        """
        Generate a pair of RSA public and private keys.

        Returns:
            tuple: A tuple containing two tuples representing the public key (e, n) and 
                private key (d, n) respectively. e and d are encryption and decryption exponents, 
                and n is the modulus.
        """
        while True:
            p = random.getrandbits(self.bitlength)
            if self.is_prime(p):
                break

        while True:
            q = random.getrandbits(self.bitlength)
            if self.is_prime(q) and p != q:
                break

        n = p * q
        phi = (p - 1) * (q - 1)

        while True:
            e = random.randrange(2, phi)
            if math.gcd(e, phi) == 1:
                break

        d = pow(e, -1, phi)
        return ((e, n), (d, n))

    @staticmethod
    def encrypt(message, public_key):
        """
        Encrypts the given message using RSA encryption algorithm.

        Args:
            message (str): The message to be encrypted.
            public_key (tuple): A tuple containing the public key (e, n), where e is the encryption exponent
                                and n is the modulus.

        Returns:
            list: A list of integers representing the encrypted message.
        """
        e, n = public_key
        encrypted_message = map(lambda char: pow(ord(char), e, n), message)
        return list(encrypted_message)

    @staticmethod
    def decrypt(encrypted_message, private_key):
        """
        Decrypts the given encrypted message using RSA decryption algorithm.

        Args:
            encrypted_message (list): A list of integers representing the encrypted message.
            private_key (tuple): A tuple containing the private key (d, n), where d is the decryption exponent
                                 and n is the modulus.

        Returns:
            str: The decrypted message as a string.
        """
        d, n = private_key
        decrypted_message = ''.join(map(lambda char: chr(pow(char, d, n)), encrypted_message))
        return decrypted_message