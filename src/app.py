# Simple Insurance Helpdesk Ticket System (v1)
# Author: Vamsi Krishna

tickets = []
ticket_id = 1

def create_ticket():
    global ticket_id
    title = input("Issue title: ").strip()
    desc = input("Issue description: ").strip()
    t = {"id": ticket_id, "title": title, "desc": desc, "status": "OPEN"}
    tickets.append(t)
    print(f"✅ Ticket created with ID: {ticket_id}")
    ticket_id += 1

def list_tickets():
    if not tickets:
        print("No tickets yet.")
        return
    for t in tickets:
        print(f"[{t['id']}] {t['title']} | {t['status']}")

def update_status():
    if not tickets:
        print("No tickets to update.")
        return
    try:
        tid = int(input("Enter ticket ID: "))
    except ValueError:
        print("Invalid ID.")
        return
    for t in tickets:
        if t["id"] == tid:
            new_status = input("New status (OPEN/IN_PROGRESS/CLOSED): ").strip().upper()
            if new_status not in {"OPEN", "IN_PROGRESS", "CLOSED"}:
                print("Invalid status.")
                return
            t["status"] = new_status
            print("✅ Status updated.")
            return
    print("Ticket not found.")

def main():
    while True:
        print("\n--- Insurance Helpdesk ---")
        print("1) Create Ticket")
        print("2) List Tickets")
        print("3) Update Status")
        print("4) Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            create_ticket()
        elif choice == "2":
            list_tickets()
        elif choice == "3":
            update_status()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
