# StegoRecover
A Python script to brute-force steghide password

Steghide is a steganography program that allows to hide data in various kinds of image files. It requires a password to hide and extract the data. Maybe you forgot the password, so you can brute-force it with the help of a wordlist to recover it. Attention: Use for educational purpuoses only.

It borns as an attempt to automate the recovering of the password for the "cute-alien.jpg" file in the machine "Agent Sudo" for the platform TryHackMe.

Usage: python stegorecover.py steg_file wordlist_file

steg-file: The file with hidden info that requires a password to be extracted.

wordlist_file: Path to a wordlist of possible passwords.

It uses the command "steghide extract -sf STEG_FILE -p PASSWORD" to try each password into the file. So, when it founds the right password, it automatically extracts the hidden info to the current folder.

![alt text](https://github.com/blu3ming/StegoRecover/blob/main/images/stegorecover.png?raw=true)
