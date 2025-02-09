# 2025-ITELEC2-LAB004
Week 02 - Python Variables, Operators and I/O Statements

Laboratory # 04 - Guided Coding Exercise: Input, Output, and Text Formatting in Python

## **Instructions**

### **Step 1.1: Accept the Assignment**

   1. Click on the assignment link provided by your instructor.
   2. GitHub Classroom will create a **private repository** under your GitHub account.
   3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
Only perform this if this is the first time you will setup your Git Environment

   1. Create a GitHub Account:
   ```bash
   https://github.com/signup?source=login
   ```
      
   2. Download and Install Git on your Laptop/Desktop:
   ```bash
   https://git-scm.com/downloads
   ```
   
   3. Create a Folder in your Laptop/Desktop
   4. Right-click anywhere in the created folder and select "Open Git Bash Here".
   5. In the Git Bash Terminal, set your git name, perform command:
   ```bash
   git config --global user.name "Your Name"
   ```
   
   6. In the Git Bash Terminal, set your git email, perform command:
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   
   7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase. In the Git Bash Terminal, perform command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   
   8. Copy your SSH Keys into clipboard. In the Git Bash Terminal, perform command:
   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```
   
   9. Log in to your GitHub account.
   10. In the upper-right corner of GitHub, click your profile picture and select Settings.
   11. In the left sidebar, click on SSH and GPG keys.
   12. Click the New SSH key button.
   13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
   14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
   15. Go Back to terminal, use command:
   ```bash
   ssh -T git@github.com
   ```

### **Step 2: Clone the Repository to Your Local Machine**

   1. On your repository page, click the green **"Code"** button.
   2. Copy the repository URL (choose HTTPS for simplicity).
   3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:
   
   ```bash
   git clone <git_repo_url>
   ```
   
   4. Navigate into the cloned folder:
   
   ```bash
   cd <git_cloned_folder>
   ```

### **Step 3: Complete the Assignment**

**Laboratory # 04 - Guided Coding Exercise: Input, Output, and Text Formatting in Python**

   **Objective:**
      1. Get input from the user using the `input()` function.
      2. Convert user input (which is initially a string) to the correct data type (integer or float).
      3. Display formatted output using old-style string formatting (the % operator).

   **Desired Output (Example - will vary based on user input):**
   
```bash
Enter an integer: 123
Enter a decimal number: 3.14159
Enter a string: Hello, Python!
Formatted Output using old-style formatting:
Integer: 123
Decimal: 3.14
String: Hello, Python!
Formatted Output using f-strings:
Integer: 123
Decimal: 3.14
String: Hello, Python!
```
*Note: The decimal number should be formatted to two decimal places in both output styles.*
      
   **Notable Observations (to be discussed after completing the exercise):**
   - Data Type Conversion: The input() function returns a string; therefore, it is essential to convert the input to the appropriate type (using int() for integers and float() for decimals). Failing to do so would prevent arithmetic operations or correct formatting.
   - Old-Style Formatting vs. f-Strings:
      - Old-style formatting uses specifiers such as %d (integer), %.2f (float with two decimal places), and %s (string).
      - f-Strings, introduced in Python 3.6, provide a more readable and flexible way to format strings, including inline arithmetic and formatting.
   - Formatting Specifiers: The specifier %.2f rounds the decimal number to two decimal places, ensuring that the output is neat and consistent.
   - User Experience: Clear prompts and formatted outputs enhance the user experience and reduce the likelihood of input errors.

   **Python Best Practices**
   - Input Validation: Always validate and convert user inputs to the correct data types to prevent runtime errors.
   - Consistent Formatting: Use consistent formatting practices throughout your code. While old-style formatting is still supported, favor modern f-strings for clarity and brevity.
   - Readable Code: Include clear prompts and descriptive variable names to improve code readability.
   - Commenting: Add comments where necessary to explain the purpose of each code section, especially when performing type conversions and formatting.
   - Modular Code: Structure your code in logical blocks (input, processing, output) to make it easier to maintain and update.

   **Step-by-Step Instructions:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `exercise_02.py`
      
   2.  Get integer input:
       - Use the `input()` function to prompt the user to enter an integer. Store the returned value in a variable named `user_integer`.
       - *Crucially*, convert the input string to an integer using the `int()` function.

```python
user_integer = int(input("Enter an integer: "))
```
      
   4. Get decimal (float) input:
      - Use the `input()` function to prompt the user to enter a decimal number. Store the returned value in a variable named `user_decimal`.
      - *Crucially*, convert the input string to a float using the `float()` function.
```python
user_decimal = float(input("Enter a decimal number: "))
```

   5. Get string input:
      - Use the `input()` function to prompt the user to enter a string. Store the returned value in a variable named `user_text`. No conversion is needed here, as `input()` already returns a string.
```python
user_text = input("Enter a string: ")
```

   6. Display formatted output (old-style):
      - Use the `print()` function along with the `%` operator to display the values of the three variables in a formatted way.
      - Use `%d` as the format specifier for the integer, `%.2f` for the decimal (formatted to two decimal places), and `%s` for the string.
```python
print("Formatted Output using old-style formatting:")
print("Integer: %d" % user_integer)
print("Decimal: %.2f" % user_decimal)
print("String: %s" % user_text)
```

   7. Display formatted output (f-strings - Modern Approach):
      - Use an f-string to display the same information. F-strings are more readable and generally preferred.
```python
print("Formatted Output using f-strings:")
print(f"Integer: {user_integer}")
print(f"Decimal: {user_decimal:.2f}")  # Format decimal to two places
print(f"String: {user_text}")
```

   8. Run the code:
   - Save the file and execute your script by running:
   ```bash
   python exercise_02.py
   ```
   - Verify that your output matches the desired output.

   9. Discussion (Notable Observations):  
   - Why is it essential to convert the input to the correct data type? What would happen if you tried to perform arithmetic operations on the string input directly?
   - Explain the difference between %d, %.2f, and %s in old-style formatting.
   - Explain how f-strings work. Why are they often preferred over old-style formatting? How do you format the decimal places in an f-string?

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
   Open the terminal and run:
   
```bash
git status
```
   This command shows any modified or new files.
   
2. Stage the changes:
   Add all modified files to staging:
   
```bash
git add .
```
   
3. Commit your changes:
   Write a meaningful commit message:
   
```bash
git commit -m "Submitting Python Week 02 - Session 01 - Exercise 02"
```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
```bash
git push origin main
```
