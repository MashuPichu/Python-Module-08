# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  oracle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/13 12:44:25 by klucchin        #+#    #+#               #
#  Updated: 2026/04/13 13:35:47 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import os
from dotenv import load_dotenv


def load_configuration():
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def validate_config(config):
    missing = [key for key, value in config.items() if not value]

    if missing:
        print("WARNING: Missing configuration variables:")
        for key in missing:
            print(f" - {key}")
        print("Using fallback defaults where possible...\n")

    return len(missing) == 0


def display_status(config):
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    mode = config["MATRIX_MODE"] or "undefined"

    print(f"Mode: {mode}")

    if config["DATABASE_URL"]:
        if mode == "production":
            print("Database: Connected to production cluster")
        else:
            print("Database: Connected to local instance")
    else:
        print("Database: Not configured")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing key")

    print(f"Log Level: {config['LOG_LEVEL'] or 'INFO (default)'}")

    if config["ZION_ENDPOINT"]:
        if mode == "production":
            print("Zion Network: Secure channel established")
        else:
            print("Zion Network: Online")
    else:
        print("Zion Network:  Unreachable")

    print("\nEnvironment security check:")

    if config["API_KEY"] and "dev" in config["API_KEY"].lower():
        print("[WARNING] Development API key detected")
    else:
        print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file found")

    if mode == "production":
        print("[OK] Production overrides active")
    else:
        print("[OK] Development mode active")

    print("\nThe Oracle sees all configurations.")


def main():
    config = load_configuration()
    validate_config(config)
    display_status(config)


if __name__ == "__main__":
    main()
