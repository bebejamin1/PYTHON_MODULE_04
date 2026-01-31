#! /bin/python3.10

# =============================================================================
# ================================= TEXT ======================================
# =============================================================================


def ft_ancient_text() -> None:
    file = "ancient_fragment.txt"

    print("Accessing Storage Vault: ", file)
    try:
        f = open(file, "r")
    except FileNotFoundError:
        print("\n" + "🚨​ ERROR: Storage vault not found. Run data generator "
              "first.")
    else:
        print("Connection established..." + "\n")
        print("RECOVERED DATA:")
        print(f.read())
        print("\n" + "Data recovery complete. Storage unit disconnected.")
        f.close()


# =============================================================================
# ================================= MAIN ======================================
# =============================================================================


if __name__ == "__main__":
    print(" CYBER ARCHIVES - DATA RECOVERY SYSTEM ".center(79, "=") + "\n")
    ft_ancient_text()
