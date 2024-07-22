# Rockyou2024 Password Search Script
This simple Python script is used to search for specific passwords within the rockyou2024.txt file. The rockyou2024.txt file is a commonly used password list for brute-force attacks and other security analyses. This script reads the file in chunks to avoid overwhelming the system's memory, allowing for efficient searching within very large text files.

In case you want to know if your password was leaked.

## How It Works
The script reads the file in binary mode, dividing it into configurable-sized chunks. Each chunk is analyzed line by line to check for the presence of the search term. When a line containing the search term is found, it is displayed in the console. The script also counts and displays the total number of occurrences of the search term.

## Usage
  ### Prerequisites
    - Python 3.x

  ### Instructions
 - Clone the repository or copy the script to your local environment.
 - Ensure that the rockyou2024.txt file is available at the specified path.
 - Run the script with the required arguments:
```	
python search_script.py <file_path> <search_term>
```
<file_path>: The full path to the rockyou2024.txt file (or another file).

<search_term>: The password or term you want to search for within the file.
    
   ### Example
```
    python3 ler.py /your/path/rockyou2024.txt password123
```    
   ### How It Works
    
- Chunk Reading: The file is read in 1 MB chunks (adjustable) to avoid overwhelming memory.
- Line-by-Line Search: Each chunk is split into lines, and the search term is looked for in each line.
- Result Display: Lines containing the search term are displayed in the console.
- Occurrence Count: The total number of occurrences of the search term is displayed at the end of execution.


# Contribution
If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.


