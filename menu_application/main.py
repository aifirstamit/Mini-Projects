from app import (
    login,
    logout,
    calculate,
    read_file,
    write_file,
    ApplicationError,
)

from app.logger import (
    log_debug,
    log_info,
    log_warning,
    log_critical,
)


def display_menu():
    """Display the application menu."""

    print("\n" + "=" * 40)
    print("       MENU-DRIVEN APPLICATION")
    print("=" * 40)

    print("1. Login")
    print("2. Calculate")
    print("3. Read a File")
    print("4. Write a File")
    print("5. Logout")

    print("=" * 40)


def main():
    """Run the application."""

    logged_in = False

    log_debug("Application started.")

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        try:

            if choice == "1":

                if logged_in:
                    print("User is already logged in.")
                    log_info(
                        "Login attempted while already logged in."
                    )
                    continue

                login()

                logged_in = True

                print("Login successful.")

            elif choice == "2":

                if not logged_in:
                    log_info(
                        "Calculate attempted without login."
                    )

                    print(
                        "Please login first."
                    )
                    continue

                calculate()

            elif choice == "3":

                if not logged_in:
                    log_info(
                        "Read file attempted without login."
                    )

                    print(
                        "Please login first."
                    )
                    continue

                read_file()

            elif choice == "4":

                if not logged_in:
                    log_info(
                        "Write file attempted without login."
                    )

                    print(
                        "Please login first."
                    )
                    continue

                write_file()

            elif choice == "5":

                if logged_in:
                    logout()
                    logged_in = False

                else:
                    log_info(
                        "Application closed without active login."
                    )

                print("Goodbye!")
                break

            else:

                log_warning(
                    f"Invalid menu choice: {choice}"
                )

                print(
                    "WARNING: Invalid menu choice."
                )

        except ApplicationError as error:

            log_critical(
                f"Application error: {error}"
            )

            print(
                f"ERROR: {error}"
            )

        except Exception as error:

            log_critical(
                f"Unexpected application failure: {error}"
            )

            print(
                "CRITICAL: Unexpected application failure."
            )


if __name__ == "__main__":
    main()