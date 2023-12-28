from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Access and print a known environment variable
print("Some other environment variable:", os.getenv("SOME_OTHER_VARIABLE"))
