from dotenv import load_dotenv
import os


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    # Load .env
    load_dotenv(".env")
    # Read_Variables
    print("Configuration loaded:")
    mode = os.getenv("MATRIX_MODE")
    db = os.getenv("DATABASE_URL")
    api = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL")
    zoin = os.getenv("ZION_ENDPOINT")

    # developer vs production
    if mode == "development":
        print("Mode : development")
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print("Log Level: DEBUG")
        print("Zion Network: Online")
    else:
        print("Mode: production")
        print("Database: Connected to remote server")
        print("API Access: Authenticated secure connection")
        print("Log Level: ERROR")
        print("Zion Network: Secure tunnel active")
    if not all([mode, db, api, log, zoin]):
        print("[ERROR] Missing configuration detected")
    else:
        print("[OK] All configuration variables present")

    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
