from datetime import datetime

def show_stats(total_queries,blocked_queries):
    total=total_queries+blocked_queries
    percentage=(blocked_queries/total*100) if total else 0
    current_time=datetime.now().strftime("%H:%M:%S")

    print("╔════════ NextDNS Stats ════════╗")
    print(f"║ Updated: {current_time:<21}║")
    print("║                               ║")
    print(f"║ Allowed: {total_queries:<21}║")
    print(f"║ Blocked: {blocked_queries:<21}║")
    print(f"║ Total: {total:<23}║")
    print(f"║ Block rate: {percentage:.2f}%{'':<12} ║")
    print("╚═══════════════════════════════╝")
