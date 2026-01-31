#! /bin/python3.10

import sys

# =============================================================================
# ================================= TEXT ======================================
# =============================================================================

def ft_stream_management() -> None:
    sys.stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    sys.stdout.write("\nInput Stream active. Enter archivist ID: ")
    sys.stdout.flush()
    archivist_id = sys.stdin.readline().rstrip('\n')
    sys.stdout.write("Input Stream active. Enter status report: ")
    sys.stdout.flush()
    status_report = sys.stdin.readline().rstrip('\n')

    sys.stdout.write("\n[STANDARD] Archive status from "
                     f"{archivist_id}: {status_report}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels "
                     "verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    sys.stdout.write("\nThree-channel communication test successful.\n")

# =============================================================================
# ================================= TEXT ======================================
# =============================================================================


if __name__ == "__main__":
    # print(" CYBER ARCHIVES - COMMUNICATION SYSTEM ".center(79, "=") + "\n")
    ft_stream_management()
