#! /bin/python3.10

# =============================================================================
# ================================= TEXT ======================================
# =============================================================================


def ft_crisis_response() -> None:
    files = ["lost_archive.txt",
             "classified_vault.txt",
             "standard_archive.txt"
             ]

    for file in files:
        try:
            with open(file, 'r') as f:
                print("\n" + "ROUTINE ACCESS: "
                      f"Attempting access to '{file}'...")
                print(f"SUCCESS: Archive recovered - \"{f.read()}\"")
                print("STATUS: Normal operations resumed")
        except FileNotFoundError:
            print("\n" + f"CRISIS ALERT: Attempting access to '{file}'...")
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
        except PermissionError:
            print("\n" + f"CRISIS ALERT: Attempting access to '{file}'...")
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")


# =============================================================================
# ================================= MAIN ======================================
# =============================================================================


if __name__ == "__main__":
    print(" CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ".center(79, "="))
    ft_crisis_response()
    print("\n" + "All crisis scenarios handled successfully. Archives secure.")
