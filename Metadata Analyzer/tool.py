import json
import sys

def unescape_json(escaped_json):
    # Remove the outer quotes and unescape the inner content
    return escaped_json.strip('"').encode().decode('unicode_escape')

def format_json(input_file, output_file):
    try:
        # Read the entire content of the file
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        print(f"File content length: {len(content)} characters")
        
        # Unescape the JSON content
        unescaped_content = unescape_json(content)
        
        # Parse the unescaped JSON content
        parsed_json = json.loads(unescaped_content)
        
        # Write the formatted JSON to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(parsed_json, file, indent=2)
        
        print(f"Formatted JSON has been saved to {output_file}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        print("First 500 characters of the unescaped content:")
        print(unescaped_content[:500])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        format_json(input_file, output_file)