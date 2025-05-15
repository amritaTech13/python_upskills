
# keyword "POSSIBLE BREAK-IN ATTEMPT"
# import os
# print(os.path.getsize("SSH.log") / (1024 * 1024), "MB")


def funt():
    key_word = input("Enter the searching keyword name: ")
    log_file_path = 'SSH.log'

    search_data = search_keyword_genrator(key_word, log_file_path)

    result = make_pagination_genrator(search_data,page_size=10)

    while True:
        try:
            search_result =  next(result)
            # print(search_result)

            for line in search_result:
                print(line)

            n = input("type next for next result or type exit to stop it: ")
            if n == 'exit':
                    print("Exit")
                    break
            elif n != 'next':
             print("Invaid input")
             break
        
        except StopIteration:
                print("No more matching")
                break
    

def search_keyword_genrator(key_word,log_file_path):
    with  open(log_file_path , 'r') as file:
        for each_line in file:
            if key_word in each_line:
              yield each_line.strip()
        
def make_pagination_genrator(search_data, page_size=10):
    page_no = []
    for key in search_data:
         page_no.append(key)
         if len(page_no) == page_size:
             yield page_no
             page_no = []
    if page_no:
        yield page_no       
       

# if __name__ == '__main__':
#   main()
funt()






# find below today's real-world scenario task. 
# A demo is attached for reference, along with the large log file required for the task. 
# (The attached log has 19406 lines with the keyword "POSSIBLE BREAK-IN ATTEMPT". 
# We need to search the keyword and get only first 10 and followed by next 10 entries and so on using generators and yield statements) 
# Problem Statement: Log File Keyword Search
# Objective: Implement a Python program that allows users to search for a specific keyword in a large log file
# and retrieve the matching entries in a paginated manner.
# The program should print the first 10 matching entries initially and yield the next set based on user input
 
# Requirements-----------------
# Log File: Assume a log file named `SSH.log` exists, containing multiple log entries,
# each with a timestamp and a message.
 
# Search Functionality:
# Prompt the user to enter a keyword to search for within the log file (e.g. "POSSIBLE BREAK-IN ATTEMPT").
# Display the first 10 entries that contain the keyword.
 
# Pagination:
# After displaying the first 10 entries,
# prompt the user to input a command (e.g., "next") to fetch the next set of 10 entries.
# Continue this process until there are no more matching entries left or the user decides to stop.
 
# Yield Concept:
# Use a generator to yield matching entries in batches of 10, allowing for efficient memory usage.