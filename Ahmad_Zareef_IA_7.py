popData = { 'CA': 39.5, 'TX': 30.0, 'FL': 22.2, 'NY': 19.8, 'PA': 13.0, 'IL': 12.8, 'OH': 11.8, 'GA': 10.9, 'NC': 10.7, 'MI': 10.1}

# Define retrieve_pop
def retrieve_pop(region_code, data_dict):
    # Check for existence using the 'in' operator
    if region_code in data_dict:
        return data_dict[region_code]
    else:
        return None


# Define main()
def main():
    # Gather valid codes into a list
    valid_codes_list = []
    for code in popData:
        valid_codes_list.append(code)

    # Store valid codes in list
    valid_codes_display = ""
    for i in range(len(valid_codes_list)):
        code = valid_codes_list[i]
        if i == 0:
            valid_codes_display = code
        else:
            valid_codes_display = f"{valid_codes_display}, {code}"

    # Begin input loop
    while True:
        # Prompt the user for a country code
        user_input = input("Please enter a country code: ")

        # Remove extra whitespace and convert to uppercase
        cleaner_code = user_input.strip().upper()

        # Look up population using the function
        pop_value = retrieve_pop(cleaner_code, popData)

        # If exists, display and end the loop
        if pop_value is not None:
            print(f"{cleaner_code} population = {pop_value}")
            break
        else:
            # Not exist, show error and valid codes
            print(f"Error: '{cleaner_code}' not recognized. Valid codes: {valid_codes_display}")

            # Ask the user if they want to retry
            retry = input("Would you like to try again? (yes/no): ")

            # Continue loop
            if retry == "yes" or retry == "y":
                pass

            else:
                print("Program terminated.")
                break

main()