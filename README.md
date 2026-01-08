# Learning Python with Projects

A comprehensive collection of 30 Python scripts organized by difficulty level, designed to help you learn Python through practical, hands-on projects. Each script comes with detailed requirements documentation (Pflichtenheft) describing functionality, inputs, outputs, and tests.

## 📚 Project Structure

This repository contains 30 Python scripts divided into three difficulty levels:
- **Beginner** (10 scripts): Fundamental Python concepts
- **Advanced** (10 scripts): Intermediate Python skills and popular libraries
- **Expert** (10 scripts): Advanced Python patterns and architectures

Each script is contained in its own directory with:
- `script.py` - The Python implementation
- `Pflichtenheft.md` - Requirements document with functionality, I/O specs, and test cases

## 🎯 Beginner Level

Perfect for those starting their Python journey. Learn basic syntax, data structures, and control flow.

| # | Project | Description |
|---|---------|-------------|
| 01 | [Hello World](beginner/01_hello_world/) | Basic print statements and functions |
| 02 | [Calculator](beginner/02_calculator/) | Simple arithmetic operations |
| 03 | [String Operations](beginner/03_string_operations/) | String manipulation techniques |
| 04 | [List Operations](beginner/04_list_operations/) | Working with lists |
| 05 | [Temperature Converter](beginner/05_temperature_converter/) | Unit conversion (°C, °F, K) |
| 06 | [Palindrome Checker](beginner/06_palindrome_checker/) | String analysis and validation |
| 07 | [Number Guessing Game](beginner/07_number_guessing_game/) | Interactive game logic |
| 08 | [Word Counter](beginner/08_word_counter/) | Text analysis and statistics |
| 09 | [Basic File Reader](beginner/09_basic_file_reader/) | File I/O operations |
| 10 | [FizzBuzz](beginner/10_fizzbuzz/) | Classic programming challenge |

## 🚀 Advanced Level

Build on fundamentals with popular libraries and real-world applications.

| # | Project | Description |
|---|---------|-------------|
| 01 | [Web Scraper](advanced/01_web_scraper/) | Extract data from websites using BeautifulSoup |
| 02 | [API Client](advanced/02_api_client/) | REST API interaction with requests |
| 03 | [Data Analyzer](advanced/03_data_analyzer/) | Data analysis with pandas |
| 04 | [File Organizer](advanced/04_file_organizer/) | Organize files by type and date |
| 05 | [Password Generator](advanced/05_password_generator/) | Secure password generation |
| 06 | [TODO List App](advanced/06_todo_list_app/) | Command-line task manager |
| 07 | [CSV Processor](advanced/07_csv_processor/) | Process and transform CSV data |
| 08 | [JSON Parser](advanced/08_json_parser/) | Parse and manipulate JSON |
| 09 | [Regex Tool](advanced/09_regex_tool/) | Regular expression utilities |
| 10 | [Unit Converter](advanced/10_unit_converter/) | Multi-unit conversion system |

## 💎 Expert Level

Master advanced Python concepts and design patterns.

| # | Project | Description |
|---|---------|-------------|
| 01 | [Async Downloader](expert/01_async_downloader/) | Asynchronous file downloader with asyncio |
| 02 | [Decorator Framework](expert/02_decorator_framework/) | Custom decorator patterns |
| 03 | [Metaclass Validator](expert/03_metaclass_validator/) | Data validation using metaclasses |
| 04 | [Context Manager](expert/04_context_manager/) | Custom context manager implementations |
| 05 | [Thread Pool](expert/05_thread_pool/) | Multi-threaded task executor |
| 06 | [Generator Pipeline](expert/06_generator_pipeline/) | Memory-efficient data processing |
| 07 | [Cache System](expert/07_cache_system/) | LRU cache implementation |
| 08 | [Mini ORM](expert/08_orm_mini/) | Simple Object-Relational Mapper |
| 09 | [Test Framework](expert/09_test_framework/) | Custom testing framework |
| 10 | [Profiler Decorator](expert/10_profiler_decorator/) | Performance profiling tool |

## 🛠️ Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/r14r/Learning_Python_with-Projects.git
cd Learning_Python_with-Projects
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies for advanced scripts:
```bash
# For web scraping
pip install requests beautifulsoup4

# For data analysis
pip install pandas

# For async operations
pip install aiohttp
```

### Running a Script

Navigate to any project directory and run the script:

```bash
cd beginner/01_hello_world
python script.py
```

Each script is self-contained and can be run independently.

## 📖 Learning Path

### Recommended Order:

1. **Start with Beginner**: Complete all 10 beginner scripts to build a solid foundation
2. **Move to Advanced**: Learn libraries and real-world applications
3. **Challenge with Expert**: Master advanced Python patterns

### How to Use Each Project:

1. **Read the Pflichtenheft.md** - Understand what the script should do
2. **Study the script.py** - Analyze the implementation
3. **Run the script** - See it in action
4. **Modify it** - Experiment with changes
5. **Try the tests** - Verify functionality

## 🎓 What You'll Learn

### Beginner Level
- Variables and data types
- Control structures (if/else, loops)
- Functions and parameters
- Lists and dictionaries
- File operations
- Basic error handling

### Advanced Level
- Working with external libraries
- API integration
- Data processing
- Regular expressions
- JSON/CSV manipulation
- Command-line applications

### Expert Level
- Asynchronous programming
- Decorators and metaclasses
- Context managers
- Concurrency and threading
- Generators and iterators
- Design patterns
- Performance optimization

## 📝 Documentation Format

Each `Pflichtenheft.md` includes:

- **Expected Functionality**: What the script does
- **Input**: What data/parameters it accepts
- **Expected Output**: What results it produces
- **Tests**: Sample test cases with expected results
- **Dependencies**: Required Python packages
- **Usage**: How to run the script

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new projects
- Improve existing code
- Add more test cases
- Enhance documentation

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

Created as a comprehensive learning resource for Python developers at all levels.

---

**Happy Learning! 🐍**