import json
import subprocess

def create_image_urls(backStr, frontStr, number):
    # Base URL for constructing the image URLs
    base_url = f"https://master-cards.s3.eu-west-2.amazonaws.com/{frontStr}/"
    
    # List comprehension to generate each item in the list
    card_urls = [
        {
            "backImgUrl": f"{base_url}{backStr}_{i}.jpg" if backStr is not None else None,
            "frontImgUrl": f"{base_url}{frontStr}_{i}.jpg"
        }
        for i in range(1, number + 1)
    ]
    
    # Convert the list to a JSON string
    json_output = json.dumps(card_urls, indent=2)
    
    # Copy the JSON output to the clipboard using clip command on Windows
    subprocess.run('clip', universal_newlines=True, input=json_output)
    
    # Return the JSON string and print message
    print("JSON has been copied to the clipboard.")
    return json_output

# Example usage
backStr = None
frontStr = "ways"
number = 95
result = create_image_urls(backStr, frontStr, number)
print(result)
