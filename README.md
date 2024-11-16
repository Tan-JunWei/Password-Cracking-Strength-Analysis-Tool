# Password Cracking & Strength Analysis Tool

This project simulates various password cracking techniques to provide a realistic assessment of password security.
Unlike conventional password checkers, which only evaluate password complexity based on rules, this tool tests passwords against real-world cracking methods, offering practical insights into password strength.

![Password Analysis Tool](Assets/main.png "Screenshot of Main Page")

## Features

### Multi-Method Cracking Simulation
- Dictionary Attack: Tests passwords against a wordlist (W.g. `rockyou.txt`) by hashing each word and comparing it with the target password hash.
- Brute Force Attack: Generates possible alphanumeric passwords within the specified range of lengths to match the hashed password. Special characters (E.g. `#`, `*`, `?`) may also be used by modifying the character set.

<div align="center">
    <img src="Assets/attack_example.png" alt="Screenshot of Password Cracking" width="700"/>
    <h4>Example of Password Cracking</h4>
</div>


### Password Strength Analysis
- Entropy Calculation: Uses password entropy formula to evaluate password strength in bits based on its length and character variety (E.g. digits, uppercase/lowercase characters).

The entropy is calculated as:

$$
E = \log_2(R^L)
$$

Where:
- \( R \): Range of possible characters.
- \( L \): Length of the password.


### Detailed Feedback
- Estimated Time to Crack: Outputs the time taken for each attack and the total number of attempts made.


## Installation
1. Clone the repository:
```bash
git clone <link>
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the tool:
```bash
python password_analysis.py
```
