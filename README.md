# 📚 Programming with Python Lab (BT CS 526)

> Complete portfolio of 20 production-grade Python laboratory programs implementing foundational to advanced computing concepts: String manipulation, Functional programming, Data structures, OOP inheritance, Object persistence, Concurrency, SQLite database integration, and Scientific data analytics.

<div align="center">

![Python](https://img.shields.io/badge/Language-Python%203-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Semester](https://img.shields.io/badge/Semester-5th-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

</div>

---

## 🧪 Lab Programs Overview

| Lab No. | Program Title                                                  | File Name   | Key Concepts                                           |
| :-----: | :------------------------------------------------------------- | :---------- | :----------------------------------------------------- |
|    1    | Dynamic Command-Line Caesar Cipher Tool                        | `lab1.py` | String Slicing, ASCII Conversion, Modular Shift Arithmetic |
|    2    | Automated Word Frequency and Pattern Analyzer                  | `lab2.py` | Punctuation Stripping, Frequency Dictionaries, Palindrome Slicing |
|    3    | Automated CSV File Inspector and Data Exporter                 | `lab3.py` | CSV/TSV Ingestion, Shape Profiling, Datatype Inference, Data Export |
|    4    | Interactive Command-Line Task Scheduler with Lazy Evaluation   | `lab4.py` | Collections Deque, Lazy Evaluation Closures, Conditional Queue Dispatch |
|    5    | Robust File Management and Directory Navigation Utility        | `lab5.py` | OS Module, Path Traversal, Workspace Provisioning, Defensive Logging |
|    6    | Dynamic Phonebook and Contact Directory Manager                | `lab6.py` | Nested Dictionaries, CRUD Operations, Comprehension Pattern Search |
|    7    | Functional Data Filtering and Matrix Transformation Suite      | `lab7.py` | Functional Map, Filter, Lambda, Row Sorting, Matrix Transposition |
|    8    | Custom Flexible Student Grade and Statistics Calculator        | `lab8.py` | Variable Arguments (*args, **kwargs), Statistical Aggregation, Grading Scale |
|    9    | Text Anagram and Pattern Matcher Tool                          | `lab9.py` | Collections Counter, Canonical Pattern Hashing, Anagram Clustering |
|   10    | In-Memory Inventory Tracker with Dictionary Merging            | `lab10.py` | Multi-Store Dictionary Merge, Union Operator (|=), Threshold Stock Warnings |
|   11    | Interactive Turtle Pattern Generator and Fractal Renderer      | `lab11.py` | Recursive Geometry (Koch Snowflake), Fractal Graphics, Parametric Spirals |
|   12    | Digital Image Filter and Color Converter Utility               | `lab12.py` | RGB Luminosity Conversion, Binary Thresholding, 3x3 Box Blur Convolution |
|   13    | Encapsulated Banking System with Inheritance Models            | `lab13.py` | OOP Encapsulation, Method Overriding, Polymorphism, Overdraft Current Accounts |
|   14    | Object Persistence Engine via Serialization                    | `lab14.py` | Binary Pickle Serialization, Disk-Backed Shelve Key-Value Persistence |
|   15    | Abstract Shape Math Engine with Operator Overloading           | `lab15.py` | Abstract Base Classes (ABC), Geometric Interfaces, 2D Vector Operator Overloading |
|   16    | Safe File Processor with Custom Exception Hierarchy            | `lab16.py` | Custom Domain Exceptions, Try-Except-Else-Finally, Traceback Logging |
|   17    | Regular Expression Pattern Matcher and Information Extractor   | `lab17.py` | Regular Expressions, Email/URL/Phone Extraction, Log Tokenization |
|   18    | Relational Database Management System via SQLite Engine        | `lab18.py` | SQLite Engine, Table Schemas, Parameterized SQL Queries, CRUD Transactions |
|   19    | Multithreaded Concurrent Task Pipeline with Thread Synchronization | `lab19.py` | Threading Module, Thread-Safe Queues, Mutual Exclusion Locks (Mutex) |
|   20    | Scientific Data Analytics and Statistical Visualization Suite  | `lab20.py` | Descriptive Moments, Pearson Correlation, Console Distribution Histograms |

---

## 🎯 Learning Objectives

This laboratory curriculum covers the complete spectrum of Python software engineering across 6 progressive modules:

### 1. Foundational Python & String Processing
- ✅ Modular arithmetic & ASCII transformation in cryptography (Caesar Cipher)
- ✅ Punctuation normalization, tokenization & frequency analysis
- ✅ High-speed palindrome checking using string slicing

### 2. Tabular Data & Operating System Automation
- ✅ Automated CSV/TSV structural parsing and datatype inference
- ✅ Lazy evaluation and deferred task scheduling via `collections.deque`
- ✅ Filesystem traversal, directory creation & defensive file logging with `os`

### 3. Data Structures & Functional Paradigms
- ✅ Interactive CRUD contact management with nested dictionaries
- ✅ Pure functional transformations with `map()`, `filter()`, and `lambda`
- ✅ Dynamic variable arguments (`*args`, `**kwargs`) and grade distribution
- ✅ Canonical pattern hashing & anagram clustering with `collections.Counter`
- ✅ Multi-store dictionary merging using Python 3.9+ union operators (`|` and `|=`)

### 4. Computational Graphics & Signal Processing
- ✅ Recursive fractal geometry (Koch Snowflake) and parametric spirals
- ✅ Digital image filters: luminosity grayscale conversion, binary thresholding, and 3x3 convolution blur kernels

### 5. Object-Oriented Architecture & Persistence
- ✅ Encapsulation, inheritance hierarchies, and method overriding in banking systems
- ✅ Defensive overdraft handling and polymorphic account dispatch
- ✅ Object serialization using binary `pickle` streams and `shelve` persistent stores
- ✅ Abstract base classes (`abc.ABC`) and mathematical operator overloading (`Vector2D`)

### 6. Robust Engineering, Systems & Advanced Python
- ✅ Hierarchical custom exception architecture and traceback error logging
- ✅ Complex regular expression pattern matching, token extraction, and log parsing
- ✅ Relational database programming with embedded `sqlite3` and parameterized queries
- ✅ Multithreaded concurrent task execution with mutex synchronization (`threading.Lock`)
- ✅ Scientific descriptive statistics, Pearson correlation, and high-resolution ASCII distribution histograms

---

## 📥 Quick Start Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vikasingh0897/Python-Lab-Repo.git
cd Python-Lab-Repo
```

### 2️⃣ Run Any Program

All 20 programs are completely standalone, interactive, and accept input directly:

```bash
# Run Caesar Cipher Tool
python lab1.py

# Run Relational SQLite Manager
python lab18.py

# Run Multithreaded Task Pipeline
python lab19.py
```

### 3️⃣ Sample Interactive Run (`lab1.py`)

```text
Enter text: Hello World!
Enter shift key: 3
Enter E to encrypt or D to decrypt: E
Result: Khoor Zruog!
```

### 4️⃣ Batch Test All Programs (PowerShell)

```powershell
1..20 | ForEach-Object { Write-Host "`n=== Testing lab$_.py ===" -ForegroundColor Cyan; python "lab$_.py" }
```

---

## 📁 Repository Structure

```
Python/
│
├── reference/
│   ├── Images/
│   │   ├── CUH_Logo.png
│   │   └── snowflakes.png
│   ├── Layout/
│   │   ├── headerfooter.tex
│   │   └── titlepage.tex
│   ├── Sections/
│   │   ├── program-1.tex ... program-20.tex
│   │   └── ...
│   ├── main.tex
│   └── readme.md
│
├── lab1.py            (Dynamic Command-Line Caesar Cipher Tool)
├── lab2.py            (Automated Word Frequency and Pattern Analyzer)
├── lab3.py            (Automated CSV File Inspector and Data Exporter)
├── lab4.py            (Interactive Command-Line Task Scheduler with Lazy Evaluation)
├── lab5.py            (Robust File Management and Directory Navigation Utility)
├── lab6.py            (Dynamic Phonebook and Contact Directory Manager)
├── lab7.py            (Functional Data Filtering and Matrix Transformation Suite)
├── lab8.py            (Custom Flexible Student Grade and Statistics Calculator)
├── lab9.py            (Text Anagram and Pattern Matcher Tool)
├── lab10.py           (In-Memory Inventory Tracker with Dictionary Merging)
├── lab11.py           (Interactive Turtle Pattern Generator and Fractal Renderer)
├── lab12.py           (Digital Image Filter and Color Converter Utility)
├── lab13.py           (Encapsulated Banking System with Inheritance Models)
├── lab14.py           (Object Persistence Engine via Serialization)
├── lab15.py           (Abstract Shape Math Engine with Operator Overloading)
├── lab16.py           (Safe File Processor with Custom Exception Hierarchy)
├── lab17.py           (Regular Expression Pattern Matcher and Information Extractor)
├── lab18.py           (Relational Database Management System via SQLite Engine)
├── lab19.py           (Multithreaded Concurrent Task Pipeline with Thread Synchronization)
├── lab20.py           (Scientific Data Analytics and Statistical Visualization Suite)
│
├── .gitignore         (Git Ignore configuration for Python and LaTeX artifacts)
└── README.md          (This Documentation)
```

---

## 👤 About Me

<div align="center">

### **Vikas Singh**

[![GitHub](https://img.shields.io/badge/GitHub-vikasingh0897-black?style=for-the-badge&logo=github)](https://github.com/vikasingh0897)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/vikasingh0897)

<table align="center">
  <tr>
    <td align="center" width="200">
      <img src="https://github.com/vikasingh0897.png" width="150" alt="Vikas Singh" style="border-radius: 50%; border: 4px solid #007ACC;"/>
      <br>
      <a href="https://github.com/vikasingh0897"><b>@vikasingh0897</b></a>
    </td>
    <td width="500">
      <h2 align="center">🚀 Student Profile</h2>
      <hr>
      <p><b>👤 Name:</b> Vikas Singh</p>
      <p><b>🆔 Roll No:</b> 241504</p>
      <p><b>🎓 Course:</b> B.Tech in Computer Science & Engineering</p>
      <p><b>🏛️ University:</b> Central University of Haryana</p>
      <p><b>📅 Status:</b> Student</p>
    </td>
  </tr>
</table>

</div>

---

<div align="center">

## 🎓 Course Information

| Detail           | Information                                             |
| ---------------- | ------------------------------------------------------- |
| **Course Title** | Programming with Python Lab                             |
| **Course Code**  | BT CS 526                                               |
| **Semester**     | 5th Semester                                            |
| **University**   | Central University of Haryana                           |
| **Department**   | Department of Computer Science & Engineering            |
| **Instructor**   | Mr. Anant R. Bara (Assistant Professor, CSE Department) |
| **Type**         | Practical Lab Assignment                                |

---

## 🏛️ Acknowledgments

> This repository serves as comprehensive documentation for the **Programming with Python Lab (BT CS 526)**.  
> Developed under the guidance of **Mr. Anant R. Bara**, Department of Computer Science & Engineering.

**Course:** Programming with Python Lab (BT CS 526) <br>
**Department:** Department of Computer Science & Engineering <br>
**University:** Central University of Haryana <br>

</div>

---

<div align="center">

### ⭐ If this repository helps you, please give it a star! ⭐

**Happy Coding! 🚀**

</div>
