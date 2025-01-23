import os
import importlib.util
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def load_modules(directory="./modules"):
    """
    Dynamically loads all Python modules from the specified directory.

    Args:
        directory (str): Path to the directory containing modules.

    Returns:
        dict: A dictionary where keys are module names and values are module objects.
    """
    modules = {}

    if not os.path.exists(directory):
        print(f"{Fore.RED}Directory '{directory}' does not exist.{Style.RESET_ALL}")
        return modules

    for filename in os.listdir(directory):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]  # Remove the .py extension
            module_path = os.path.join(directory, filename)

            spec = importlib.util.spec_from_file_location(module_name, module_path)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                modules[module_name] = module
                print(f"{Fore.GREEN}Loaded module: {module_name}{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}Failed to load module: {module_name}{Style.RESET_ALL}")

    return modules

    #TODO: Create sub dir loader.


def main():
    print(f"{Fore.CYAN}Module Loader Initialized. Type 'exit' to quit.{Style.RESET_ALL}")
    loaded_modules = {}

    while True:
        # Display available commands
        print(f"\n{Fore.BLUE}Commands:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}  reload{Style.RESET_ALL} - Reload all modules from './modules'.")
        print(f"{Fore.YELLOW}  list  {Style.RESET_ALL} - List all loaded modules.")
        print(f"{Fore.YELLOW}  call  {Style.RESET_ALL} - Call a function from a module (with optional arguments).")
        print(f"{Fore.YELLOW}  exit  {Style.RESET_ALL} - Exit the program.")

        # Get user input
        command = input(f"\n{Fore.CYAN}Enter a command: {Style.RESET_ALL}").strip().lower()

        if command == "reload":
            # Reload modules
            loaded_modules = load_modules()
        elif command == "list":
            # List loaded modules
            if loaded_modules:
                print(f"{Fore.GREEN}Loaded modules:{Style.RESET_ALL}")
                for module_name in loaded_modules:
                    print(f"  - {Fore.YELLOW}{module_name}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}No modules are loaded. Use 'reload' to load modules.{Style.RESET_ALL}")
        elif command == "call":
            # Call a function from a module
            if not loaded_modules:
                print(f"{Fore.RED}No modules are loaded. Use 'reload' to load modules.{Style.RESET_ALL}")
                continue

            module_name = input(f"{Fore.CYAN}Enter module name: {Style.RESET_ALL}").strip()
            if module_name not in loaded_modules:
                print(f"{Fore.RED}Module '{module_name}' is not loaded.{Style.RESET_ALL}")
                continue

            function_name = input(f"{Fore.CYAN}Enter function name: {Style.RESET_ALL}").strip()
            module = loaded_modules[module_name]

            if not hasattr(module, function_name):
                print(f"{Fore.RED}Function '{function_name}' not found in module '{module_name}'.{Style.RESET_ALL}")
                continue

            # Parse arguments
            args = input(
                f"{Fore.CYAN}Enter arguments (comma-separated, leave blank for none): {Style.RESET_ALL}"
            ).strip()
            if args:
                args = [arg.strip() for arg in args.split(",")]  # Convert to list of strings
            else:
                args = []

            function = getattr(module, function_name)
            if callable(function):
                try:
                    result = function(*args)  # Pass arguments dynamically
                    print(f"{Fore.GREEN}Function result: {result}{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Error calling function: {e}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}'{function_name}' is not a callable function.{Style.RESET_ALL}")
        elif command == "exit":
            print(f"{Fore.CYAN}Exiting Module Loader. Goodbye!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid command. Please try again.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()

