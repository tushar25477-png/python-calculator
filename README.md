# 🧮 Python Scientific Calculator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/CLI-Tool-orange?style=for-the-badge" />
</p>

<p align="center">
  A feature-rich <strong>command-line scientific calculator</strong> built using Python — supports everything from basic arithmetic to trigonometry, logarithms, factorials, and more!
</p>

---

## 📸 Demo

```
========================================
     🧮 PYTHON SCIENTIFIC CALCULATOR
========================================

Select operation:
  1. Add          2. Subtract
  3. Multiply     4. Divide
  5. sin          6. cos
  7. tan          8. log
  9. Power       10. Factorial
 11. Prime Check 12. HCF
 13. Average     14. Exit

Enter choice: 1
Enter first number: 15
Enter second number: 27
✅ Result: 15 + 27 = 42

Use 'ans' to reuse last result.
```

---

## 🚀 Features

| Category              | Operations                                      |
|-----------------------|-------------------------------------------------|
| ➕ Basic Arithmetic    | Addition, Subtraction, Multiplication, Division |
| 📐 Trigonometry        | sin, cos, tan                                   |
| 🔄 Inverse Trig        | asin, acos, atan                                |
| 📊 Logarithm & Exp     | log, log10, e^x                                 |
| ⚡ Power & Factorial   | x^y, n!                                         |
| 🔢 Number Theory       | Prime Check, HCF (GCD)                          |
| 📈 Statistics          | Average of a list                               |
| 💾 Memory              | `ans` stores last result for reuse              |
| 🔁 Continuous Loop     | Keeps running like a real calculator            |

---

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **Module:** `math` (built-in, no installation needed)

---

## ▶️ How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/tushar25477-png/python-calculator.git
cd python-calculator
```

**2. Run the calculator:**
```bash
python calculator.py
```

> ✅ No external libraries required — works out of the box!

---

## 💡 Example Usage

**Basic Addition:**
```
Enter choice: 1
Enter first number: 100
Enter second number: 250
Result: 350.0
```

**Sine of 90 degrees:**
```
Enter choice: 5
Enter angle in degrees: 90
Result: sin(90°) = 1.0
```

**Factorial of 6:**
```
Enter choice: 10
Enter number: 6
Result: 6! = 720
```

**Using `ans` (memory feature):**
```
Enter choice: 9
Enter base: ans        ← reuses previous result
Enter exponent: 2
Result: 720^2 = 518400
```

---

## 📁 Project Structure

```
python-calculator/
│
├── calculator.py      # Main calculator script
└── README.md          # Project documentation
```

---

## 🙌 Author

Made with ❤️ by [Tushar](https://github.com/tushar25477-png)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">⭐ If you found this helpful, please star the repository!</p>
