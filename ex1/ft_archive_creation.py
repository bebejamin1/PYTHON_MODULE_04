#! /bin/python3.10

# =============================================================================
# ================================= TEXT ======================================
# =============================================================================

def ft_archive_creation() -> None:
    file = "new_discovery.txt"

    text = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
            ]

    print("Initializing new storage unit: ", file)
    f = open(file, "w")
    print("Storage unit created successfully..." + "\n")

    print("Inscribing preservation data...")
    for line in text:
        f.write(line + "\n")
        print(line)
    f.close()

    print("\n" + "Data inscription complete. Storage unit sealed.")
    print(f"Archive '{file}' ready for long-term preservation.")

# =============================================================================
# ================================= MAIN ======================================
# =============================================================================


if __name__ == "__main__":
    print(" CYBER ARCHIVES - PRESERVATION SYSTEM ".center(79, "=") + "\n")
    ft_archive_creation()
