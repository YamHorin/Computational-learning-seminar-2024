import os
import subprocess

def install_dependencies():
    subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
    subprocess.check_call(["ollama", "pull", "llama3"])

def main():
    install_dependencies()
    print("Setup complete!")

if __name__ == "__main__":
    main()