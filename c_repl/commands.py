def handle_command(cmd, buffer):
    if cmd == "§view":
        print("| " + "\n| ".join(buffer.lines))
        return True
    elif cmd == "§generic":
        buffer.generic()
        return True
    elif cmd == "§clear":
        buffer.clear()
        print("Buffer cleared.")
        return True
    elif cmd.startswith("§save "):
        filename = cmd.split(" ", 1)[1]
        buffer.save(filename)
        print(f"Saved to {filename}")
        return True
    elif cmd == "§run":
        buffer.run()
        return True
    elif cmd.lower() == "exit":
        exit(0)
    return False
