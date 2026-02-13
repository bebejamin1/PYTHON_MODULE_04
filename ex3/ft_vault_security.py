#! /bin/python3.10

# =============================================================================
# ================================= TEXT ======================================
# =============================================================================


def ft_vault_security() -> None:
    file1 = "classified_data.txt"
    file2 = "security_protocols.txt"
    text = "[CLASSIFIED] New security protocols archived"

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("\n" + "SECURE EXTRACTION:")
    try:
        with open(file1, "r",) as f1:
            print(f1.read())
    except FileNotFoundError:
        print(f"🚨​ No such file or directory: '{file1}'")
    # print(f1.closed)

    print("\n" + "SECURE EXTRACTION:")
    try:
        with open(file2, "w") as f2:
            f2.write(text)
            print(text)
    except FileNotFoundError:
        print(f"🚨​ No such file or directory: '{file2}'")
    # print(f2.closed)

    print("Vault automatically sealed upon completion")


# =============================================================================
# ================================= TEXT ======================================
# =============================================================================


if __name__ == "__main__":
    print(" CYBER ARCHIVES - VAULT SECURITY SYSTEM ".center(79, "=") + "\n")
    ft_vault_security()
    print("\n" + "All vault operations completed with maximum security.")
